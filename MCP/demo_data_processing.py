#!/usr/bin/env python3
"""
Demo Data Processing - Hiển thị chi tiết về việc chia dữ liệu và xử lý
"""

import torch
import numpy as np
from typing import List, Tuple
import json

def create_sample_data():
    """Tạo dữ liệu mẫu đa dạng"""
    print("=== Tạo dữ liệu mẫu ===")
    
    # Text data
    text_data = [
        "A cat sitting on a chair",
        "A dog running in the park", 
        "A bird flying in the sky",
        "A car driving on the road",
        "A person walking on the street",
        "A tree standing in the forest",
        "A flower blooming in the garden",
        "A house standing on the hill",
        "A computer on the desk",
        "A book lying on the table",
        "A phone ringing in the room",
        "A clock hanging on the wall"
    ]
    
    # Image data (mô phỏng)
    image_data = [torch.randn(3, 224, 224) for _ in range(len(text_data))]
    
    # Numerical data
    numerical_data = np.random.randn(len(text_data), 10)
    
    print(f"Text data: {len(text_data)} samples")
    print(f"Image data: {len(image_data)} samples")
    print(f"Numerical data: {numerical_data.shape}")
    
    return text_data, image_data, numerical_data

def split_data_into_batches(data: List, batch_size: int, data_type: str = "data"):
    """Chia dữ liệu thành các batch"""
    print(f"\n=== Chia {data_type} thành batches (batch_size={batch_size}) ===")
    
    batches = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        batches.append(batch)
        print(f"Batch {len(batches)}: {len(batch)} samples")
        if data_type == "text":
            print(f"  Samples: {batch}")
        elif data_type == "image":
            print(f"  Shapes: {[item.shape for item in batch]}")
        elif data_type == "numerical":
            print(f"  Shape: {batch.shape}")
    
    return batches

def process_batch(batch_texts: List[str], batch_images: List[torch.Tensor], 
                 batch_numerical: np.ndarray, batch_id: int):
    """Xử lý một batch dữ liệu"""
    print(f"\n--- Xử lý Batch {batch_id} ---")
    
    # 1. Text processing
    print("1. Text Processing:")
    for i, text in enumerate(batch_texts):
        word_count = len(text.split())
        char_count = len(text)
        print(f"   Sample {i+1}: '{text}'")
        print(f"     - Words: {word_count}, Characters: {char_count}")
    
    # 2. Image processing
    print("\n2. Image Processing:")
    for i, image in enumerate(batch_images):
        total_pixels = image.numel()
        mean_value = image.mean().item()
        std_value = image.std().item()
        print(f"   Sample {i+1}: Shape {image.shape}")
        print(f"     - Total pixels: {total_pixels:,}")
        print(f"     - Mean: {mean_value:.4f}, Std: {std_value:.4f}")
    
    # 3. Numerical processing
    print("\n3. Numerical Processing:")
    print(f"   Shape: {batch_numerical.shape}")
    print(f"   Mean: {batch_numerical.mean():.4f}")
    print(f"   Std: {batch_numerical.std():.4f}")
    print(f"   Min: {batch_numerical.min():.4f}")
    print(f"   Max: {batch_numerical.max():.4f}")
    
    # 4. Feature extraction (mô phỏng)
    print("\n4. Feature Extraction:")
    text_features = torch.randn(len(batch_texts), 768)  # Mô phỏng text features
    image_features = torch.randn(len(batch_images), 512)  # Mô phỏng image features
    numerical_features = torch.randn(batch_numerical.shape[0], 256)  # Mô phỏng numerical features
    
    print(f"   Text features: {text_features.shape}")
    print(f"   Image features: {image_features.shape}")
    print(f"   Numerical features: {numerical_features.shape}")
    
    # 5. Fusion (mô phỏng)
    print("\n5. Feature Fusion:")
    # Giả sử chúng ta có cùng số lượng samples
    fused_features = torch.cat([text_features, image_features, numerical_features], dim=1)
    print(f"   Fused features: {fused_features.shape}")
    print(f"   Total features per sample: {fused_features.shape[1]}")
    
    return fused_features

