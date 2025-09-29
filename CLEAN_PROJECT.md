# 🏛️ Moot Court AI System - Clean Project

## 📁 Essential Files Only

### 🤖 Core AI System
- `agents.py` - Multi-agent moot court system (Claimant, Respondent, Judge)
- `retriever.py` - Document retrieval with FAISS + Sentence Transformers
- `train_lora_simple.py` - LoRA fine-tuning script (working version)
- `demo_moot_court.py` - System demonstration

### 📚 Data & Models
- `courtcase.pdf` - Source legal document
- `training.jsonl` - Training dataset
- `cases_sections.jsonl` - Legal case sections for retrieval
- `case_index.faiss` - FAISS vector index
- `case_meta.jsonl` - Document metadata
- `moot_lora_simple/` - Trained LoRA model directory

### 🔧 Data Processing
- `data_preprocess.py` - PDF text extraction and structuring
- `index_cases.py` - Document indexing script

### 📖 Documentation
- `README.md` - Project documentation
- `SYSTEM_OVERVIEW.md` - Complete system overview

### 🐍 Environment
- `venv/` - Virtual environment with all dependencies

## 🚀 Quick Start

### 1. Activate Environment
```bash
cd /Users/isaiah/Documents/moot_court
source venv/bin/activate
```

### 2. Build Document Index
```bash
python index_cases.py
```

### 3. Train Model (if needed)
```bash
python train_lora_simple.py
```

### 4. Run Demo
```bash
python demo_moot_court.py
```

### 5. Run Full System
```bash
python agents.py
```

## 🗑️ Files Removed

The following unnecessary files were deleted:
- `monitor_training.py` - Training monitoring (no longer needed)
- `watch_training.py` - Real-time monitoring (no longer needed)
- `test_model.py` - Model testing (replaced by demo)
- `test_simple_model.py` - Simple model testing (replaced by demo)
- `train_lora.py` - Original Falcon-7B script (didn't work)
- `activate_env.sh` - Environment activation script (use `source venv/bin/activate`)
- `__pycache__/` - Python cache files

## ✅ Clean Project Benefits

1. **Focused**: Only essential files remain
2. **Functional**: All core components working
3. **Documented**: Clear documentation and examples
4. **Maintainable**: Easy to understand and modify
5. **Efficient**: No redundant or broken files

## 🎯 Core System Components

### Document Retrieval
- FAISS vector search
- Sentence Transformers embeddings
- Legal precedent ranking

### LoRA Fine-tuning
- DialoGPT-medium base model
- Parameter-efficient training
- Legal domain adaptation

### Multi-Agent System
- Claimant, Respondent, Judge agents
- Context-aware responses
- Legal argumentation simulation

The project is now clean, focused, and ready for production use or further development!
