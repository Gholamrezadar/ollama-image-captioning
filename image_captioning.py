import os
import argparse
import ollama
from PIL import Image
from io import BytesIO
import base64

model_name = 'gemma3:4b'

# Shared captioning prompt
prompt = (
    "You are tasked with captioning this image in great detail. "
    "The caption should be about 1 paragraph long and should contain everything there is in the image. "
    "The generated caption is going to be used for image retrieval based on text matching so ideally we need very descriptive caption"
    "Also, the output of your message should only include the 1 paragraph that is going to be used as the caption of the image, so no talking, no thinking, no explaining your thought process, just one long and detailed paragraph about the image"
)

# Convert image to base64
def encode_image(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.convert("RGB").save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()

# Caption a single image
def caption_single_image(image_path):
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return

    print(f"\nProcessing: {image_path}")
    image_base64 = encode_image(image_path)

    response = ollama.chat(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt, "images": [image_base64]}
        ]
    )

    caption = response['message']['content']
    print(f"File: {image_path}")
    print(f"\nCaption:\n{caption}\n")
    print()
    return caption

# Caption all images in a folder
def caption_images_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            image_path = os.path.join(folder_path, filename)
            caption_single_image(image_path)

# Entry point
def main():
    global model_name
    parser = argparse.ArgumentParser(description="Caption images using Ollama and a multimodal model like Llava.")
    parser.add_argument('--image', type=str, help="Path to a single image to caption")
    parser.add_argument('--folder', type=str, help="Path to a folder of images to caption")
    parser.add_argument('--model', type=str, default=model_name, help="Ollama model to use (default: llava)")

    args = parser.parse_args()
    model_name = args.model

    if args.image:
        caption_single_image(args.image)
    elif args.folder:
        caption_images_in_folder(args.folder)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
