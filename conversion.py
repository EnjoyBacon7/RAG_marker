from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser


import os

def convert(file):

    config = {
        
    }
    config_parser = ConfigParser(config)

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
        config=config_parser.generate_config_dict(),
        processor_list=config_parser.get_processors(),
        renderer=config_parser.get_renderer(),
        llm_service=config_parser.get_llm_service()
    )

    rendered = converter(file)
    return rendered

def chunk_convert(data_path):
    cmd = f"marker '{data_path}' --output_dir ./output --converter_cls marker.converters.pdf.PdfConverter --workers 2"
    os.system(cmd)

def chunk_convert_homemade(data_path):

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".pdf"):
                rendered = converter(os.path.join(root, file))
                save_md(rendered, file)

def save_md(render, filename):
    os.makedirs("output", exist_ok=True)
    output_dir = os.path.join("output", filename)
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, filename + ".md"), "w") as f:
        f.write(render.markdown)
    
    img_dict = render.images
    for key, image in img_dict.items():
        image.save(os.path.join(output_dir, key))