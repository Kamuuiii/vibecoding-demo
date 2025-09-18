import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

IMAGGA_API_KEY = os.getenv("IMAGGA_API_KEY")
IMAGGA_API_SECRET = os.getenv("IMAGGA_API_SECRET")

def fetch_colors_from_imagga(image_url):
    url = "https://api.imagga.com/v2/colors"
    # 認証情報をBase64でエンコード
    auth = base64.b64encode(f"{IMAGGA_API_KEY}:{IMAGGA_API_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}"
    }
    params = {"image_url": image_url}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print("Imagga API is working correctly.")
        return response.json()
    elif response.status_code == 401:
        print("Error: Unauthorized. Check your Imagga API Key and Secret.")
    else:
        print(f"Error fetching colors from Imagga: {response.status_code}, {response.text}")
    return None

# テスト用の画像URL
image_url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
fetch_colors_from_imagga(image_url)