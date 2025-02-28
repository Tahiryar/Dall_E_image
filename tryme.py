import os
import openai
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Get API key
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

# Extract image URL
image_url = response['data'][0]['url']
print("Image URL:", image_url)

# Save the image
img_data = requests.get(image_url).content
with open("static/generated_image.png", "wb") as handler:
    handler.write(img_data)

print("Image saved as static/generated_image.png")
