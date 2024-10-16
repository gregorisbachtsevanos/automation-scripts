from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    # Open the input image
    with open(input_path, 'rb') as input_file:
        input_image = input_file.read()

    # Remove the background
    output_image = remove(input_image)

    # Convert to a PIL image to save
    img = Image.open(io.BytesIO(output_image))

    # Save the output image
    img.save(output_path)

if __name__ == "__main__":
    # Example usage
    input_image_path = 'input_image.png'  # Path to your input image
    output_image_path = 'output_image.png'  # Path to save the output image without background

    remove_background(input_image_path, output_image_path)
    print(f"Background removed. Output saved to {output_image_path}.")
