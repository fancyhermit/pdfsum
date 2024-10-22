from pipeline.file_processor import process_pdfs_concurrently
from pipeline.mongo_db import MongoDBHandler
from config import DATASET_PATH

def main():
    # Load PDF URLs from the dataset.json file
    pdf_urls = process_pdfs_concurrently(DATASET_PATH)

    # Initialize MongoDB handler
    db_handler = MongoDBHandler()

    # Store metadata, summaries, and keywords in MongoDB
    for pdf_data in pdf_urls:
        db_handler.save_metadata(pdf_data)

    print("PDF processing complete.")

if __name__ == "__main__":
    main()
