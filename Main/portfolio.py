import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file=None):
        self.file = file
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if self.file is None:
            raise ValueError("No portfolio file provided.")
        
        # Load the CSV file from the uploaded file object
        self.data = pd.read_csv(self.file)

        # Add documents to the chroma collection if it doesn't already exist
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
