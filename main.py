from PIL import Image
import os


def optimize_images(folder, height):
    logo = Image.open('logo.png')

    try:
        os.mkdir(f"{folder}\\optimized")
    except:
        print("Toks katalogas jau yra")
    files = os.listdir(folder)
    for file in files:
        if file.endswith((".jpg", '.png')):
            pic = Image.open(f"{folder}\\{file}")
            pic = pic.resize((round(pic.size[0] / pic.size[1] * height), height))
            pic.paste(logo, (pic.size[0] - logo.size[0], pic.size[1] - logo.size[1], pic.size[0], pic.size[1]), logo)
            pic.save(f"{folder}\\optimized\\{file}")


optimize_images(r"Your directory", 800)