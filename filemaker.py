
## 裏表割り振りができているか点検するために、大量に画像を作成するPythonスクリプトです。

import os
import sys
import shutil
import subprocess
from PIL import Image, ImageFilter , ImageDraw , ImageFont



def make_image(screen, bgcolor, filename):
    """
    画像の作成
    """
    num = os.path.splitext(os.path.basename(filename))[0] 
    print(num)
    num = int(num)
    if num%2 == 1:
      label = str(int((num+1)/2)) +"_omote"
    else:
      label = str(int(num/2)) +"_ura"

    img = Image.new('RGB', screen,bgcolor)
    draw = ImageDraw.Draw(img)# im上のImageDrawインスタンスを作る
    font = ImageFont.truetype("Arial.ttf", 32)
    draw.text((30,30),label , font = font)
    img.save(filename)
    return


if os.path.isdir("./test"):
  shutil.rmtree("./test")

os.makedirs("./test", exist_ok=True)

for i  in range(1,101):
  print(i)
  make_image((300,300), "red", "./test/" + str(i).zfill(4) + ".jpg")