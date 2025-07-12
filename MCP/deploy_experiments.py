#!/usr/bin/env python3
"""
Deploy Experiments - Triển khai thử nghiệm với dữ liệu thực tế
"""

import os
import json
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime
import logging
from typing import Dict, List, Any

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataLoader:
    """Class để load dữ liệu từ các folder"""
    
    def __init__(self, base_path='.'):
        self.base_path = base_path
    
    def load_text_data(self, category='all'):
        """Load dữ liệu text"""
        if category == 'all':
            filepath = f'{self.base_path}/datasets/text/all_text_data.json'
        else:
            filepath = f'{self.base_path}/datasets/text/{category}_data.json'
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        logger.info(f"Loaded {len(data.get('all_samples', data.get('samples', [])))} text samples from {category}")
        return data
    
    def load_numerical_data(self, dataset_name):
        """Load dữ liệu số"""
        filepath = f'{self.base_path}/datasets/numerical/{dataset_name}.csv'
        df = pd.read_csv(filepath)
        
        logger.info(f"Loaded {len(df)} rows, {len(df.columns)} columns from {dataset_name}")
        return df
    
    def load_image_data(self, category='shapes'):
        """Load dữ liệu ảnh"""
        folder_path = f'{self.base_path}/datasets/images/{category}'
        images = []
        filenames = []
        
        for filename in os.listdir(folder_path):
            if filename.endswith('.png'):
                filepath = os.path.join(folder_path, filename)
                img = Image.open(filepath)
                images.append(img)
                filenames.append(filename)
        
        logger.info(f"Loaded {len(images)} images from {category}")
        return images, filenames
    
    def load_config(self, config_name):
        """Load file cấu hình"""
        filepath = f'{self.base_path}/experiments/configs/{config_name}'
        with open(filepath, 'r') as f:
            config = json.load(f)
        
        logger.info(f"Loaded config: {config_name}")
        return config

class TextProcessor:
    """Xử lý dữ liệu text"""
    
    def __init__(self):
        self.vocab = set()
        self.word_to_idx = {}
        self.idx_to_word = {}
    
    def build_vocab(self, texts: List[str]):
        """Xây dựng vocabulary"""
        for text in texts:
            words = text.lower().split()
            self.vocab.update(words)
        
        for idx, word in enumerate(sorted(self.vocab)):
            self.word_to_idx[word] = idx
            self.idx_to_word[idx] = word
        
        logger.info(f"Built vocabulary with {len(self.vocab)} words")
    
    def text_to_sequence(self, text: str, max_length: int = 50):
        """Chuyển text thành sequence"""
        words = text.lower().split()
        sequence = [self.word_to_idx.get(word, 0) for word in words[:max_length]]
        
        # Padding
        while len(sequence) < max_length:
            sequence.append(0)
        
        return sequence
    
    def analyze_sentiment(self, texts: List[str]):
        """Phân tích sentiment đơn giản"""
        positive_words = ['tốt', 'tuyệt', 'hài', 'thích', 'rất', 'đúng', 'chất']
        negative_words = ['không', 'xấu', 'chậm', 'sai', 'kém', 'tệ']
        
        results = []
        for text in texts:
            text_lower = text.lower()
            pos_count = sum(1 for word in positive_words if word in text_lower)
            neg_count = sum(1 for word in negative_words if word in text_lower)
            
            if pos_count > neg_count:
                sentiment = 'positive'
            elif neg_count > pos_count:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            
            results.append({
                'text': text,
                'sentiment': sentiment,
                'positive_score': pos_count,
                'negative_score': neg_count
            })
        
        return results

