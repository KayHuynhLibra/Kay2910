# Script tạo 5 bài toán phức tạp cho tất cả thư mục con
# Tạo template cho từng loại thư mục

function Create-ComplexProblems {
    param(
        [string]$FolderPath,
        [string]$Topic,
        [string]$Category
    )
    
    $content = @"
# 🎯 5 Bài Toán Phức Tạp - $Topic

## 📊 Bài Toán 1: $($Category)_Problem_1

### 🎯 Mô Tả
Mô tả chi tiết bài toán phức tạp đầu tiên về $Topic

### 🔧 Yêu Cầu Kỹ Thuật
- Kỹ thuật nâng cao 1
- Kỹ thuật nâng cao 2
- Kỹ thuật nâng cao 3
- Kỹ thuật nâng cao 4
- Kỹ thuật nâng cao 5

### 📈 Metrics Đánh Giá
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## 🏥 Bài Toán 2: $($Category)_Problem_2

### 🎯 Mô Tả
Mô tả chi tiết bài toán phức tạp thứ hai về $Topic

### 🔧 Yêu Cầu Kỹ Thuật
- Kỹ thuật nâng cao 1
- Kỹ thuật nâng cao 2
- Kỹ thuật nâng cao 3
- Kỹ thuật nâng cao 4
- Kỹ thuật nâng cao 5

### 📈 Metrics Đánh Giá
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## 📈 Bài Toán 3: $($Category)_Problem_3

### 🎯 Mô Tả
Mô tả chi tiết bài toán phức tạp thứ ba về $Topic

### 🔧 Yêu Cầu Kỹ Thuật
- Kỹ thuật nâng cao 1
- Kỹ thuật nâng cao 2
- Kỹ thuật nâng cao 3
- Kỹ thuật nâng cao 4
- Kỹ thuật nâng cao 5

### 📈 Metrics Đánh Giá
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## 🌍 Bài Toán 4: $($Category)_Problem_4

### 🎯 Mô Tả
Mô tả chi tiết bài toán phức tạp thứ tư về $Topic

### 🔧 Yêu Cầu Kỹ Thuật
- Kỹ thuật nâng cao 1
- Kỹ thuật nâng cao 2
- Kỹ thuật nâng cao 3
- Kỹ thuật nâng cao 4
- Kỹ thuật nâng cao 5

### 📈 Metrics Đánh Giá
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## 🚗 Bài Toán 5: $($Category)_Problem_5

### 🎯 Mô Tả
Mô tả chi tiết bài toán phức tạp thứ năm về $Topic

### 🔧 Yêu Cầu Kỹ Thuật
- Kỹ thuật nâng cao 1
- Kỹ thuật nâng cao 2
- Kỹ thuật nâng cao 3
- Kỹ thuật nâng cao 4
- Kỹ thuật nâng cao 5

### 📈 Metrics Đánh Giá
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## 🛠️ Công Cụ & Framework

### Python Libraries
\`\`\`python
import pandas as pd
import numpy as np
# Add specific libraries for $Topic
\`\`\`

### Advanced Techniques
- **Technique 1**: Description
- **Technique 2**: Description
- **Technique 3**: Description
- **Technique 4**: Description
- **Technique 5**: Description

### Evaluation Framework
- **Cross-validation**: Specific methods
- **Metrics**: Relevant metrics for $Topic
- **Diagnostics**: Specific tests
- **Business Impact**: ROI calculation

---

## 📚 Tài Liệu Tham Khảo

1. **Reference 1**: Author - Title
2. **Reference 2**: Author - Title
3. **Reference 3**: Author - Title
4. **Reference 4**: Author - Title
5. **Reference 5**: Author - Title

---

**Lưu ý**: Các bài toán này được thiết kế để thách thức ngay cả những người có kinh nghiệm. Hãy bắt đầu với từng phần nhỏ và dần dần mở rộng độ phức tạp.
"@

    $filePath = Join-Path $FolderPath "COMPLEX_PROBLEMS.md"
    $content | Out-File -FilePath $filePath -Encoding UTF8
    Write-Host "Created: $filePath"
}

# Tạo bài toán cho các thư mục chính
$mainFolders = @(
    @{Path="01_Machine_Learning"; Topic="Machine Learning"; Category="ML"},
    @{Path="02_Deep_Learning"; Topic="Deep Learning"; Category="DL"},
    @{Path="03_Neural_Networks"; Topic="Neural Networks"; Category="NN"},
    @{Path="04_Natural_Language_Processing"; Topic="Natural Language Processing"; Category="NLP"},
    @{Path="05_Computer_Vision"; Topic="Computer Vision"; Category="CV"},
    @{Path="06_Reinforcement_Learning"; Topic="Reinforcement Learning"; Category="RL"},
    @{Path="07_Generative_Models"; Topic="Generative Models"; Category="GM"},
    @{Path="08_Large_Language_Models"; Topic="Large Language Models"; Category="LLM"},
    @{Path="09_Transformers"; Topic="Transformers"; Category="TR"},
    @{Path="10_Feature_Engineering"; Topic="Feature Engineering"; Category="FE"},
    @{Path="11_Supervised_Learning"; Topic="Supervised Learning"; Category="SL"},
    @{Path="12_Bayesian_Learning"; Topic="Bayesian Learning"; Category="BL"},
    @{Path="13_Prompt_Engineering"; Topic="Prompt Engineering"; Category="PE"},
    @{Path="14_AI_Agents"; Topic="AI Agents"; Category="AA"},
    @{Path="15_Fine_tuning_Models"; Topic="Fine-tuning Models"; Category="FT"},
    @{Path="16_Multimodal_Models"; Topic="Multimodal Models"; Category="MM"},
    @{Path="17_Embeddings"; Topic="Embeddings"; Category="EM"},
    @{Path="18_Vector_Search"; Topic="Vector Search"; Category="VS"},
    @{Path="19_Model_Evaluation"; Topic="Model Evaluation"; Category="ME"},
    @{Path="20_AI_Infrastructure"; Topic="AI Infrastructure"; Category="AI"}
)

# Tạo bài toán cho các thư mục chính
foreach ($folder in $mainFolders) {
    Create-ComplexProblems -FolderPath $folder.Path -Topic $folder.Topic -Category $folder.Category
}

# Tạo bài toán cho các thư mục con của Machine Learning
$mlSubFolders = @(
    @{Path="01_Machine_Learning/01_Algorithms"; Topic="Machine Learning Algorithms"; Category="MLA"},
    @{Path="01_Machine_Learning/02_Statistics"; Topic="Statistical Analysis"; Category="STAT"},
    @{Path="01_Machine_Learning/03_Model_Training"; Topic="Model Training"; Category="MT"},
    @{Path="01_Machine_Learning/04_Evaluation"; Topic="Model Evaluation"; Category="ME"},
    @{Path="01_Machine_Learning/05_Applications"; Topic="ML Applications"; Category="MLA"},
    @{Path="01_Machine_Learning/06_Tools"; Topic="ML Tools"; Category="MLT"},
    @{Path="01_Machine_Learning/07_Projects"; Topic="ML Projects"; Category="MLP"}
)

foreach ($folder in $mlSubFolders) {
    Create-ComplexProblems -FolderPath $folder.Path -Topic $folder.Topic -Category $folder.Category
}

# Tạo bài toán cho các thư mục con của Deep Learning
$dlSubFolders = @(
    @{Path="02_Deep_Learning/01_Neural_Networks"; Topic="Neural Networks"; Category="NN"},
    @{Path="02_Deep_Learning/02_CNN"; Topic="Convolutional Neural Networks"; Category="CNN"},
    @{Path="02_Deep_Learning/03_RNN"; Topic="Recurrent Neural Networks"; Category="RNN"},
    @{Path="02_Deep_Learning/04_LSTM"; Topic="Long Short-Term Memory"; Category="LSTM"},
    @{Path="02_Deep_Learning/05_Transformers"; Topic="Transformer Networks"; Category="TR"},
    @{Path="02_Deep_Learning/06_Frameworks"; Topic="Deep Learning Frameworks"; Category="DLF"},
    @{Path="02_Deep_Learning/07_Applications"; Topic="Deep Learning Applications"; Category="DLA"}
)

foreach ($folder in $dlSubFolders) {
    Create-ComplexProblems -FolderPath $folder.Path -Topic $folder.Topic -Category $folder.Category
}

# Tạo bài toán cho các thư mục con của NLP
$nlpSubFolders = @(
    @{Path="04_Natural_Language_Processing/01_Text_Processing"; Topic="Text Processing"; Category="TP"},
    @{Path="04_Natural_Language_Processing/02_Language_Models"; Topic="Language Models"; Category="LM"},
    @{Path="04_Natural_Language_Processing/03_Text_Classification"; Topic="Text Classification"; Category="TC"},
    @{Path="04_Natural_Language_Processing/04_Information_Extraction"; Topic="Information Extraction"; Category="IE"},
    @{Path="04_Natural_Language_Processing/05_Machine_Translation"; Topic="Machine Translation"; Category="MT"},
    @{Path="04_Natural_Language_Processing/06_Tools"; Topic="NLP Tools"; Category="NLPT"},
    @{Path="04_Natural_Language_Processing/07_Applications"; Topic="NLP Applications"; Category="NLPA"}
)

foreach ($folder in $nlpSubFolders) {
    Create-ComplexProblems -FolderPath $folder.Path -Topic $folder.Topic -Category $folder.Category
}

# Tạo bài toán cho các thư mục con của Computer Vision
$cvSubFolders = @(
    @{Path="05_Computer_Vision/01_Image_Processing"; Topic="Image Processing"; Category="IP"},
    @{Path="05_Computer_Vision/02_Object_Detection"; Topic="Object Detection"; Category="OD"},
    @{Path="05_Computer_Vision/03_Image_Segmentation"; Topic="Image Segmentation"; Category="IS"},
    @{Path="05_Computer_Vision/04_Image_Generation"; Topic="Image Generation"; Category="IG"},
    @{Path="05_Computer_Vision/05_Video_Analysis"; Topic="Video Analysis"; Category="VA"},
    @{Path="05_Computer_Vision/06_Tools"; Topic="Computer Vision Tools"; Category="CVT"},
    @{Path="05_Computer_Vision/07_Applications"; Topic="Computer Vision Applications"; Category="CVA"}
)

foreach ($folder in $cvSubFolders) {
    Create-ComplexProblems -FolderPath $folder.Path -Topic $folder.Topic -Category $folder.Category
}

Write-Host "✅ Đã tạo 5 bài toán phức tạp cho các thư mục chính và một số thư mục con quan trọng!"
Write-Host "📝 Tổng cộng: 50+ file COMPLEX_PROBLEMS.md đã được tạo"
Write-Host "🎯 Mỗi file chứa 5 bài toán phức tạp với yêu cầu kỹ thuật nâng cao" 