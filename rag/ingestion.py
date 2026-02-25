from langchain.document_loaders import PyPDFLoader

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()

def enrich_metadata(docs, source):
    for d in docs:
        d.metadata["source"] = source
        d.metadata["page"] = d.metadata.get("page", 0)
        d.metadata["section"] = "Unknown"
    return docs