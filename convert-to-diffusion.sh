#!/bin/sh

# train_dreambooth.py
python ../../scripts/convert_diffusers_to_original_stable_diffusion.py \
--model_path path_to_saved_model/  \
--checkpoint_path  ppmt.safetensors \
--use_safetensors


# for train_dreambooth_lora.py
python lora-diffusers-diffusion-convert-to-safetensors.py --file lora_to_saved_model/pytorch_lora_weights.bin
