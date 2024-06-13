import os
from PIL import Image
import numpy as np

def posterize_image(image, bits=4):
    """
    Posterize an image by reducing the number of color bits,
    while keeping transparent pixels unchanged.
    """
    # Convert image to RGB and apply posterization
    rgb_image = image.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=2**bits).convert('RGBA')
    
    # Extract alpha channel from the original image
    alpha_channel = np.array(image)[:, :, 3]
    
    # Combine posterized RGB channels with the original alpha channel
    posterized_image = np.array(rgb_image)
    posterized_image[:, :, 3] = alpha_channel
    
    return Image.fromarray(posterized_image)

def process_images(input_dir, output_dir, bits=4):
    """
    Process all PNG images in the input directory and save the posterized images to the output directory.
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
                    posterized_img = posterize_image(img, bits)
                    posterized_img.save(output_path)
                    print(f"Processed {file_name} with posterize effect")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images(input_directory, output_directory, bits=4)
