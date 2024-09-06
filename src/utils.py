from pathlib import Path
import graphviz


def get_system_prompt():
    system_prompt_file = Path(__file__).parent / "prompts" / "system_prompt.txt"
    with open(system_prompt_file, "r") as f:
        system_prompt = f.read()
        return system_prompt


def generate_image(dot_text):
    # Placeholder function to generate image from dot language text
    dot = graphviz.Source(dot_text)
    # Render the DOT code to an image file

    # Save the image to a file
    output_path = "output"

    print(dot.render(output_path, format="png", cleanup=True))
    # Return the path to the generated image
    return output_path + ".png"
