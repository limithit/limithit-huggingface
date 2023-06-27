from PIL import Image

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

transparent_white_png("example.png")
transparent_black_png("example.png")
transparent_white2_png("black.png")
