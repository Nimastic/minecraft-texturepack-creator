import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def earlybird_filter(image):
    """
    Apply an Earlybird-like filter to an image while maintaining transparency.
    """
    # Convert image to numpy array
    np_image = np.array(image)
    
    # Separate the alpha channel
    alpha_channel = np_image[:, :, 3]
    
    # Apply a warm color overlay to the RGB channels
    overlay = np.full_like(np_image[:, :, :3], [255, 194, 144])
    np_image[:, :, :3] = np.clip(np_image[:, :, :3] * 0.7 + overlay * 0.3, 0, 255).astype(np.uint8)
    
    # Convert back to image
    image = Image.fromarray(np_image, 'RGBA')
    
    # Apply vignette
    vignette = Image.new('L', (image.width, image.height), 0)
    for y in range(image.height):
        for x in range(image.width):
            vignette.putpixel((x, y), int(255 * (1 - ((x - image.width / 2) ** 2 + (y - image.height / 2) ** 2) ** 0.5 / max(image.width, image.height))))
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=10))
    
    # Blend vignette with the alpha channel
    alpha_channel = Image.fromarray(alpha_channel)
    alpha_channel = Image.composite(alpha_channel, vignette, vignette)
    
    # Enhance image
    image = ImageEnhance.Brightness(image).enhance(1.2)
    image = ImageEnhance.Contrast(image).enhance(1.1)
    
    # Combine enhanced image with the original alpha channel
    np_image = np.array(image)
    np_image[:, :, 3] = np.array(alpha_channel)
    
    return Image.fromarray(np_image, 'RGBA')

def process_images_earlybird(input_dir, output_dir):
    """
    Process all PNG images in the input directory and save the Earlybird-like filtered images to the output directory.
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
                    earlybird_img = earlybird_filter(img)
                    earlybird_img.save(output_path)
                    print(f"Processed {file_name} with Earlybird filter")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/texturess"

process_images_earlybird(input_directory, output_directory)
