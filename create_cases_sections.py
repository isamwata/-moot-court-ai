#!/usr/bin/env python3
"""
Create cases_sections.jsonl from PDF files in cases directory
"""
import pdfplumber
import json
import re
from pathlib import Path

def extract_sections_from_pdf(pdf_path):
    """Extract different sections from a PDF"""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([p.extract_text() or "" for p in pdf.pages])
    
    # Extract case information
    case_info = {
        "id": Path(pdf_path).stem,
        "source": Path(pdf_path).name,
        "text": text[:2000] + "..." if len(text) > 2000 else text,  # Limit length
        "full_text": text
    }
    
    return case_info

def main():
    cases_dir = Path("cases")
    sections = []
    
    print("Processing PDF files in cases directory...")
    
    for pdf_file in cases_dir.glob("*.pdf"):
        print(f"Processing: {pdf_file.name}")
        try:
            case_info = extract_sections_from_pdf(pdf_file)
            sections.append(case_info)
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {e}")
    
    # Write to cases_sections.jsonl
    with open("cases_sections.jsonl", "w", encoding="utf-8") as f:
        for section in sections:
            f.write(json.dumps(section, ensure_ascii=False) + "\n")
    
    print(f"Created cases_sections.jsonl with {len(sections)} cases")

if __name__ == "__main__":
    main()
