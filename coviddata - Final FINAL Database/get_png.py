from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
import io
img = Image.new('RGB', (1080 , 1920))

def getpngstr(dict):
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 30)
    d.multiline_text((10,400), f"""
    • Patient name:   {dict[0]}\n\
    • Blood group:   {dict[1]}\n\
    • Age:   {dict[2]}\n\
    • Hospital name:   {dict[3]}\n\
    • City:   {dict[4]}\n\
    • Relationship with patient:   {dict[5]}\n\
    • Phone number:   {dict[6]}\n\
    • Requirements:   {dict[7]}\n\
    • spo2 level:   {dict[8]}\n""", font=font,spacing=75, fill=(255, 255, 0))
    data = io.BytesIO()  
    img.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return  encoded_img_data.decode("utf-8")


