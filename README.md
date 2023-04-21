# limithit-huggingface 
ref (https://huggingface.co/docs/diffusers/v0.15.0/en/training/dreambooth)

# example 
```
 export MODEL_NAME="runwayml/stable-diffusion-v1-5"
 export INSTANCE_DIR="/root/img"
 export OUTPUT_DIR="img"
 export CLASS_DIR="img_path_to_class_images"

accelerate launch train_dreambooth.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --output_dir=$OUTPUT_DIR \
  --with_prior_preservation --prior_loss_weight=1.0 \
  --class_data_dir=$CLASS_DIR \
  --instance_prompt="a photo of mine makeup" \
  --class_prompt="a photo of makeup" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=5e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=200 \
  --max_train_steps=800

```

```
export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export INSTANCE_DIR="/root/img"
export CLASS_DIR="lora_img_to_class_images"
export OUTPUT_DIR="lora_ppmt_to_saved_model"

accelerate launch train_dreambooth_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --output_dir=$OUTPUT_DIR \
  --instance_prompt="a photo of mine" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --checkpointing_steps=100 \
  --learning_rate=1e-4 \
  --report_to="wandb" \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=1000 \
  --validation_prompt="A photo of mine" \
  --validation_epochs=50 \
  --seed="0" 

```
