import os
import shutil

def replace_png_files(input_dir, output_dir):
    # Ensure the input and output directories exist
    if not os.path.isdir(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return
    
    if not os.path.isdir(output_dir):
        print(f"Output directory '{output_dir}' does not exist.")
        return

    # Walk through the input directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.png'):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, relative_path)

                # Check if the file exists in the output directory
                if os.path.exists(output_file_path):
                    # Replace the file
                    print(f"Replacing {output_file_path} with {input_file_path}")
                    shutil.copy2(input_file_path, output_file_path)

# Example usage
input_directory = 'C:/Users/jerie/OneDrive/Desktop/upscaled_enhanced_textures'
output_directory = 'C:/Users/jerie/OneDrive/Desktop/assets/minecraft/textures'

replace_png_files(input_directory, output_directory)
