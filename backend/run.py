from app import create_app
from flask import jsonify, request
import os
import cv2
from exceptions import InvalidUsage
import math
import operator
import random
import imageclassifier as imgc

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
    numpy_array = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_value = imgc.classify_image(img)
    return str(img_value)

@app.route("/processtestimg")
def process_testimg():
    img_nb = imgc.classify_image_test()

    return str(img_nb)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False)