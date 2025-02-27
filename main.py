from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict

import os

FILE = 'BIZEUL Camille_CNI.pdf'

def convert():
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    rendered = converter("./data/" + FILE)
    save_md(rendered)

def save_md(render):
    os.makedirs("output", exist_ok=True)
    filename = FILE.split(".pdf")[0]
    output_dir = os.path.join("output", filename)
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, filename + ".md"), "w") as f:
        f.write(render.markdown)
    
    img_dict = render.images
    for key, image in img_dict.items():
        image.save(os.path.join(output_dir, key))

if __name__ == "__main__":
    convert()