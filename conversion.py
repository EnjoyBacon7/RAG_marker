from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict


import os

def convert(file):
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    rendered = converter("./data/" + file)
    return rendered

def chunk_convert(data_path):
    cmd = f"marker '{data_path}' --output_dir ./output --converter_cls marker.converters.pdf.PdfConverter --workers 8"
    os.system(cmd)

def save_md(render, filename):
    os.makedirs("output", exist_ok=True)
    output_dir = os.path.join("output", filename)
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, filename + ".md"), "w") as f:
        f.write(render.markdown)
    
    img_dict = render.images
    for key, image in img_dict.items():
        image.save(os.path.join(output_dir, key))