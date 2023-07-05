from PIL import Image
import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
import numpy as np

ins = instanceSegmentation()
ins.load_model("pointrend_resnet50.pkl")
target_classes = ins.select_target_classes(bottle=True)
results, output = ins.segmentImage(
  "44.jpg",
  show_bboxes=True,
  segment_target_classes=target_classes,
  output_image_name="mask_image1.jpg"
)

width, height = 3705, 5477
image=Image.open("mask_image1.jpg")
# Store the mask of dogs found by the pointrend model
mask_image = np.zeros(image.size)
for idx, mask in enumerate(results["masks"].transpose()):
  if results["class_names"][idx] == "bottle":
    mask_image += mask

# Create a mask image bigger than the original segmented image
#mask_image += np.roll(mask_image, 10, axis=[0, 0]) # Translate the mask 10 pixels to the left
#mask_image += np.roll(mask_image, -10, axis=[0, 0]) # Translate the mask 10 pixels to the right
#mask_image += np.roll(mask_image, 10, axis=[1, 1]) # Translate the mask 10 pixels to the bottom
#mask_image += np.roll(mask_image, -10, axis=[1, 1]) # Translate the mask 10 pixels to the top

# Set non black pixels to white pixels
mask_image = np.clip(mask_image, 0, 1).transpose() * 255
# Save the mask image
mask_image = Image.fromarray(np.uint8(mask_image)).resize((width, height))
mask_image.save("mask_image3.jpg")
