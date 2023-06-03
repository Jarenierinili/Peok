import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print("Failed to download file.")

if __name__ == "__main__":
    # URL of the file to download
    file_url = "https://example.com/path/to/file.txt"

    # Destination path to save the downloaded file
    save_path = "downloads/file.txt"

    # Create the 'downloads' directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Download the file
    download_file(file_url, save_path)
