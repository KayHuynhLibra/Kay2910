#!/usr/bin/env python3
"""
AI Training Examples 2025 - Các ví dụ về huấn luyện AI
Bao gồm: Fine-tuning, RLHF, Multimodal training, và các kỹ thuật mới nhất
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import json
import logging
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
import matplotlib.pyplot as plt
import seaborn as sns

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TrainingConfig:
    """Cấu hình huấn luyện"""
    model_name: str = "microsoft/DialoGPT-medium"
    batch_size: int = 4
    learning_rate: float = 5e-5
    num_epochs: int = 3
    max_length: int = 512
    warmup_steps: int = 500
    weight_decay: float = 0.01
    gradient_accumulation_steps: int = 4

class CustomDataset(Dataset):
    """Dataset tùy chỉnh cho huấn luyện"""
    
    def __init__(self, texts: List[str], tokenizer, max_length: int = 512):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': encoding['input_ids'].flatten()
        }

class RLHFTrainer:
    """Reinforcement Learning từ Human Feedback Trainer"""
    
    def __init__(self, model, tokenizer, config: TrainingConfig):
        self.model = model
        self.tokenizer = tokenizer
        self.config = config
        self.reward_model = self._create_reward_model()
    
    def _create_reward_model(self):
        """Tạo reward model cho RLHF"""
        # Mô phỏng reward model đơn giản
        class SimpleRewardModel(nn.Module):
            def __init__(self, hidden_size=768):
                super().__init__()
                self.linear = nn.Linear(hidden_size, 1)
                self.sigmoid = nn.Sigmoid()
            
            def forward(self, hidden_states):
                return self.sigmoid(self.linear(hidden_states.mean(dim=1)))
        
        return SimpleRewardModel()
    
    def generate_responses(self, prompts: List[str], num_responses: int = 3) -> List[List[str]]:
        """Tạo nhiều phản hồi cho mỗi prompt"""
        all_responses = []
        
        for prompt in prompts:
            responses = []
            for _ in range(num_responses):
                # Mô phỏng generation với độ đa dạng
                response = self._generate_single_response(prompt)
                responses.append(response)
            all_responses.append(responses)
        
        return all_responses
    
    def _generate_single_response(self, prompt: str) -> str:
        """Tạo một phản hồi cho prompt"""
        # Mô phỏng generation
        responses = [
            "Đây là một phản hồi hữu ích và chính xác.",
            "Tôi có thể giúp bạn với vấn đề này.",
            "Dựa trên thông tin có sẵn, tôi nghĩ rằng...",
            "Đây là cách tiếp cận tốt nhất cho tình huống này."
        ]
        return np.random.choice(responses)
    
    def calculate_rewards(self, responses: List[List[str]]) -> List[List[float]]:
        """Tính toán reward cho các phản hồi"""
        rewards = []
        
        for prompt_responses in responses:
            prompt_rewards = []
            for response in prompt_responses:
                # Mô phỏng reward calculation
                # Trong thực tế, đây sẽ là human feedback hoặc learned reward model
                reward = np.random.uniform(0.1, 1.0)  # Random reward
                prompt_rewards.append(reward)
            rewards.append(prompt_rewards)
        
        return rewards
    
    def train_step(self, prompts: List[str]):
        """Một bước huấn luyện RLHF"""
        # 1. Generate responses
        responses = self.generate_responses(prompts)
        
        # 2. Calculate rewards
        rewards = self.calculate_rewards(responses)
        
        # 3. Update policy (mô phỏng)
        logger.info(f"Generated {len(responses)} response sets")
        logger.info(f"Average reward: {np.mean([np.mean(r) for r in rewards]):.3f}")
        
        return responses, rewards

class MultimodalTrainer:
    """Multimodal AI Trainer"""
    
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.text_encoder = None
        self.image_encoder = None
        self.fusion_layer = None
        self._setup_encoders()
    
    def _setup_encoders(self):
        """Thiết lập các encoder cho multimodal"""
        # Mô phỏng text encoder
        class TextEncoder(nn.Module):
            def __init__(self, vocab_size=50000, hidden_size=768):
                super().__init__()
                self.embedding = nn.Embedding(vocab_size, hidden_size)
                self.transformer = nn.TransformerEncoderLayer(hidden_size, nhead=12)
                self.output_projection = nn.Linear(hidden_size, hidden_size)
            
            def forward(self, input_ids):
                embeddings = self.embedding(input_ids)
                encoded = self.transformer(embeddings)
                return self.output_projection(encoded.mean(dim=1))
        
        # Mô phỏng image encoder
        class ImageEncoder(nn.Module):
            def __init__(self, input_channels=3, hidden_size=768):
                super().__init__()
                self.conv1 = nn.Conv2d(input_channels, 64, 7, stride=2, padding=3)
                self.conv2 = nn.Conv2d(64, 128, 3, stride=2, padding=1)
                self.conv3 = nn.Conv2d(128, 256, 3, stride=2, padding=1)
                self.adaptive_pool = nn.AdaptiveAvgPool2d((1, 1))
                self.output_projection = nn.Linear(256, hidden_size)
            
            def forward(self, images):
                x = torch.relu(self.conv1(images))
                x = torch.relu(self.conv2(x))
                x = torch.relu(self.conv3(x))
                x = self.adaptive_pool(x).flatten(1)
                return self.output_projection(x)
        
        # Fusion layer
        class FusionLayer(nn.Module):
            def __init__(self, hidden_size=768):
                super().__init__()
                self.attention = nn.MultiheadAttention(hidden_size, num_heads=8)
                self.norm = nn.LayerNorm(hidden_size)
                self.output_projection = nn.Linear(hidden_size, hidden_size)
            
            def forward(self, text_features, image_features):
                # Cross-modal attention
                fused_features, _ = self.attention(
                    text_features.unsqueeze(0),
                    image_features.unsqueeze(0),
                    image_features.unsqueeze(0)
                )
                fused_features = self.norm(fused_features.squeeze(0))
                return self.output_projection(fused_features)
        
        self.text_encoder = TextEncoder()
        self.image_encoder = ImageEncoder()
        self.fusion_layer = FusionLayer()
    
    def train_multimodal(self, text_data: List[str], image_data: List[torch.Tensor]):
        """Huấn luyện multimodal model"""
        logger.info("Bắt đầu huấn luyện multimodal model...")
        logger.info(f"Tổng số dữ liệu: {len(text_data)} text, {len(image_data)} images")
        logger.info(f"Batch size: {self.config.batch_size}")
        
        # Mô phỏng training loop
        for epoch in range(self.config.num_epochs):
            total_loss = 0
            num_batches = 0
            
            logger.info(f"Epoch {epoch+1}/{self.config.num_epochs} - Bắt đầu")
            
            for i in range(0, len(text_data), self.config.batch_size):
                batch_texts = text_data[i:i+self.config.batch_size]
                batch_images = image_data[i:i+self.config.batch_size]
                
                logger.info(f"  Batch {num_batches + 1}: {len(batch_texts)} samples")
                logger.info(f"    Text samples: {batch_texts}")
                logger.info(f"    Image shapes: {[img.shape for img in batch_images]}")
                
                # Forward pass
                text_features = self.text_encoder(torch.randint(0, 50000, (len(batch_texts), 512)))
                image_features = self.image_encoder(torch.randn(len(batch_images), 3, 224, 224))
                
                logger.info(f"    Text features shape: {text_features.shape}")
                logger.info(f"    Image features shape: {image_features.shape}")
                
                # Fusion
                fused_features = self.fusion_layer(text_features, image_features)
                logger.info(f"    Fused features shape: {fused_features.shape}")
                
                # Mô phỏng loss calculation
                loss = torch.mean(fused_features ** 2)  # Placeholder loss
                total_loss += loss.item()
                num_batches += 1
                
                logger.info(f"    Loss: {loss.item():.4f}")
            
            if num_batches > 0:
                avg_loss = total_loss / num_batches
                logger.info(f"Epoch {epoch+1}/{self.config.num_epochs}, Average Loss: {avg_loss:.4f}")
            else:
                logger.info(f"Epoch {epoch+1}/{self.config.num_epochs}, No batches processed")
        
        logger.info("Hoàn thành huấn luyện multimodal model!")

class FederatedTrainer:
    """Federated Learning Trainer"""
    
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.global_model = None
        self.client_models = []
        self._setup_models()
    
    def _setup_models(self):
        """Thiết lập global model và client models"""
        # Mô phỏng simple model
        class SimpleModel(nn.Module):
            def __init__(self, input_size=100, hidden_size=50, output_size=10):
                super().__init__()
                self.fc1 = nn.Linear(input_size, hidden_size)
                self.fc2 = nn.Linear(hidden_size, output_size)
                self.relu = nn.ReLU()
            
            def forward(self, x):
                x = self.relu(self.fc1(x))
                return self.fc2(x)
        
        self.global_model = SimpleModel()
        # Tạo client models
        for i in range(5):  # 5 clients
            client_model = SimpleModel()
            client_model.load_state_dict(self.global_model.state_dict())
            self.client_models.append(client_model)
    
    def train_federated(self, client_data: List[torch.Tensor], num_rounds: int = 10):
        """Huấn luyện federated learning"""
        logger.info("Bắt đầu Federated Learning...")
        
        for round_num in range(num_rounds):
            logger.info(f"Federated Round {round_num + 1}/{num_rounds}")
            
            # 1. Train on each client
            client_updates = []
            for i, (client_model, data) in enumerate(zip(self.client_models, client_data)):
                # Local training
                optimizer = optim.SGD(client_model.parameters(), lr=self.config.learning_rate)
                
                for epoch in range(3):  # Local epochs
                    optimizer.zero_grad()
                    outputs = client_model(data)
                    loss = torch.mean(outputs ** 2)  # Placeholder loss
                    loss.backward()
                    optimizer.step()
                
                # Collect model update
                client_updates.append(client_model.state_dict())
            
            # 2. Aggregate updates (FedAvg)
            self._aggregate_models(client_updates)
            
            # 3. Update client models
            for client_model in self.client_models:
                client_model.load_state_dict(self.global_model.state_dict())
            
            logger.info(f"Round {round_num + 1} completed")
        
        logger.info("Federated Learning completed!")
    
    def _aggregate_models(self, client_updates: List[Dict]):
        """Aggregate client model updates"""
        # FedAvg algorithm
        aggregated_state = {}
        
        for key in client_updates[0].keys():
            aggregated_state[key] = torch.zeros_like(client_updates[0][key])
            for update in client_updates:
                aggregated_state[key] += update[key]
            aggregated_state[key] /= len(client_updates)
        
        self.global_model.load_state_dict(aggregated_state)

def demo_ai_training():
    """Demo các phương pháp huấn luyện AI"""
    print("=== AI Training Examples 2025 ===")
    print("=" * 50)
    
    config = TrainingConfig()
    
    # 1. Fine-tuning demo
    print("\n1. Fine-tuning Language Model:")
    try:
        # Mô phỏng tokenizer và model
        class MockTokenizer:
            def __call__(self, text, **kwargs):
                return {'input_ids': torch.randint(0, 50000, (1, 512)), 
                        'attention_mask': torch.ones(1, 512)}
        
        class MockModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.embedding = nn.Embedding(50000, 768)
                self.transformer = nn.TransformerEncoderLayer(768, nhead=12)
            
            def forward(self, input_ids, attention_mask=None):
                embeddings = self.embedding(input_ids)
                return self.transformer(embeddings)
        
        tokenizer = MockTokenizer()
        model = MockModel()
        
        # Tạo sample data
        sample_texts = [
            "Hello, how are you today?",
            "What is the weather like?",
            "Can you help me with this problem?",
            "I need assistance with coding.",
            "Tell me a joke."
        ]
        
        dataset = CustomDataset(sample_texts, tokenizer, config.max_length)
        dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)
        
        print(f"  - Model: Mock Language Model")
        print(f"  - Dataset size: {len(dataset)}")
        print(f"  - Batch size: {config.batch_size}")
        print("  - Fine-tuning setup completed!")
        
    except Exception as e:
        print(f"  - Fine-tuning setup failed: {e}")
    
    # 2. RLHF demo
    print("\n2. Reinforcement Learning từ Human Feedback:")
    try:
        rlhf_trainer = RLHFTrainer(model, tokenizer, config)
        
        prompts = [
            "Explain quantum computing",
            "Write a poem about AI",
            "Solve this math problem: 2x + 5 = 15"
        ]
        
        responses, rewards = rlhf_trainer.train_step(prompts)
        
        print(f"  - Generated {len(responses)} response sets")
        print(f"  - Average reward: {np.mean([np.mean(r) for r in rewards]):.3f}")
        print("  - RLHF training completed!")
        
    except Exception as e:
        print(f"  - RLHF training failed: {e}")
    
    # 3. Multimodal training demo
    print("\n3. Multimodal Training:")
    try:
        multimodal_trainer = MultimodalTrainer(config)
        
        # Tăng số lượng dữ liệu mẫu
        text_data = [
            "A cat sitting on a chair",
            "A dog running in the park", 
            "A bird flying in the sky",
            "A car driving on the road",
            "A person walking on the street",
            "A tree standing in the forest",
            "A flower blooming in the garden",
            "A house standing on the hill"
        ]
        image_data = [torch.randn(3, 224, 224) for _ in range(len(text_data))]
        
        print(f"  - Text data size: {len(text_data)}")
        print(f"  - Image data size: {len(image_data)}")
        print(f"  - Batch size: {config.batch_size}")
        print(f"  - Expected batches: {len(text_data) // config.batch_size + (1 if len(text_data) % config.batch_size > 0 else 0)}")
        
        multimodal_trainer.train_multimodal(text_data, image_data)
        print("  - Multimodal training completed!")
        
    except Exception as e:
        print(f"  - Multimodal training failed: {e}")
        import traceback
        traceback.print_exc()
    
    # 4. Federated learning demo
    print("\n4. Federated Learning:")
    try:
        federated_trainer = FederatedTrainer(config)
        
        # Sample client data
        client_data = [torch.randn(100, 100) for _ in range(5)]
        
        federated_trainer.train_federated(client_data, num_rounds=3)
        print("  - Federated learning completed!")
        
    except Exception as e:
        print(f"  - Federated learning failed: {e}")
    
    print("\n=== Demo hoàn thành! ===")
    print("\nCác phương pháp này đại diện cho xu hướng AI 2025:")
    print("  - Fine-tuning: Tùy chỉnh model cho task cụ thể")
    print("  - RLHF: Cải thiện chất lượng từ human feedback")
    print("  - Multimodal: Xử lý đa phương tiện")
    print("  - Federated: Bảo vệ privacy và học tập phân tán")

if __name__ == "__main__":
    demo_ai_training() 