import PIL
print(PIL.__version__)

from PIL import Image, ImageDraw, ImageFont

width, height = 400, 400
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)
draw.rectangle([(50, 50), (350, 350)], outline='black', width=5)
draw.ellipse([(150, 150), (250, 250)], fill='blue', outline='black')
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

draw.text((100, 100), "Hello!", font=font, fill="black")
image.save('generated_image.png')
image.show()
