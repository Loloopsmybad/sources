from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM

model_path = r"D:\samsung\New Volume (NTFS)\sources\a4c\ai\openvino_model"

model = OVModelForCausalLM.from_pretrained(model_path)
from optimum.intel import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline

model_id = "ov_TinyLlama_v1_1"
model = OVModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
results = pipe("Hey, how are you doing today?", max_new_tokens=100)