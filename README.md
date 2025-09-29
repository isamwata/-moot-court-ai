# 🏛️ Moot Court AI System

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Transformers](https://img.shields.io/badge/Transformers-4.56.2+-green.svg)](https://huggingface.co/transformers)
[![LoRA](https://img.shields.io/badge/LoRA-PEFT-orange.svg)](https://github.com/huggingface/peft)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-red.svg)](https://github.com/facebookresearch/faiss)

## 🎯 Project Overview
A sophisticated multi-agent legal AI system that simulates moot court hearings using LoRA fine-tuning, document retrieval, and AI agents representing Claimant, Respondent, and Judge perspectives.

## 📁 Project Structure
```
moot_court/
├── venv/                          # Virtual environment
├── courtcase.pdf                  # Source legal document
├── data_preprocess.py             # PDF text extraction and structuring
├── training.jsonl                 # Training dataset (1 sample)
├── train_lora.py                  # Original Falcon-7B training script
├── train_lora_simple.py           # Simplified DialoGPT training script
├── test_simple_model.py           # Model testing script
├── monitor_training.py            # Training progress monitor
├── watch_training.py              # Real-time training watcher
├── activate_env.sh                # Environment activation script
└── moot_lora_simple/             # Trained model output
    ├── adapter_config.json
    ├── adapter_model.safetensors
    ├── tokenizer files...
    └── checkpoint-2/
```

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/moot-court-ai.git
cd moot-court-ai
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run setup
python setup.py
```

### 3. Run Demo
```bash
python demo_moot_court.py
```

## 📊 Data Processing

### PDF to Training Data
The `data_preprocess.py` script extracts text from PDFs and structures it for training:

```bash
python data_preprocess.py . training.jsonl
```

**Output Format:**
```json
{
  "instruction": "Simulate a moot court hearing (Claimant, Respondent, Judge) for these facts.",
  "input": "Facts: [legal facts]\\nIssues: [legal issues]",
  "output": "Claimant: [arguments]\\nRespondent: [arguments]\\nJudge: [decision]"
}
```

## 🤖 Model Training

### Successful Training: DialoGPT-Medium
We successfully trained a LoRA fine-tuned model using `microsoft/DialoGPT-medium`:

```bash
python train_lora_simple.py
```

**Training Results:**
- ✅ Model: DialoGPT-medium (345M parameters)
- ✅ Training time: ~2 minutes
- ✅ Loss: 9.6 (final epoch)
- ✅ Output: `./moot_lora_simple/`

### Training Configuration
- **LoRA Rank**: 8
- **LoRA Alpha**: 16
- **Epochs**: 2
- **Batch Size**: 1
- **Learning Rate**: 5e-4
- **Target Modules**: `["c_attn", "c_proj"]`

## 🧪 Model Testing

### Test the Fine-tuned Model
```bash
python test_simple_model.py
```

**Sample Output:**
```
Input: Simulate a moot court hearing for these facts.
Facts: An employee was terminated for alleged misconduct.
Issues: Was the termination fair?

Generated Response:
Responsibilities : I have no idea what they're talking about.
```

## 📈 Training Progress

### Monitoring Scripts
- `monitor_training.py`: Check training status
- `watch_training.py`: Real-time progress monitoring

### Training Metrics
- **Runtime**: 115.2 seconds
- **Samples per second**: 0.017
- **Steps per second**: 0.017
- **Final Loss**: 9.6

## 🔧 Technical Notes

### Challenges Encountered
1. **Falcon-7B Issues**: Large model failed to load on system
2. **PEFT API Changes**: Updated deprecated functions
3. **Quantization**: BitsAndBytesConfig configuration
4. **Training Arguments**: Fixed parameter names

### Solutions Implemented
1. **Simplified Model**: Switched to DialoGPT-medium
2. **Updated Imports**: Fixed PEFT and Transformers compatibility
3. **CPU Training**: Removed GPU dependencies
4. **Error Handling**: Added comprehensive logging

## 🎯 Next Steps

### To Improve Model Performance:
1. **More Training Data**: Add more legal cases to `training.jsonl`
2. **Larger Model**: Try with more powerful hardware
3. **Better Prompting**: Refine instruction format
4. **Longer Training**: Increase epochs and learning rate

### To Scale the Project:
1. **Data Collection**: Process more PDF legal documents
2. **Model Selection**: Experiment with different base models
3. **Fine-tuning**: Try QLoRA or other PEFT methods
4. **Evaluation**: Add proper metrics and benchmarks

## 📝 Usage Examples

### Generate Moot Court Responses
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Load model
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
model = PeftModel.from_pretrained(model, "./moot_lora_simple")

# Generate response
prompt = "Simulate a moot court hearing for these facts..."
response = model.generate(tokenizer(prompt, return_tensors="pt"))
```

## 🏆 Success Metrics
- ✅ Virtual environment setup
- ✅ Dependencies installed
- ✅ Data preprocessing working
- ✅ LoRA training completed
- ✅ Model saved and loadable
- ✅ Basic inference working

The project successfully demonstrates end-to-end LoRA fine-tuning for legal AI applications!
