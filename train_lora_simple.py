#!/usr/bin/env python3
"""
Simplified LoRA training script with a smaller model
"""
import json
import os
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model, TaskType

print("Starting simplified LoRA fine-tuning for moot court model...")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Use a smaller, more compatible model
BASE_MODEL = "microsoft/DialoGPT-medium"  # Much smaller model
JSONL_PATH = "training.jsonl"
OUTPUT_DIR = "./moot_lora_simple"

# 1. Load dataset
print(f"Loading dataset from {JSONL_PATH}...")
dataset = load_dataset("json", data_files=JSONL_PATH)["train"]
print(f"Dataset loaded with {len(dataset)} samples")

# build text pairs: instruction + input -> output
def build_prompt(example):
    instr = example.get("instruction","")
    inp = example.get("input","")
    out = example.get("output","")
    prompt = f"{instr}\n\n{inp}\n\n###\n\n{out}"
    return prompt

dataset = dataset.map(lambda x: {"text": build_prompt(x)}, remove_columns=dataset.column_names)

# 2. Tokenizer and model
print(f"Loading tokenizer from {BASE_MODEL}...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print(f"Loading model from {BASE_MODEL}...")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
print("Model loaded successfully!")

# 3. PEFT LoRA config
print("Setting up LoRA configuration...")
lora_config = LoraConfig(
    r=8,  # Smaller rank
    lora_alpha=16,
    target_modules=["c_attn", "c_proj"],  # GPT-2 style modules
    lora_dropout=0.1,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, lora_config)
print("LoRA model created successfully!")

# 4. Tokenize
print("Tokenizing dataset...")
def tok(ex):
    return tokenizer(ex["text"], truncation=True, max_length=512, padding=True)

tokenized = dataset.map(tok, batched=True, remove_columns=["text"])
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
print(f"Dataset tokenized with {len(tokenized)} samples")

# 5. Trainer
print("Setting up training arguments...")
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=2,
    learning_rate=5e-4,
    logging_steps=5,
    save_steps=25,
    warmup_steps=5,
    save_total_limit=2,
    eval_strategy="no",
    remove_unused_columns=False,
)

print("Creating trainer...")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    data_collator=data_collator,
)

print("Starting training...")
trainer.train()

print("Saving model...")
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"Saved LoRA-tuned model to {OUTPUT_DIR}")
