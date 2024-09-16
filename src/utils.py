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



if __name__ == "__main__":
    dot_text = """
digraph user_flow {

node[shape=box, style=filled, color=white];
        Azure_VNET1[label=<VNET1>, image="imgs\Virtual-Networks.svg"];
        On_Premises_DC_MumbaiHQ[label=<MumbaiHQ>];
        Expressroute_Tunnel_EXR1[label=<EXR1>, image="imgs\ExpressRoute-Circuits.svg"];
        VPN_Gateway_VNG1[label=<VNG1>, image="imgs\Virtual-Network-Gateways.svg"];
        Site_to_Site_VPN[label=<Site to Site VPN>];

        Azure_VNET1 -> Expressroute_Tunnel_EXR1[label=<Create Expressroute tunnel>];
        Expressroute_Tunnel_EXR1 -> On_Premises_DC_MumbaiHQ[label=<Connect to On premises DC>];
        Azure_VNET1 -> VPN_Gateway_VNG1[label=<Create VPN Gateway>];
        VPN_Gateway_VNG1 -> Site_to_Site_VPN[label=<Create Site to Site VPN>];
        Site_to_Site_VPN -> On_Premises_DC_MumbaiHQ[label=<Connect to On premises DC>];
}
"""
    import json
    print(json.dumps({"dot_file":dot_text}))

    generate_image(dot_text)    
