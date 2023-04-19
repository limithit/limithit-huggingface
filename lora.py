import torch
import uuid
from diffusers import StableDiffusionPipeline

model_base = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(model_base, torch_dtype=torch.float16)
pipe.unet.load_attn_procs("dehua_to_saved_model")
pipe.to("cuda")

image = pipe(
    "A photo of liudehua man.",
    num_inference_steps=25,
    guidance_scale=7.5,
    cross_attention_kwargs={"scale": 0.5},
).images[0]

for i in range(10):
  filename = str(uuid.uuid4()) + ".png"
  image = pipe("A photo of liudehua man.", num_inference_steps=25, guidance_scale=7.5).images[0]
  image.save(filename)