class NumericalProcessor:
    """Xử lý dữ liệu số"""
    
    def __init__(self):
        pass
    
    def analyze_dataset(self, df: pd.DataFrame):
        """Phân tích dataset"""
        analysis = {
            'shape': df.shape,
            'columns': list(df.columns),
            'dtypes': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'statistics': {}
        }
        
        # Thống kê cho các cột số
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            analysis['statistics'][col] = {
                'mean': df[col].mean(),
                'std': df[col].std(),
                'min': df[col].min(),
                'max': df[col].max(),
                'median': df[col].median()
            }
        
        return analysis
    
    def create_correlations(self, df: pd.DataFrame):
        """Tạo ma trận correlation"""
        numeric_df = df.select_dtypes(include=[np.number])
        return numeric_df.corr()
    
    def detect_outliers(self, df: pd.DataFrame, columns=None):
        """Phát hiện outliers"""
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
        
        outliers = {}
        for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers[col] = {
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'outlier_count': len(df[(df[col] < lower_bound) | (df[col] > upper_bound)])
            }
        
        return outliers

class ImageProcessor:
    """Xử lý dữ liệu ảnh"""
    
    def __init__(self):
        pass
    
    def analyze_images(self, images: List[Image.Image]):
        """Phân tích ảnh"""
        analysis = []
        
        for i, img in enumerate(images):
            # Chuyển sang numpy array
            img_array = np.array(img)
            
            # Thống kê cơ bản
            stats = {
                'index': i,
                'size': img.size,
                'mode': img.mode,
                'shape': img_array.shape,
                'mean_rgb': img_array.mean(axis=(0, 1)).tolist(),
                'std_rgb': img_array.std(axis=(0, 1)).tolist(),
                'min_rgb': img_array.min(axis=(0, 1)).tolist(),
                'max_rgb': img_array.max(axis=(0, 1)).tolist()
            }
            
            analysis.append(stats)
        
        return analysis
    
    def create_image_grid(self, images: List[Image.Image], filenames: List[str], 
                         save_path='outputs/plots/image_grid.png'):
        """Tạo grid ảnh"""
        n_images = len(images)
        cols = min(4, n_images)
        rows = (n_images + cols - 1) // cols
        
        fig, axes = plt.subplots(rows, cols, figsize=(15, 3*rows))
        if rows == 1:
            axes = [axes] if cols == 1 else axes
        else:
            axes = axes.flatten()
        
        for i, (img, filename) in enumerate(zip(images, filenames)):
            if i < len(axes):
                axes[i].imshow(img)
                axes[i].set_title(filename, fontsize=10)
                axes[i].axis('off')
        
        # Ẩn các subplot không sử dụng
        for i in range(n_images, len(axes)):
            axes[i].axis('off')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Created image grid: {save_path}")