def demo_data_processing():
    """Demo chính về xử lý dữ liệu"""
    print("=== Demo Data Processing ===")
    print("Hiển thị chi tiết về việc chia dữ liệu và xử lý")
    print("=" * 50)
    
    # 1. Tạo dữ liệu
    text_data, image_data, numerical_data = create_sample_data()
    
    # 2. Chia thành batches với các batch size khác nhau
    batch_sizes = [3, 4, 6]
    
    for batch_size in batch_sizes:
        print(f"\n{'='*60}")
        print(f"THỬ NGHIỆM VỚI BATCH SIZE = {batch_size}")
        print(f"{'='*60}")
        
        # Chia dữ liệu
        text_batches = split_data_into_batches(text_data, batch_size, "text")
        image_batches = split_data_into_batches(image_data, batch_size, "image")
        numerical_batches = [numerical_data[i:i+batch_size] for i in range(0, len(numerical_data), batch_size)]
        
        # Xử lý từng batch
        all_features = []
        for i, (text_batch, image_batch, numerical_batch) in enumerate(zip(text_batches, image_batches, numerical_batches)):
            features = process_batch(text_batch, image_batch, numerical_batch, i+1)
            all_features.append(features)
        
        # Tổng kết
        print(f"\n--- TỔNG KẾT BATCH SIZE {batch_size} ---")
        print(f"Số batch: {len(all_features)}")
        print(f"Tổng features: {sum(f.shape[0] for f in all_features)} samples")
        print(f"Feature dimension: {all_features[0].shape[1] if all_features else 0}")
        
        if all_features:
            combined_features = torch.cat(all_features, dim=0)
            print(f"Combined features shape: {combined_features.shape}")
            print(f"Memory usage: {combined_features.numel() * 4 / 1024:.2f} KB")

def demo_statistics():
    """Demo thống kê dữ liệu"""
    print("\n=== Demo Statistics ===")
    
    # Tạo dữ liệu lớn hơn để demo
    n_samples = 1000
    print(f"Tạo {n_samples} samples để demo thống kê...")
    
    # Tạo dữ liệu với phân phối khác nhau
    normal_data = np.random.normal(0, 1, (n_samples, 10))
    uniform_data = np.random.uniform(-1, 1, (n_samples, 10))
    categorical_data = np.random.choice(['A', 'B', 'C', 'D'], n_samples)
    
    print("\n1. Normal Distribution Data:")
    print(f"   Shape: {normal_data.shape}")
    print(f"   Mean: {normal_data.mean():.4f}")
    print(f"   Std: {normal_data.std():.4f}")
    print(f"   Min: {normal_data.min():.4f}")
    print(f"   Max: {normal_data.max():.4f}")
    
    print("\n2. Uniform Distribution Data:")
    print(f"   Shape: {uniform_data.shape}")
    print(f"   Mean: {uniform_data.mean():.4f}")
    print(f"   Std: {uniform_data.std():.4f}")
    print(f"   Min: {uniform_data.min():.4f}")
    print(f"   Max: {uniform_data.max():.4f}")
    
    print("\n3. Categorical Data:")
    print(f"   Shape: {categorical_data.shape}")
    unique, counts = np.unique(categorical_data, return_counts=True)
    for value, count in zip(unique, counts):
        print(f"   {value}: {count} ({count/n_samples*100:.1f}%)")

if __name__ == "__main__":
    # Chạy demo chính
    demo_data_processing()
    
    # Chạy demo thống kê
    demo_statistics()
    
    print("\n=== Demo hoàn thành! ===")
    print("Bạn đã thấy được:")
    print("1. Cách chia dữ liệu thành batches")
    print("2. Xử lý từng loại dữ liệu (text, image, numerical)")
    print("3. Feature extraction và fusion")
    print("4. Thống kê dữ liệu với các phân phối khác nhau") 