import os
from PIL import Image
import numpy as np

def calculate_average_color(image_block):
    """
    Calculate the average color of an image block, excluding transparent pixels.
    """
    np_block = np.array(image_block)
    if np_block.shape[2] == 4:  # RGBA image
        alpha_channel = np_block[:, :, 3]
        mask = alpha_channel > 0
        if np.any(mask):
            avg_color = np.mean(np_block[mask], axis=0).astype(int)
        else:
            avg_color = np.array([0, 0, 0, 0])
    else:  # RGB image
        avg_color = np.mean(np_block, axis=(0, 1)).astype(int)
    
    return tuple(avg_color)

def reduce_resolution(image, block_size):
    """
    Reduce the resolution of an image by averaging blocks of pixels.
    """
    np_image = np.array(image)
    height, width, channels = np_image.shape
    
    # Calculate padding needed
    pad_height = (block_size - (height % block_size)) % block_size
    pad_width = (block_size - (width % block_size)) % block_size
    
    # Pad the image
    if pad_height > 0 or pad_width > 0:
        np_image = np.pad(np_image, ((0, pad_height), (0, pad_width), (0, 0)), mode='constant', constant_values=0)
    
    new_height = (height + pad_height) // block_size
    new_width = (width + pad_width) // block_size
    
    new_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)
    
    for y in range(new_height):
        for x in range(new_width):
            block = np_image[y*block_size:(y+1)*block_size, x*block_size:(x+1)*block_size]
            avg_color = calculate_average_color(block)
            new_image[y, x] = avg_color
    
    # Rescale the new image back to the original size
    new_image = Image.fromarray(new_image).resize((width, height), Image.NEAREST)
    
    # Apply transparency mask
    original_pixels = np.array(image)
    new_pixels = np.array(new_image)
    mask = original_pixels[:, :, 3] == 0
    new_pixels[mask] = original_pixels[mask]
    
    return Image.fromarray(new_pixels)

def process_images(input_dir, output_dir, block_size=8):
    """
    Process all PNG images in the input directory and save the reduced resolution images to the output directory.
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
                    reduced_img = reduce_resolution(img, block_size)
                    reduced_img.save(output_path)
                    print(f"Processed {file_name} with reduced resolution")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images(input_directory, output_directory, block_size=8)
