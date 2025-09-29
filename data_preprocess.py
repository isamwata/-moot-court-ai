# parse_judgments.py
import pdfplumber
import re
import json
from pathlib import Path

# heuristics: anchor words to split doc
FACT_KEYS = [r"\bFacts\b", r"\bBackground\b", r"\bIntroduction\b"]
CLAIMANT_KEYS = [r"\bClaimant\b", r"\bClaimant's case\b", r"\bClaimant’s Submissions\b"]
RESPONDENT_KEYS = [r"\bRespondent\b", r"\bRespondent's case\b", r"\bRespondent’s Submissions\b"]
ISSUE_KEYS = [r"\bIssues\b", r"\bIssue\b", r"\bWhat to determine\b"]
DECISION_KEYS = [r"\bJudgment\b", r"\bDecision\b", r"\bOrders\b", r"\bConclusion\b"]

def text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        pages = [p.extract_text() or "" for p in pdf.pages]
    return "\n".join(pages)

def first_match_pos(text, patterns):
    for pat in patterns:
        m = re.search(pat, text, flags=re.I)
        if m:
            return m.start()
    return None

def split_sections(text):
    # find anchors
    positions = {}
    positions['facts'] = first_match_pos(text, FACT_KEYS)
    positions['claimant'] = first_match_pos(text, CLAIMANT_KEYS)
    positions['respondent'] = first_match_pos(text, RESPONDENT_KEYS)
    positions['issues'] = first_match_pos(text, ISSUE_KEYS)
    positions['decision'] = first_match_pos(text, DECISION_KEYS)

    # build coarse segments by ordering found anchors
    anchors = [(k, pos) for k, pos in positions.items() if pos is not None]
    anchors.sort(key=lambda x: x[1])
    # append end
    anchors_positions = anchors + [("end", len(text))]
    sections = {}
    for i in range(len(anchors)):
        name, start = anchors_positions[i]
        _, end = anchors_positions[i+1]
        sections[name] = text[start:end].strip()
    # fallback -- if some anchors absent try heuristics
    if 'facts' not in sections:
        sections['facts'] = text[:anchors_positions[0][1] if anchors_positions else 1000].strip()
    for key in ['claimant','respondent','issues','decision']:
        sections.setdefault(key, "")
    # short clean-up: collapse whitespace
    for k,v in sections.items():
        sections[k] = re.sub(r"\s+", " ", v).strip()
    return sections

def make_training_sample(sections):
    facts = sections.get('facts','').strip()
    claimant = sections.get('claimant','').strip()
    respondent = sections.get('respondent','').strip()
    decision = sections.get('decision','').strip()
    # create an instruction-format sample
    instruction = "Simulate a moot court hearing (Claimant, Respondent, Judge) for these facts."
    input_text = f"Facts: {facts}\nIssues: {sections.get('issues','')}"
    # Create concise outputs: you might shorten claimant/respondent to the main submissions
    output_text = f"Claimant: {claimant}\nRespondent: {respondent}\nJudge: {decision}"
    return {"instruction": instruction, "input": input_text, "output": output_text}

def process_pdf_to_jsonl(pdf_path, out_path):
    text = text_from_pdf(pdf_path)
    sections = split_sections(text)
    sample = make_training_sample(sections)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(sample, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    import sys
    src_dir = Path(sys.argv[1] if len(sys.argv)>1 else "pdfs")
    out_file = Path(sys.argv[2] if len(sys.argv)>2 else "training.jsonl")
    samples = []
    for pdf in src_dir.glob("*.pdf"):
        try:
            text = text_from_pdf(pdf)
            sections = split_sections(text)
            sample = make_training_sample(sections)
            samples.append(sample)
        except Exception as e:
            print(f"ERROR parsing {pdf}: {e}")
    with open(out_file, "w", encoding="utf-8") as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"Wrote {len(samples)} samples to {out_file}")
