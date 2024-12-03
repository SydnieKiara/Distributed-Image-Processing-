from PIL import Image
import os

def process_grayscale(image_path, output_path):
    """
    Convert an image to grayscale and save it to the output path.
    """
    try:
        image = Image.open(image_path)
        grayscale_image = image.convert("L")  # Convert to grayscale (L mode)
        grayscale_image.save(output_path)
        print(f"Grayscale image saved to {output_path}")
    except Exception as e:
        print(f"Error processing grayscale image: {e}")

def handle_grayscale_task(task):
    """
    Handle grayscale task by calling the process_grayscale function.
    """
    image_name = task["image_name"]
    client_id = task["client_id"]
    input_image_path = os.path.join("images", image_name)  # Input image folder
    output_image_path = os.path.join("client_results", f"{client_id}_grayscale.jpg")

    # Process the image
    process_grayscale(input_image_path, output_image_path)
    return {"client_id": client_id, "status": "grayscale processed", "output": output_image_path}
