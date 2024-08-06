import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with a specific class or id (adjust as needed)
divs = soup.find_all('div', {'class': 'text--prose'})

# Check if there are at least two such divs
if len(divs) > 1:
    # Extract and print all text within the second div
    scraped_data = divs[1].get_text()
    print(scraped_data)
else:
    print('Less than two divs found')

# Save the scraped data to a text file with utf-8 encoding
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    file.write(scraped_data)

# Read the existing HTML file
with open('playlists.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Replace the placeholder with the scraped data
updated_html_content = html_content.replace('<!-- SCRAPED_DATA -->', scraped_data)

# Save the updated HTML content back to the file
with open('playlists.html', 'w', encoding='utf-8') as file:
    file.write(updated_html_content)

    #SECONDPLAYLISTSCRIPT

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with a specific class or id (adjust as needed)
divs = soup.find_all('div', {'class': 'text--prose'})

# Check if there are at least two such divs
if len(divs) > 1:
    # Extract and print all text within the second div
    scraped_data2 = divs[2].get_text()
    print(scraped_data2)
else:
    print('Less than two divs found')

# Save the scraped data to a text file with utf-8 encoding
with open('scraped_data2.txt', 'w', encoding='utf-8') as file:
    file.write(scraped_data2)

# Read the existing HTML file
with open('playlists.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Replace the placeholder with the scraped data
updated_html_content = html_content.replace('<!-- SCRAPED_DATA2 -->', scraped_data2)

# Save the updated HTML content back to the file
with open('playlists.html', 'w', encoding='utf-8') as file:
    file.write(updated_html_content)

    #THIRDPLAYLISTSCRIPT

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with a specific class or id (adjust as needed)
divs = soup.find_all('div', {'class': 'text--prose'})

# Check if there are at least two such divs
if len(divs) > 1:
    # Extract and print all text within the second div
    scraped_data3 = divs[3].get_text()
    print(scraped_data3)
else:
    print('Less than two divs found')

# Save the scraped data to a text file with utf-8 encoding
with open('scraped_data3.txt', 'w', encoding='utf-8') as file:
    file.write(scraped_data3)

# Read the existing HTML file
with open('playlists.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Replace the placeholder with the scraped data
updated_html_content = html_content.replace('<!-- SCRAPED_DATA3 -->', scraped_data3)

# Save the updated HTML content back to the file
with open('playlists.html', 'w', encoding='utf-8') as file:
    file.write(updated_html_content)

import subprocess
import schedule
import time

def run_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
        print(f"Successfully ran {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

def job():
    run_script("playlistsscripts1.py")

# Schedule the job every Monday at 06:00 AM
schedule.every().monday.at("06:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)