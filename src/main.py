import gradio as gr
from dotenv import load_dotenv
from utils import get_system_prompt, generate_image
from core.generate_dot import generate_dot
import json

# Load environment variables from .env file
load_dotenv("../.env")

system_prompt = get_system_prompt()


def generate_dot_and_image(text, temperature, top_p):
    # Placeholder function to generate dot language text and image
    output = generate_dot(system_prompt, text, temperature, top_p)
    print(output)
    dot_text = json.loads(output)
    print(dot_text)
    dot_text = dot_text["dot_file"]
    image = generate_image(dot_text)  # Replace with actual image generation logic
    return dot_text, image


with gr.Blocks() as ui:
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                label="User Input",
                placeholder="Describe your network here...",
                lines=20,
            )
            temperature = gr.Slider(
                minimum=0, maximum=1, step=0.1, label="Temperature", value=0
            )
            top_p = gr.Slider(minimum=0, maximum=1, step=0.1, label="Max P", value=1.0)
        with gr.Column():
            dot_output = gr.Textbox(
                label="Dot Language Text",
                placeholder="Generated dot text will appear here...",
                lines=20,
                interactive=False,
            )
            image_output = gr.Image(label="Generated Image")

    generate_button = gr.Button("Generate")
    generate_button.click(
        generate_dot_and_image,
        inputs=[user_input, temperature, top_p],
        outputs=[dot_output, image_output],
    )

ui.launch()
