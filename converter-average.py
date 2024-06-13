import os
from PIL import Image
import numpy as np

def calculate_average_color(image):
    """
    Calculate the average color of an image.
    """
    np_image = np.array(image)
    avg_color = np.mean(np_image, axis=(0, 1)).astype(int)
    
    if np_image.ndim == 2:  # Grayscale image
        avg_color = np.tile(avg_color, 3)  # Repeat grayscale value across RGB channels
        return tuple(avg_color)
    elif np_image.shape[2] == 4:  # RGBA image
        return tuple(avg_color[:4])
    else:  # RGB image
        return tuple(avg_color[:3])

def create_average_color_image(size, avg_color):
    """
    Create an image of the specified size filled with the average color.
    """
    mode = "RGBA" if len(avg_color) == 4 else "RGB"
    return Image.new(mode, size, avg_color)

def process_images(input_dir, output_dir):
    """
    Process all PNG images in the input directory and save the new images to the output directory.
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
                    avg_color = calculate_average_color(img)
                    new_img = create_average_color_image(img.size, avg_color)
                    new_img.save(output_path)
                    print(f"Processed {file_name} - Average Color: {avg_color}")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images(input_directory, output_directory)
