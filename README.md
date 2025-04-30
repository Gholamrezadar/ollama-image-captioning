# Ollama Image Captioning

Captions images using Ollama and a multimodal model like Gemma3:4b.

## Usage

```bash
python image_captioning.py --image image.jpg
```

```bash
python image_captioning.py --folder images/
```

## Performance

**~3.5** seconds per image using Gemma3:4b on a Colab T4 GPU

## Prompt

```py
prompt = (
    "You are tasked with captioning this image in great detail. "
    "The caption should be about 1 paragraph long and should contain everything there is in the image. "
    "The generated caption is going to be used for image retrieval based on text matching so ideally we need very descriptive caption"
    "Also, the output of your message should only include the 1 paragraph that is going to be used as the caption of the image, so no talking, no thinking, no explaining your thought process, just one long and detailed paragraph about the image"
)

```

## Results

TODO
