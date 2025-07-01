import os
from dotenv import load_dotenv
from app.riteriver import read_pdf

# Load environment variables
load_dotenv()

# Set environment variables for LangChain integrations
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGSMITH_PROJECT"] = "default"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY", "")

def main():
    print("🚀 Hello from Rashmeet!")
    read_pdf()

if __name__ == "__main__":
    main()
