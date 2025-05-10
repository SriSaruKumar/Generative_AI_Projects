import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import io

# Page settings
st.set_page_config(page_title="🖼️ Text-to-Image Generator", layout="centered")
st.title("🎨 Text-to-Image with Stable Diffusion")

# Input prompt
prompt = st.text_area("Enter a description for the image:", height=150)

# Generate button
generate = st.button("Generate Image")

# Cache model loading for performance
@st.cache_resource
def load_pipeline():
    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Load model with GPU support (FP16 if CUDA available)
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        revision="fp16" if torch.cuda.is_available() else None,
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

# If Generate is clicked
if generate:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        st.info("Generating image, please wait...")
        pipe = load_pipeline()
        
        # Inference
        with torch.autocast("cuda") if torch.cuda.is_available() else torch.no_grad():
            image = pipe(prompt).images[0]
        
        # Show image
        st.image(image, caption="Generated Image", use_column_width=True)

        # Download button
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button("Download Image", byte_im, "generated_image.png", "image/png")
