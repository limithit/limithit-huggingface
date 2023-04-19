from diffusers import DiffusionPipeline
import torch
import uuid

model_id = "dehua"
pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompt = "liudehua person"

for i in range(10):
  filename = str(uuid.uuid4()) + ".png"
  image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
  image.save(filename)
