# agents.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from retriever import retrieve

MODEL_DIR = "./moot_lora_simple"  # path to LoRA + base adapter or to base model with adapters applied
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR, device_map="auto", torch_dtype=torch.float16)
# If you saved just LoRA adapters, load them with peft.get_peft_model - omitted here for brevity.

def make_context(facts, top_k=4):
    docs = retrieve(facts, top_k=top_k)
    ctx = "\n".join([f"[{d.get('source','unknown')}] {d.get('text','')}" for d in docs])
    return ctx

# role prompts
SYSTEM_TEMPLATES = {
    "claimant": "You are the Claimant's counsel in a moot court. Produce a clear legal submission arguing that dismissal was unfair. Support your submission by reference to the provided precedents where relevant. Keep to < 600 words.",
    "respondent": "You are the Respondent's counsel. Provide a rebuttal to the Claimant's points. Use the precedents to support the defense of the employer. Keep it focused and professional.",
    "judge": "You are the Judge. Given the facts and arguments, analyze procedurally and substantively, evaluate the cited precedents and give a reasoned judgment, list orders and monetary award if any."
}

def generate(prompt, max_new_tokens=512):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False, temperature=0.0)
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    # strip off the prompt part (simple heuristic)
    return text[len(prompt):].strip()

def run_moot(facts):
    ctx = make_context(facts, top_k=4)
    # 1. Claimant
    claim_prompt = SYSTEM_TEMPLATES["claimant"] + "\n\nContext:\n" + ctx + "\n\nFacts:\n" + facts + "\n\nClaimant Submission:\n"
    claimant_submission = generate(claim_prompt)
    print("=== Claimant ===\n", claimant_submission)

    # 2. Respondent
    resp_prompt = SYSTEM_TEMPLATES["respondent"] + "\n\nContext:\n" + ctx + "\n\nFacts:\n" + facts + "\n\nClaimant said:\n" + claimant_submission + "\n\nRespondent Submission:\n"
    respondent_submission = generate(resp_prompt)
    print("=== Respondent ===\n", respondent_submission)

    # 3. Judge
    judge_prompt = SYSTEM_TEMPLATES["judge"] + "\n\nContext:\n" + ctx + "\n\nFacts:\n" + facts + "\n\nClaimant:\n" + claimant_submission + "\n\nRespondent:\n" + respondent_submission + "\n\nJudgment:\n"
    judgment = generate(judge_prompt, max_new_tokens=1024)
    print("=== Judge ===\n", judgment)
    return claimant_submission, respondent_submission, judgment

if __name__ == "__main__":
    sample_facts = "The claimant was a procurement officer dismissed after alleged overstatement of procurement costs totalling Ksh 825,700. After the hearing, a follow-up letter said the correct figure was Ksh 442,600. Claimant says dismissal was unfair, procedural and substantive issues."
    run_moot(sample_facts)
