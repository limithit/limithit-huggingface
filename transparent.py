from PIL import Image, ImageOps

def transparent_white_png(imgfile, out="white"):
    img = Image.open(imgfile)
    img = img.convert("RGBA")
    W, H = img.size
    white_pixel = (255, 255, 255, 255)
    for h in range(W):
        for w in range(H):
            if img.getpixel((h, w))[3] == 0:
                img.putpixel((h, w), white_pixel)
    img.save(out + ".png")


def transparent_black_png(imgfile, out="black"):
    img = Image.open(imgfile)
    img = img.convert("RGBA")
    W, H = img.size
    black_pixel = (0, 0, 0, 255)
    for h in range(W):
        for w in range(H):
            if img.getpixel((h, w))[3] != 0:
                img.putpixel((h, w), black_pixel)
    img.save(out + ".png")



def transparent_white2_png(imgfile, out="white2"):
    img = Image.open(imgfile)
    img = img.convert("RGBA")
    W, H = img.size
    white_pixel = (255, 255, 255, 255)
    for h in range(W):
        for w in range(H):
            if img.getpixel((h, w))[3] == 0:
                img.putpixel((h, w), white_pixel)
    img.save(out + ".png")

def set_transparent_area_to_white(image_path, output_path):
    with Image.open(image_path) as image:
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        alpha = image.split()[-1]
        bg_mask = alpha.point(lambda x: 255 - x)
        bg = Image.new("RGBA", image.size, (0, 0, 0, 255))
        bg.paste(image, mask=bg_mask)
        new_image = bg.convert("RGB")
        new_image = ImageOps.expand(new_image,border=512,fill='white')
        new_image.save(output_path)

transparent_white_png("example.png")
transparent_black_png("example.png")
transparent_white2_png("black.png")
# set_transparent_area_to_white("black.png", "output.png")
