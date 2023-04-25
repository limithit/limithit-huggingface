下载预训练模型并转化成diffusers格式。
```
 pip install safetensors
 cd stable-diffusion-webui/models/Stable-diffusion && wget -c https://huggingface.co/naonovn/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors -O chilloutmix_NiPrunedFp32Fix.safetensors
 python diffusers/scripts/convert_original_stable_diffusion_to_diffusers.py \
--checkpoint_path=stable-diffusion-webui/models/Stable-diffusion/chilloutmix_NiPrunedFp32Fix.safetensors \
--dump_path=chilloutmix-ni --from_safetensors
```
模型训练。设置num_train_epochs为200，进行lora模型的训练。MODEL_NAME 修改为你本地路径即可，`export MODEL_NAME="/path/../model/chilloutmix-ni"`
或者与scripts同一目录`export MODEL_NAME="chilloutmix-ni"`

```
export MODEL_NAME="chilloutmix-ni" && \
export DATASET_NAME="cloth_train_example" && \
accelerate launch --mixed_precision="fp16" train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME --caption_column="text" \
  --width=640 --height=768 --random_flip \
  --train_batch_size=1 \
  --num_train_epochs=200 --checkpointing_steps=5000 \
  --learning_rate=1e-04 --lr_scheduler="constant" --lr_warmup_steps=0 \
  --seed=42 \
  --output_dir="cloth-model-lora" \
  --validation_prompt="cloth1" --validation_epochs=100
  ```
  
  将lora模型转化成WebUI支持格式并拷贝到WebUI所在目录。
  ```

 python lora-diffusers-diffusion-convert-to-safetensors.py --file='cloth-model-lora/pytorch_lora_weights.bin'
 mkdir stable-diffusion-webui/models/Lora
 cp cloth-model-lora/pytorch_lora_weights_converted.safetensors stable-diffusion-webui/models/Lora/cloth_lora_weights.safetensors
  ```
  # 有两种加载lora权重的方法，如图所示，权重放置的路径不同
  ![image](https://user-images.githubusercontent.com/7675726/234150424-b051563b-146e-43fc-872d-c37968a377c1.png)
  
  ![image](https://user-images.githubusercontent.com/7675726/234150494-ecca695a-380c-44b8-bbb0-f5035544f217.png)
```
cp cloth-model-lora/pytorch_lora_weights_converted.safetensors \
stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora
```
