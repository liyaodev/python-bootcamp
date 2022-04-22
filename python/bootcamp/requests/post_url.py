# -*- coding: utf-8 -*-

import base64
import requests
from urllib.parse import urlencode

img_path = "./demo.jpg"
with open(img_path,"rb") as f:
    image = f.read()
base64_image = base64.b64encode(image)

params = {
    "image_base64": base64_image
}

res = requests.post("<http-url>", 
    data=params, 
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
if res:
    print(res.json())
