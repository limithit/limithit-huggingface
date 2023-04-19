#!/bin/sh

python ../../scripts/convert_diffusers_to_original_stable_diffusion.py \
--model_path path_to_saved_model/  \
--checkpoint_path  ppmt.safetensors \
--use_safetensors
