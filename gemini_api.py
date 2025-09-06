import json
from google import genai

with open("creds.json", "r") as akh:
    access_info = json.load(akh)

client = genai.Client(api_key=access_info["API_AI"]["API_KEY"])
response = client.models.generate_content(
    model=access_info["API_AI"]["MODEL"],
    contents="Testing the connection"
)

"""

"""


