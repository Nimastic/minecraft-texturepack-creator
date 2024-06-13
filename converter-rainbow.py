import os
from PIL import Image
import numpy as np

def rainbow_overlay(image):
    """
    Apply a rainbow overlay to an image, while keeping transparent pixels unchanged.
    """
    np_image = np.array(image)
    height, width, _ = np_image.shape
    rainbow = np.zeros_like(np_image)
    
    for i in range(height):
        ratio = i / float(height)
        r = int(255 * ratio)
        g = int(255 * (1 - ratio))
        b = 128  # Keep blue constant for a rainbow gradient
        rainbow[i, :, 0] = r
        rainbow[i, :, 1] = g
        rainbow[i, :, 2] = b
        rainbow[i, :, 3] = np_image[i, :, 3]  # Maintain original alpha channel
    
    blended = np_image * 0.5 + rainbow * 0.5
    blended = blended.astype(np.uint8)
    return Image.fromarray(blended)

def process_images_rainbow(input_dir, output_dir):
    """
    Process all PNG images in the input directory and save the rainbow overlay images to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)
        current_output_dir = os.path.join(output_dir, relative_path)
        
        if not os.path.exists(current_output_dir):
            os.makedirs(current_output_dir)
        
        for file_name in files:
            if file_name.endswith(".png"):
                input_path = os.path.join(root, file_name)
                output_path = os.path.join(current_output_dir, file_name)
                
                with Image.open(input_path) as img:
                    img = img.convert("RGBA")  # Ensure image is in RGBA mode
                    rainbow_img = rainbow_overlay(img)
                    rainbow_img.save(output_path)
                    print(f"Processed {file_name} with rainbow overlay")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images_rainbow(input_directory, output_directory)
