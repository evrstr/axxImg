#!/usr/bin/env python    
# -*- coding: utf-8 -*-  

from PIL import Image, ImageDraw, ImageFont
import random
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import os

def test():
    print(os.listdir())
    img = Image.open("./dest.png")
    print(img.info)
    text = "御驾亲征"

    # 字体
    font = ImageFont.truetype("Shouxieti.ttf", 75)
    # 将图片转为图层
    layer = img.convert("RGBA")
    #生成对应图片
    text_layer = Image.new("RGBA", (img.size[0]*2,img.size[1]*2), (255, 255, 255, 0))
    Image_draw = ImageDraw.Draw(text_layer) #画图
    #获取文本大小
    textsize_x, textsize_y = Image_draw.textsize(text, font=font)
    nums = max(round(layer.size[0] / textsize_x), round(layer.size[1] / textsize_y))
    print(nums)
    for i in range (1,nums):
        for j in range(1,nums):
            #设置文本文字位置
            text_xy = (textsize_x*(i-1)*1.5,textsize_y*(j-1)*2.5)
        # 设置文本颜色和透明度位置
            Image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, random.randint(5,50)))
    # 将新图层旋转45度后裁剪和图片一样大，新图层必须和图片一样大，否则无法合并
    text_layer = text_layer.rotate(45)
    text_layer = text_layer.crop((text_layer.size[0]/2 - img.size[0]/2, text_layer.size[1]/2 - img.size[1]/2, text_layer.size[0]/2 + img.size[0]/2, text_layer.size[1]/2 + img.size[1]/2))

    # 合并图层
    after = Image.alpha_composite(layer, text_layer)
    return after
    after.save("output.png")


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    img = test()
    self.send_response(200)
    self.send_header('Content-type', 'application/x-www-form-urlencoded')
    self.end_headers()
    # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(img)
    return

