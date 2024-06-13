import os
import random
from PIL import Image
import numpy as np

def glitch_image(image, glitch_amount=0.1):
    """
    Apply a glitch effect to an image, while keeping transparent pixels unchanged.
    """
    np_image = np.array(image)
    height, width, channels = np_image.shape
    glitched_image = np_image.copy()
    
    for _ in range(int(height * glitch_amount)):
        row = random.randint(0, height - 1)
        shift = random.randint(-width // 5, width // 5)
        # Only shift the non-transparent pixels
        transparent_mask = np_image[row, :, 3] == 0
        glitched_image[row, ~transparent_mask] = np.roll(np_image[row, ~transparent_mask], shift, axis=0)
    
    return Image.fromarray(glitched_image)

def process_images_glitch(input_dir, output_dir, glitch_amount=0.1):
    """
    Process all PNG images in the input directory and save the glitched images to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        # Determine the corresponding output directory
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
                    glitched_img = glitch_image(img, glitch_amount)
                    glitched_img.save(output_path)
                    print(f"Processed {file_name} with glitch effect")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/glitched_textures"

process_images_glitch(input_directory, output_directory, glitch_amount=0.1)
