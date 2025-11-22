import numpy as np
import cv2
from PIL import Image

def preprocess_image(file):
    img = Image.open(file)
    img = img.convert("L")  # grayscale
    img = img.resize((256, 256))
    img_array = np.array(img)
    return img_array
