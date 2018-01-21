from app import create_app
from flask import jsonify, request
import os
import cv2
from exceptions import InvalidUsage
import math
import base64
import operator
import random
import imageclassifier as imgc
import numpy as np

app = create_app("development")


@app.route('/')
def index():
    return 'Index Page'

@app.route('/status')
def hello_world():
    return "J'aime les singes"

@app.route("/processimg", methods=["POST"])
def process_img():
    r = request
    img_base64 = r.data['data'].split(",")[1]
    print(img_base64)
    img_data = base64.b64decode(img_base64)
    with open("image_from_ui.png", 'wb') as f:
        f.write(img_data)
    
    img_nb = imgc.classify_image()

    return str(img_nb)

@app.route("/processtestimg")
def process_testimg():
    img_nb = imgc.classify_image_test()

    return str(img_nb)

# Allow CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False)