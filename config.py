from dotenv import load_dotenv
import os

load_dotenv()

DATASET_PATH = os.path.join('data', 'dataset.json')

# MongoDB Atlas connection string using environment variables
MONGO_URI = f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@cluster0.mongodb.net/{os.getenv('MONGO_DB')}?retryWrites=true&w=majority"
DATABASE_NAME = os.getenv('MONGO_DB')
COLLECTION_NAME = "documents"
