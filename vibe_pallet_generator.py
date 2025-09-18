import os
import requests
import base64
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont # Pillowライブラリをインポート

# .envファイルの読み込み
load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_image_from_unsplash(keyword):
    # ... (この関数は変更なし) ...
    url = f"https://api.unsplash.com/photos/random?query={keyword}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['urls']['regular']
    else:
        print("Error fetching image from Unsplash:", response.status_code)
        return None

IMAGGA_API_KEY = os.getenv("IMAGGA_API_KEY")
IMAGGA_API_SECRET = os.getenv("IMAGGA_API_SECRET")

def fetch_colors_from_imagga(image_url):
    # ... (この関数は変更なし) ...
    url = "https://api.imagga.com/v2/colors"
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

# ===== 新しく追加する関数 =====
def create_palette_image(colors):
    """
    色のリストを受け取り、カラーパレットの画像を生成する関数
    """
    swatch_size = 100  # 各色の四角形の一辺のサイズ
    padding = 10      # 余白
    image_width = (swatch_size + padding) * len(colors) + padding
    image_height = swatch_size + (padding * 2) + 40 # 色コード表示用に高さを追加
    
    # 新しい画像を生成 (背景は白)
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    try:
        # フォントを読み込む（指定したフォントがない場合はデフォルト）
        font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        font = ImageFont.load_default()

    # 各色を四角形として描画
    for i, color_info in enumerate(colors):
        rgb = (color_info['r'], color_info['g'], color_info['b'])
        hex_code = color_info['html_code']
        
        # 色の四角形を描画
        x0 = i * (swatch_size + padding) + padding
        y0 = padding
        x1 = x0 + swatch_size
        y1 = y0 + swatch_size
        draw.rectangle([x0, y0, x1, y1], fill=rgb)

        # HEXコードをテキストで描画
        text_position = (x0, y1 + 5)
        draw.text(text_position, hex_code, fill="black", font=font)

    # 画像をファイルとして保存
    image.save("palette.png")
    print("\n🎨 Color palette saved as palette.png")
# ===== ここまで追加 =====

def generate_vibe_palette(keyword):
    print(f"Fetching image for keyword: {keyword}")
    image_url = fetch_image_from_unsplash(keyword)
    if image_url:
        print(f"Image URL: {image_url}")
        print("Fetching color palette...")
        colors_data = fetch_colors_from_imagga(image_url)
        if colors_data and 'result' in colors_data and 'colors' in colors_data['result']:
            image_colors = colors_data['result']['colors']['image_colors']
            print("Generated Color Palette:")
            for color in image_colors:
                print(f"HEX: {color['html_code']}, Name: {color['closest_palette_color']}")
            
            # ===== この行を修正・追加 =====
            # 取得した色情報を使って画像生成関数を呼び出す
            create_palette_image(image_colors)
            # ===== ここまで修正 =====

        else:
            print("Error: Unexpected response format from Imagga API.")
    else:
        print("Failed to fetch image.")