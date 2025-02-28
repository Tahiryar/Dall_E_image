import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file")
    exit()

# Initialize OpenAI API
openai.api_key = api_key

# Generate an image with DALL·E
response = openai.Image.create(
    prompt="A futuristic city with flying cars",
    n=1,
    size="1024x1024"
)

# Print response
print(response)
