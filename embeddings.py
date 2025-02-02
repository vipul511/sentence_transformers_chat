import os
from sentence_transformers import SentenceTransformer
def read_text_files(directory, extensions=[".md", ".py", ".txt"]):
    """Read and return all text from files with given extensions."""
    text_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    text_data.append(f.read())
    return text_data

repo_texts = read_text_files("repo")
print(f"✅ Extracted {len(repo_texts)} documents from repo.")

import faiss
import numpy as np

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert repo documents to embeddings
doc_embeddings = model.encode(repo_texts)

# Store embeddings in FAISS
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))

print("✅ Repository content embedded successfully!")

def search_repo(query):
    """Search GitHub repo using semantic search."""
    query_embedding = model.encode([query])  # Convert query to vector
    _, idx = index.search(np.array(query_embedding), k=2)  # Retrieve top 2 results

    results = []
    for i in idx[0]:
        results.append(repo_texts[i])
    return results

import streamlit as st

st.title("🤖 GitHub Q&A System")

query = st.text_input("Ask a question about the GitHub repo:")
if query:
    results = search_repo(query)
    st.subheader("🔎 Most Relevant Answers:")
    for i, result in enumerate(results):
        st.write(f"✅ **Result {i+1}:**")
        st.write(result[:10000] + "...")  # Display first 500 characters
