import os
from PIL import Image
import numpy as np

def invert_colors(image):
    """
    Invert the colors of an image, while keeping transparent pixels unchanged.
    """
    np_image = np.array(image)
    inverted_image = np_image.copy()
    inverted_image[:, :, :3] = 255 - np_image[:, :, :3]
    
    # Keep the alpha channel unchanged
    inverted_image[:, :, 3] = np_image[:, :, 3]
    
    return Image.fromarray(inverted_image)

def process_images_inversion(input_dir, output_dir):
    """
    Process all PNG images in the input directory and save the inverted images to the output directory.
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
                    inverted_img = invert_colors(img)
                    inverted_img.save(output_path)
                    print(f"Processed {file_name} with color inversion")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images_inversion(input_directory, output_directory)
