import cv2
import os

def process_edge_detection(image_path, output_path):
    """
    Apply edge detection to an image and save it to the output path.
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        edges = cv2.Canny(image, 100, 200)  # Apply Canny edge detection
        cv2.imwrite(output_path, edges)
        print(f"Edge detected image saved to {output_path}")
    except Exception as e:
        print(f"Error processing edge detection image: {e}")

def handle_edge_detection_task(task):
    """
    Handle edge detection task by calling the process_edge_detection function.
    """
    image_name = task["image_name"]
    client_id = task["client_id"]
    input_image_path = os.path.join("images", image_name)  # Input image folder
    output_image_path = os.path.join("client_results", f"{client_id}_edges.jpg")

    # Process the image
    process_edge_detection(input_image_path, output_image_path)
    return {"client_id": client_id, "status": "edge detection processed", "output": output_image_path}