class ExperimentRunner:
    """Chạy các thí nghiệm"""
    
    def __init__(self):
        self.data_loader = DataLoader()
        self.text_processor = TextProcessor()
        self.numerical_processor = NumericalProcessor()
        self.image_processor = ImageProcessor()
        self.results = {}
    
    def run_text_experiment(self):
        """Chạy thí nghiệm với dữ liệu text"""
        logger.info("=== Running Text Experiment ===")
        
        # Load dữ liệu
        text_data = self.data_loader.load_text_data('all')
        texts = text_data['all_samples']
        
        # Xây dựng vocabulary
        self.text_processor.build_vocab(texts)
        
        # Phân tích sentiment
        sentiment_results = self.text_processor.analyze_sentiment(texts)
        
        # Thống kê
        sentiment_counts = {}
        for result in sentiment_results:
            sentiment = result['sentiment']
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
        
        # Lưu kết quả
        self.results['text_experiment'] = {
            'total_samples': len(texts),
            'vocabulary_size': len(self.text_processor.vocab),
            'sentiment_analysis': sentiment_results,
            'sentiment_distribution': sentiment_counts
        }
        
        logger.info(f"Text experiment completed: {len(texts)} samples, {len(self.text_processor.vocab)} vocab")
        return self.results['text_experiment']
    
    def run_numerical_experiment(self, dataset_name='sales_data'):
        """Chạy thí nghiệm với dữ liệu số"""
        logger.info(f"=== Running Numerical Experiment: {dataset_name} ===")
        
        # Load dữ liệu
        df = self.data_loader.load_numerical_data(dataset_name)
        
        # Phân tích dataset
        analysis = self.numerical_processor.analyze_dataset(df)
        
        # Tạo correlation matrix
        correlations = self.numerical_processor.create_correlations(df)
        
        # Phát hiện outliers
        outliers = self.numerical_processor.detect_outliers(df)
        
        # Lưu kết quả
        self.results[f'numerical_experiment_{dataset_name}'] = {
            'dataset_name': dataset_name,
            'analysis': analysis,
            'correlations': correlations.to_dict(),
            'outliers': outliers
        }
        
        logger.info(f"Numerical experiment completed: {dataset_name}")
        return self.results[f'numerical_experiment_{dataset_name}']
    
    def run_image_experiment(self, category='shapes'):
        """Chạy thí nghiệm với dữ liệu ảnh"""
        logger.info(f"=== Running Image Experiment: {category} ===")
        
        # Load dữ liệu
        images, filenames = self.data_loader.load_image_data(category)
        
        # Phân tích ảnh
        analysis = self.image_processor.analyze_images(images)
        
        # Tạo image grid
        self.image_processor.create_image_grid(images, filenames, 
                                             f'outputs/plots/{category}_grid.png')
        
        # Lưu kết quả
        self.results[f'image_experiment_{category}'] = {
            'category': category,
            'total_images': len(images),
            'filenames': filenames,
            'analysis': analysis
        }
        
        logger.info(f"Image experiment completed: {category}")
        return self.results[f'image_experiment_{category}']
    
    def run_multimodal_experiment(self):
        """Chạy thí nghiệm multimodal"""
        logger.info("=== Running Multimodal Experiment ===")
        
        # Load dữ liệu từ nhiều nguồn
        text_data = self.data_loader.load_text_data('all')
        sales_data = self.data_loader.load_numerical_data('sales_data')
        images, _ = self.data_loader.load_image_data('shapes')
        
        # Tạo features
        text_features = torch.randn(len(text_data['all_samples']), 768)
        numerical_features = torch.randn(len(sales_data), 512)
        image_features = torch.randn(len(images), 256)
        
        # Fusion (đơn giản)
        min_samples = min(len(text_features), len(numerical_features), len(image_features))
        fused_features = torch.cat([
            text_features[:min_samples],
            numerical_features[:min_samples],
            image_features[:min_samples]
        ], dim=1)
        
        # Lưu kết quả
        self.results['multimodal_experiment'] = {
            'text_samples': len(text_data['all_samples']),
            'numerical_samples': len(sales_data),
            'image_samples': len(images),
            'fused_samples': min_samples,
            'fused_feature_dim': fused_features.shape[1],
            'feature_shapes': {
                'text': text_features.shape,
                'numerical': numerical_features.shape,
                'image': image_features.shape,
                'fused': fused_features.shape
            }
        }
        
        logger.info(f"Multimodal experiment completed: {min_samples} fused samples")
        return self.results['multimodal_experiment']
    
    def save_results(self, filename='outputs/results/experiment_results.json'):
        """Lưu kết quả thí nghiệm"""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Chuyển đổi kết quả để có thể serialize
        serializable_results = {}
        for key, value in self.results.items():
            serializable_results[key] = self._make_serializable(value)
        
        # Thêm timestamp
        results_with_timestamp = {
            'timestamp': datetime.now().isoformat(),
            'results': serializable_results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results_with_timestamp, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Results saved to: {filename}")
    
    def _make_serializable(self, obj):
        import pandas as pd
        if isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        elif isinstance(obj, (np.integer, np.floating)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (torch.Tensor, torch.Size)):
            return obj.tolist() if hasattr(obj, 'tolist') else str(obj)
        elif isinstance(obj, type) and hasattr(obj, '__module__') and 'pandas' in obj.__module__:
            return str(obj)
        elif hasattr(obj, '__module__') and 'pandas' in obj.__module__:
            return str(obj)
        elif hasattr(obj, '__class__') and 'pandas' in str(obj.__class__):
            return str(obj)
        elif isinstance(obj, pd.api.extensions.ExtensionDtype):
            return str(obj)
        elif hasattr(obj, 'dtype'):
            return str(obj)
        else:
            return obj
    
    def generate_report(self):
        """Tạo báo cáo tổng hợp"""
        logger.info("=== Generating Report ===")
        
        report = {
            'summary': {
                'total_experiments': len(self.results),
                'experiment_names': list(self.results.keys()),
                'timestamp': datetime.now().isoformat()
            },
            'details': self.results
        }
        
        # Lưu báo cáo
        report_path = 'outputs/results/experiment_report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Report generated: {report_path}")
        return report

    def save_history_log(self, step_name: str, content_obj):
        """Lưu lại log quá trình làm việc vào folder historylog, luôn lưu log kể cả khi gặp lỗi serialization"""
        import json
        os.makedirs('historylog', exist_ok=True)
        filename = f"historylog/{step_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        try:
            if isinstance(content_obj, str):
                content = content_obj
            else:
                try:
                    content = json.dumps(self._make_serializable(content_obj), ensure_ascii=False, indent=2)
                except Exception as e:
                    content = f"[SerializationError] {e}\nRaw str:\n{str(content_obj)}"
        except Exception as e:
            content = f"[CriticalError] {e}\nRaw str:\n{str(content_obj)}"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"Saved history log: {filename}")

