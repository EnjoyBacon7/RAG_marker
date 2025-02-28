import db
import conversion
import llm

import os
import time

import logging

def main():
    chroma_client = db.init_db()
    try:
        collection = chroma_client.get_collection('documents')
    except:
        collection = chroma_client.create_collection('documents')

    logging.basicConfig(
        filename='log.log',
        filemode='w',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

    # Convert all files to markdown
    logging.info("Converting files to markdown")
    conversion.chunk_convert("data")
    logging.info("Finished converting files to markdown")

    # Store all documents in the database
    files = os.listdir("./output")
    for file in files:
        with open(os.path.join("./output", file, file + ".md"), "r") as f:
            text = f.read()
            db.store_document(text, collection)



if __name__ == "__main__":
    start = time.time()
    main()
    print("Execution time:", time.time() - start)