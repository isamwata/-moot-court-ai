#!/usr/bin/env python3
"""
Setup script for Moot Court AI System
"""
import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def create_sample_data():
    """Create sample data files if they don't exist"""
    print("📄 Creating sample data files...")
    
    # Create sample training data if training.jsonl doesn't exist
    if not os.path.exists("training.jsonl"):
        sample_training = """{"instruction": "Simulate a moot court hearing (Claimant, Respondent, Judge) for these facts.", "input": "Facts: An employee was terminated for alleged misconduct.\\nIssues: Was the termination fair?", "output": "Claimant: The dismissal was procedurally unfair.\\nRespondent: The dismissal was justified.\\nJudge: The dismissal was substantively unfair."}"""
        with open("training.jsonl", "w") as f:
            f.write(sample_training)
        print("✅ Created sample training.jsonl")
    
    # Create sample case data if cases_sections.jsonl doesn't exist
    if not os.path.exists("cases_sections.jsonl"):
        sample_cases = """{"id": "sample_case", "text": "Sample legal precedent about employment law.", "source": "sample.pdf"}"""
        with open("cases_sections.jsonl", "w") as f:
            f.write(sample_cases)
        print("✅ Created sample cases_sections.jsonl")

def build_index():
    """Build FAISS index"""
    print("🔍 Building document index...")
    try:
        import index_cases
        print("✅ Document index built successfully")
    except Exception as e:
        print(f"⚠️  Could not build index: {e}")
        print("   Run 'python index_cases.py' manually after adding your data")

def main():
    print("🏛️ Setting up Moot Court AI System")
    print("=" * 50)
    
    install_requirements()
    create_sample_data()
    build_index()
    
    print("\n✅ Setup complete!")
    print("\n🚀 Next steps:")
    print("1. Add your legal PDFs and process them with data_preprocess.py")
    print("2. Train the model with: python train_lora_simple.py")
    print("3. Run the demo with: python demo_moot_court.py")

if __name__ == "__main__":
    main()
