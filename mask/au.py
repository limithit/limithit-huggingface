import PIL
from PIL import Image
import requests
import torch
from io import BytesIO
import uuid

from diffusers import StableDiffusionInpaintPipeline

pipeline = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float16,
)
pipeline = pipeline.to("cuda")


init_image = Image.open("white.png")
init_image = init_image.convert("RGBA")
init_image = init_image.resize((512, 512))

mask_image = Image.open("white2.png")
mask_image = mask_image.convert("RGBA")
mask_image = mask_image.resize((512, 512))

prompt = "Face of a yellow cat, high resolution, sitting on a park bench"
for i in range(5):
  filename = str(uuid.uuid4()) + ".png"
  image = pipeline(prompt=prompt, image=init_image, mask_image=mask_image).images[0]
  image.save(filename)
