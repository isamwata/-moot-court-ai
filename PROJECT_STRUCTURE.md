# 🏛️ Moot Court AI - Clean Project Structure

## 📁 **Essential Files Only**

### **🤖 Core AI System**
- `agents.py` - Multi-agent system (Claimant, Respondent, Judge)
- `case_arguer.py` - Case argumentation system for new cases
- `retriever.py` - Legal document retrieval system
- `demo_moot_court.py` - System demonstration script

### **🧠 Model & Training**
- `moot_lora_simple/` - Fine-tuned LoRA model directory
- `train_lora_simple.py` - LoRA fine-tuning script
- `training.jsonl` - Training data

### **📚 Data Processing**
- `data_preprocess.py` - PDF processing and training data creation
- `create_cases_sections.py` - Create sections from PDF cases
- `index_cases.py` - Build FAISS search index
- `cases_sections.jsonl` - Processed legal case sections
- `case_index.faiss` - FAISS search index
- `case_meta.jsonl` - Case metadata

### **📄 Legal Cases**
- `cases/` - Directory containing 6 PDF legal cases
  - `courtcase.pdf`
  - `case2.pdf`
  - `central-organisation-of-trade-unions-cotuk-5-others-v-cabinet-secretary-national-treasury-3-others-federation-of-kenya-employers-fke-interested-party-2021-eklr.pdf`
  - `commission-for-human-rights-justice-v-board-of-directors-kenya-ports-authority-2-others-dock-workers-union-intended-interested-party-2020-eklr.pdf`
  - `dock-workers-union-v-kenya-ports-authority-2018-eklr.pdf`
  - `william-odhiambo-ramogi-3-others-v-attorney-general-6-others-muslims-for-human-rights-2-others-interested-parties-2020-eklr.pdf`

### **📖 Documentation**
- `README.md` - Project overview and setup
- `SYSTEM_OVERVIEW.md` - Comprehensive system documentation
- `PROJECT_STRUCTURE.md` - This file

### **⚙️ Configuration**
- `requirements.txt` - Python dependencies
- `setup.py` - Project setup script
- `venv/` - Virtual environment (excluded from git)

## 🚀 **Quick Start**

```bash
# Activate virtual environment
source venv/bin/activate

# Run system demo
python demo_moot_court.py

# Argue a new case
python case_arguer.py

# Process new cases
python create_cases_sections.py
python index_cases.py
```

## 🎯 **System Capabilities**

1. **📚 Legal Document Processing**: Extract and index legal cases
2. **🧠 AI Model Training**: Fine-tune language models with LoRA
3. **🔍 Document Retrieval**: Find relevant legal precedents
4. **🎭 Multi-Agent System**: Claimant, Respondent, Judge interactions
5. **⚖️ Case Argumentation**: Generate legal arguments for new cases

## 📊 **Project Statistics**

- **Total Files**: ~20 essential files
- **Legal Cases**: 6 PDF documents
- **AI Model**: Fine-tuned LoRA model
- **Search Index**: FAISS vector database
- **Dependencies**: 10+ Python packages

**Clean, focused, and ready for production use!**
