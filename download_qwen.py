from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2-1.5B-Instruct"  # 或上面列的其他开放ID
save_path = "./models/qwen2-1_5b"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.save_pretrained(save_path)

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
model.save_pretrained(save_path)
print(f"模型已下载到 {save_path}")