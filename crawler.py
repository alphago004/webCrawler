import os
import requests
from bs4 import BeautifulSoup
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def crawl(url, depth=3):
    visited = set()
    queue = [(url, 0)]

    while queue:
        url, level = queue.pop(0)
        if level <= depth and url not in visited:
            try:
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    print(f"Crawling {url}...")
                    visited.add(url)
                    soup = BeautifulSoup(response.content, 'html.parser')

                    # Extract content from all <script> tags
                    for script_tag in soup.find_all('script'):
                        script_content = script_tag.string
                        if script_content:
                            
                            temp_filename = f"{url.replace('/', '_')}_script.txt"
                            with open(temp_filename, 'w') as f:
                                f.write(script_content.strip())

                            # Upload the temporary file to S3
                            s3.upload_file(temp_filename, 'crawler-bucket2', temp_filename)
                            os.remove(temp_filename)  # Remove the temporary file

                    # Find and follow links on the page
                    for link in soup.find_all('a', href=True):
                        next_url = link['href']
                        if next_url.startswith('http') and next_url not in visited:
                            queue.append((next_url, level + 1))

            except Exception as e:
                print(f"Error crawling {url}: {e}")

if __name__ == "__main__":
    start_url = "https://www.example.com/"
    crawl(start_url)
