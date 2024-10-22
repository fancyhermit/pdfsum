from dotenv import load_dotenv
import os

load_dotenv()

DATASET_PATH = os.path.join('data', 'dataset.json')

# MongoDB Atlas connection string using environment variables
MONGO_URI= f"mongodb+srv://sahejyotbhatia:{os.getenv('MONGO_PASSWORD')}@cluster0.c5org.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "pdf_processing"
COLLECTION_NAME = "documents"
