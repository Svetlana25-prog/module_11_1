from PIL import Image, ImageDraw, ImageFont

image = Image.open('img.png').convert('RGBA')

txt = Image.new('RGBA', image.size, (255,255,255,0))
draw = ImageDraw.Draw(txt)

draw.text((50, 50), 'Hello URBAN',font=None,fill=(255,255,255,128),font_size=144)
w = Image.alpha_composite(image, txt)
w.save('new.png')
w.show()