import os
import requests
import pandas as pd

# Replace with your own API key and Custom Search Engine ID
API_KEY = 'YOUR_API_KEY'
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'
QUERY = 'YOUR QUERY'
NUM_IMAGES = 1000
MIN_WIDTH = 640
MIN_HEIGHT = 480

def fetch_image_info(query, api_key, search_engine_id, num_images, min_width, min_height):
    image_info_list = []
    page_limit = num_images // 10
    for start in range(1, page_limit + 1):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&searchType=image&start={start * 10 - 9}&num=10&key={api_key}&cx={search_engine_id}"
        response = requests.get(url).json()
        if 'items' not in response:
            break
        for item in response['items']:
            if 'image' in item:
                width = item['image'].get('width', 0)
                height = item['image'].get('height', 0)
                if width >= min_width and height >= min_height:
                    image_info = {
                        'title': item['title'],
                        'link': item['link'],
                        'page_link': item['image']['contextLink']
                    }
                    image_info_list.append(image_info)
                    if len(image_info_list) >= num_images:
                        return image_info_list
    return image_info_list

def download_images(image_info_list, save_dir='images'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for idx, info in enumerate(image_info_list):
        try:
            response = requests.get(info['link'])
            if response.status_code == 200:
                with open(os.path.join(save_dir, f'image_{idx + 1}.jpg'), 'wb') as file:
                    file.write(response.content)
            print(f"Downloaded image {idx + 1}/{len(image_info_list)}")
        except Exception as e:
            print(f"Could not download image {idx + 1}. Error: {e}")

def save_image_info_to_csv(image_info_list, filename='image_info.csv'):
    df = pd.DataFrame(image_info_list)
    df.to_csv(filename, index=False)
    print(f"Saved image info to {filename}")

def main():
    image_info_list = fetch_image_info(QUERY, API_KEY, SEARCH_ENGINE_ID, NUM_IMAGES, MIN_WIDTH, MIN_HEIGHT)
    print(f"Found {len(image_info_list)} images meeting the criteria")
    download_images(image_info_list)
    save_image_info_to_csv(image_info_list)

if __name__ == "__main__":
    main()
