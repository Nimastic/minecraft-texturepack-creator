import os
from PIL import Image
import numpy as np


def apply_sepia(image):
    """
    Apply a sepia tone to an image, while keeping transparent pixels unchanged.
    """
    np_image = np.array(image)
    tr = 0.393 * np_image[:, :, 0] + 0.769 * np_image[:, :, 1] + 0.189 * np_image[:, :, 2]
    tg = 0.349 * np_image[:, :, 0] + 0.686 * np_image[:, :, 1] + 0.168 * np_image[:, :, 2]
    tb = 0.272 * np_image[:, :, 0] + 0.534 * np_image[:, :, 1] + 0.131 * np_image[:, :, 2]
    
    sepia_image = np_image.copy()
    sepia_image[:, :, 0] = np.clip(tr, 0, 255)
    sepia_image[:, :, 1] = np.clip(tg, 0, 255)
    sepia_image[:, :, 2] = np.clip(tb, 0, 255)
    
    # Keep the alpha channel unchanged
    sepia_image[:, :, 3] = np_image[:, :, 3]
    
    return Image.fromarray(sepia_image.astype(np.uint8))

def process_images_sepia(input_dir, output_dir):
    """
    Process all PNG images in the input directory and save the sepia-toned images to the output directory.
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
                    sepia_img = apply_sepia(img)
                    sepia_img.save(output_path)
                    print(f"Processed {file_name} with sepia tone")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/sepia_textures"

process_images_sepia(input_directory, output_directory)
