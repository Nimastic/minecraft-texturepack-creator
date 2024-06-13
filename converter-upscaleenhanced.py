import os
from PIL import Image, ImageEnhance, ImageFilter

def upscale_image(image, scale_factor):
    """
    Upscale an image by a given scale factor using high-quality resampling.
    """
    new_width = image.width * scale_factor
    new_height = image.height * scale_factor
    return image.resize((new_width, new_height), Image.LANCZOS)

def enhance_image(image):
    """
    Enhance the image by sharpening and increasing contrast.
    """
    # Apply sharpening
    image = image.filter(ImageFilter.SHARPEN)
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)  # Adjust this value as needed
    
    # Optional: Apply Unsharp Mask
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    return image

def process_images(input_dir, output_dir, scale_factor):
    """
    Process all PNG images in the input directory, upscale them, enhance, and save to the output directory.
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
                    upscaled_img = upscale_image(img, scale_factor)
                    enhanced_img = enhance_image(upscaled_img)
                    enhanced_img.save(output_path)
                    print(f"Processed {file_name} with upscaling and enhancement")

input_directory = "C:/Users/jerie/OneDrive/Desktop/textures"
output_directory = "C:/Users/jerie/OneDrive/Desktop/upscaled_enhanced_textures"
scale_factor = 2  # Change this to the desired scale factor (e.g., 2 for doubling the resolution)

process_images(input_directory, output_directory, scale_factor)
