"""
Adapted from https://github.com/huggingface/diffusers/issues/2326 by https://github.com/ignacfetser

The LoRA trained using Diffusers are saved in .bin or .pkl format, which must be converted to be used in Automatic1111 WebUI.

This script converts .bin or .pkl files into .safetensors format, which can be used in WebUI.

Put this file in the same folder of .bin or .pkl file and run `python convert-to-safetensors.py --file checkpoint_file`  for diffusers <=v0.15.0 or >=v0.19.0  skip v0.16-v0.18
edit train_dreambooth_lora.py
 530 def main(args):
 531     logging_dir = Path(args.output_dir, args.logging_dir)
 532 
 533     accelerator_project_config = ProjectConfiguration(project_dir=args.output_dir, logging_dir=logging_dir)
 534
 535     accelerator = Accelerator(
         gradient_accumulation_steps=args.gradient_accumulation_steps,
         mixed_precision=args.mixed_precision,
         log_with=args.report_to,
         project_config=accelerator_project_config,
     )
 536
 537


"""
import re
import os
import argparse
import torch;
from safetensors.torch import save_file

def main(args):
    
    ## use GPU or CPU
    if torch.cuda.is_available():
        device = 'cuda'
        checkpoint = torch.load(args.file, map_location=torch.device('cuda'))
    else:
        device = 'cpu'
        # if on CPU or want to have maximum precision on GPU, use default full-precision setting
        checkpoint = torch.load(args.file, map_location=torch.device('cpu'))
    
    print(f'device is {device}')

    
    new_dict = dict()
    for idx, key in enumerate(checkpoint):
        new_key = re.sub('\.processor\.', '_', key)
        new_key = re.sub('mid_block\.', 'mid_block_', new_key)
        new_key = re.sub('_lora.up.', '.lora_up.', new_key)
        new_key = re.sub('_lora.down.', '.lora_down.', new_key)
        new_key = re.sub('\.(\d+)\.', '_\\1_', new_key)
        new_key = re.sub('to_out', 'to_out_0', new_key)
        new_key = 'lora_unet_' + new_key

        new_dict[new_key] = checkpoint[key]

    file_name = os.path.splitext(args.file)[0]  # get the file name without the extension
    new_lora_name = file_name + '_converted.safetensors'
    print("Saving " + new_lora_name)
    save_file(new_dict, new_lora_name)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        required=True,
        help="path to the full file name",
    )
    
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
