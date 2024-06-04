from bing_image_downloader import downloader
from pathlib import Path

path = Path(__file__).parent
def download_images(query, limit):
    downloader.download(query, limit, output_dir=path)

if __name__ == "__main__":
    keyword = input("Search keyword: ")
    num_image = input("Number of images: ")
    download_images(keyword, int(num_image))