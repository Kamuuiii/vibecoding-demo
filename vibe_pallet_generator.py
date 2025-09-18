import os
import requests
import base64
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_image_from_unsplash(keyword):
    url = f"https://api.unsplash.com/photos/random?query={keyword}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['urls']['regular']  # 画像URLを返す
    else:
        print("Error fetching image from Unsplash:", response.status_code)
        return None

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
    
def generate_vibe_palette(keyword):
    print(f"Fetching image for keyword: {keyword}")
    image_url = fetch_image_from_unsplash(keyword)
    if image_url:
        print(f"Image URL: {image_url}")
        print("Fetching color palette...")
        colors = fetch_colors_from_imagga(image_url)
        if colors and 'result' in colors and 'colors' in colors['result']:
            print("Generated Color Palette:")
            for color in colors['result']['colors']['image_colors']:
                print(f"HEX: {color['html_code']}, RGB: {color['closest_palette_color']}")
        else:
            print("Error: Unexpected response format from Imagga API.")
    else:
        print("Failed to fetch image.")