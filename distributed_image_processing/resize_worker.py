from PIL import Image
import os

def process_resize(image_path, output_path, dimensions):
    """
    Resize an image to the specified dimensions and save it to the output path.
    """
    try:
        image = Image.open(image_path)
        resized_image = image.resize(dimensions)
        resized_image.save(output_path)
        print(f"Resized image saved to {output_path}")
    except Exception as e:
        print(f"Error processing resize image: {e}")

def handle_resize_task(task):
    """
    Handle resize task by calling the process_resize function.
    """
    image_name = task["image_name"]
    client_id = task["client_id"]
    input_image_path = os.path.join("images", image_name)  # Input image folder
    output_image_path = os.path.join("client_results", f"{client_id}_resized.jpg")
    resize_dimensions = task["resize_dimensions"]

    # Process the image
    process_resize(input_image_path, output_image_path, resize_dimensions)
    return {"client_id": client_id, "status": "resize processed", "output": output_image_path}
