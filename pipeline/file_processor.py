import os
import requests
import json
from PyPDF2 import PdfReader
from concurrent.futures import ProcessPoolExecutor
from config import DATASET_PATH

# Ensure the 'pdfs' directory exists
os.makedirs("pdfs", exist_ok=True)

# Function to load dataset JSON
def load_dataset(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Download and extract text from PDF
def download_and_read_pdf(pdf_url, file_name):
    try:
        response = requests.get(pdf_url, timeout=10, verify=False)
        pdf_path = os.path.join("pdfs", file_name)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

        # Extract text from PDF
        try:
            reader = PdfReader(pdf_path)
            text = ''.join([page.extract_text() for page in reader.pages])
            return text
        except Exception as e:
            print(f"Error reading PDF {file_name}: {e}")
            return None

    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")
        return None

# Define a function for processing each PDF
def process_pdf_data(pdf_data):
    url, file_name = pdf_data
    text = download_and_read_pdf(url, file_name)
    return {
        "file_name": file_name,
        "url": url,
        "text": text
    }

# Process PDF data concurrently
def process_pdfs_concurrently(dataset_path):
    dataset = load_dataset(dataset_path)
    pdf_urls = [(url, f"pdf_{i+1}.pdf") for i, (key, url) in enumerate(dataset.items())]

    # Concurrently process the PDFs using the new function
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_pdf_data, pdf_urls))

    return [res for res in results if res["text"]]

# Example main function to call the processing
def main():
    pdf_texts = process_pdfs_concurrently(DATASET_PATH)
    print(pdf_texts)

if __name__ == "__main__":
    main()
