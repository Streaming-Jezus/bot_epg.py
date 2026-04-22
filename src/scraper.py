import requests
from bs4 import BeautifulSoup

# Function to scrape channels from gatotv.com

def scrape_gatotv_channels():
    url = 'https://www.gatotv.com/'  # Change to the actual URL of the channel list
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        channels = []
        
        # Find channel elements - adjust selectors according to actual HTML structure
        for channel in soup.find_all('div', class_='channel'):  # Example class, replace it with the correct one
            channel_name = channel.find('h3').text.strip()  # Example HTML structure
            channel_link = channel.find('a')['href']
            channels.append({'name': channel_name, 'link': channel_link})
        
        return channels
    else:
        print('Failed to retrieve channels')
        return None

if __name__ == '__main__':
    channels = scrape_gatotv_channels()
    if channels:
        for channel in channels:
            print(f"Channel Name: {channel['name']}, Link: {channel['link']}")