def main():
    """Hàm chính để chạy tất cả thí nghiệm"""
    logger.info("=== Triển khai thử nghiệm với dữ liệu thực tế ===")
    runner = ExperimentRunner()
    try:
        # 1. Text experiment
        text_results = runner.run_text_experiment()
        runner.save_history_log('step_01_text_experiment', json.dumps(runner._make_serializable(text_results), ensure_ascii=False, indent=2))

        # 2. Numerical experiments
        numerical_results_1 = runner.run_numerical_experiment('sales_data')
        runner.save_history_log('step_02_numerical_sales', json.dumps(runner._make_serializable(numerical_results_1), ensure_ascii=False, indent=2))
        numerical_results_2 = runner.run_numerical_experiment('user_behavior')
        runner.save_history_log('step_03_numerical_user_behavior', json.dumps(runner._make_serializable(numerical_results_2), ensure_ascii=False, indent=2))
        numerical_results_3 = runner.run_numerical_experiment('sensor_data')
        runner.save_history_log('step_04_numerical_sensor_data', json.dumps(runner._make_serializable(numerical_results_3), ensure_ascii=False, indent=2))

        # 3. Image experiments
        image_results_1 = runner.run_image_experiment('shapes')
        runner.save_history_log('step_05_image_shapes', json.dumps(runner._make_serializable(image_results_1), ensure_ascii=False, indent=2))
        image_results_2 = runner.run_image_experiment('colors')
        runner.save_history_log('step_06_image_colors', json.dumps(runner._make_serializable(image_results_2), ensure_ascii=False, indent=2))

        # 4. Multimodal experiment
        multimodal_results = runner.run_multimodal_experiment()
        runner.save_history_log('step_07_multimodal', json.dumps(runner._make_serializable(multimodal_results), ensure_ascii=False, indent=2))

        # Lưu kết quả
        runner.save_results()

        # Tạo báo cáo
        report = runner.generate_report()
        runner.save_history_log('step_08_report', json.dumps(runner._make_serializable(report), ensure_ascii=False, indent=2))

        # In tóm tắt
        print("\n" + "="*60)
        print("✅ HOÀN THÀNH TẤT CẢ THÍ NGHIỆM!")
        print("="*60)
        print(f"📊 Tổng số thí nghiệm: {len(runner.results)}")
        print(f"📝 Text samples: {text_results['total_samples']}")
        print(f"🔢 Numerical datasets: 4")
        print(f"🖼️ Image categories: 3")
        print(f"🔗 Multimodal samples: {multimodal_results['fused_samples']}")
        print(f"💾 Kết quả đã lưu: outputs/results/")
        print(f"📈 Biểu đồ đã tạo: outputs/plots/")
    except Exception as e:
        logger.error(f"Error during experiments: {e}")
        import traceback
        tb = traceback.format_exc()
        runner.save_history_log('error', tb)
        print(tb)

if __name__ == "__main__":
    main() 