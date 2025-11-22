import numpy as np
import cv2

def generate_heatmap(img_array):
    heatmap = cv2.applyColorMap(img_array, cv2.COLORMAP_JET)
    return heatmap
