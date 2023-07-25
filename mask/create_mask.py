from PIL import Image
from pixellib.torchbackend.instance import instanceSegmentation

import numpy as np

def invert_png(imgfile, out="output.png"):
    img = np.array(Image.open(imgfile).convert("RGBA"))
    mask = np.all(img == [0, 0, 0, 255], axis=-1)
    img[mask] = [255, 255, 255, 255]
    img[~mask] = [0, 0, 0, 255]
    Image.fromarray(img).save(out)

def segment_image(input_filename, output_filename, target_class):
    # Segment the image using instance segmentation
    ins = instanceSegmentation()
    ins.load_model("pointrend_resnet50.pkl")
    target_classes = ins.select_target_classes(**{target_class: True})
    results, output = ins.segmentImage(input_filename, show_bboxes=True, segment_target_classes=target_classes, output_image_name=output_filename)

    # Create a mask image for the target class
    image = Image.open(output_filename)
    width, height = image.size
    mask_image = np.zeros(image.size)
    for idx, mask in enumerate(results["masks"].transpose()):
        if results["class_names"][idx] == target_class:
            mask_image += mask
    mask_image = np.clip(mask_image, 0, 1).transpose() * 255
    mask_image = mask_image.astype(np.uint8)
    mask_image = Image.fromarray(mask_image).resize((width, height))

    # Save the mask image
    mask_image.save(output_filename)

# Segment the image and create a mask image for the "bottle" class
segment_image("44.jpg", "mask_image3.jpg", "bottle")
invert_png("mask_image3.jpg")
