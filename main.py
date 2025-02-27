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

    logging.basicConfig(level=logging.INFO)

    # Convert all files to markdown
    conversion.chunk_convert("data")

    # Store all documents in the database
    files = os.listdir("./output")
    for file in files:
        with open(os.path.join("./output", file, file + ".md"), "r") as f:
            text = f.read()
            db.store_document(text, collection)

    # # Query the database
    # query = "What is the purpose of the document?"
    # results = db.query(query, collection)
    # print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    print("Execution time:", time.time() - start)