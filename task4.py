
import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
   
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def parse_headlines(html_content):
   
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        headlines = []
        
        
        for headline in soup.find_all('h2', class_='headline'):
            headlines.append(headline.get_text())
        
        return headlines
    except Exception as e:
        print(f"Error parsing the HTML content: {e}")
        return []

def display_headlines(headlines):
    
    if headlines:
        print("News Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline}")
    else:
        print("No headlines found.")

def main():
    url = 'https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=4435396578870885450&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9075302&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1'  
    html_content = fetch_webpage(url)
    
    if html_content:
        headlines = parse_headlines(html_content)
        display_headlines(headlines)

if __name__ == "__main__":
    main()
