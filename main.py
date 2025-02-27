import os

import db
import conversion
import llm



# with open("output/DTA-2004_/DTA-2004_.md") as f:
#     md = f.read()

#     db.store_document(md)

#     answer = db.query("Quelle est l'addresse du DTA?")
#     assistant = llm.query_llm(answer, "Quelle est l'addresse du DTA?")
#     print(assistant)


render = conversion.convert("2024-07_rapport-propositions-pour-2025_assurance-maladie.pdf")
conversion.save_md(render, "2024-07_rapport-propositions-pour-2025_assurance-maladie")