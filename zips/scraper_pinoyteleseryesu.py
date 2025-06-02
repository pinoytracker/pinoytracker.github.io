import requests, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import xbmc

def scrape(url, label='PINOYTELESERYESU', color='hotpink'):
    xbmc.log(f"[scraper_pinoyteleseryesu] First Url {url}", xbmc.LOGINFO)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    shows_list = []
    next_pages = []

    try:
        # Step 1: Extract current page number from the URL
        match = re.search(r'page=(\d+)', url)
        current_page = int(match.group(1)) if match else 1
        xbmc.log(f"\n\n [scraper_pinoyteleseryesu] CURRENT URL INITIAL LOAD {url}", xbmc.LOGINFO)
        # Step 2: Fetch API data for this page
        api_url = f'https://www.pinoylive.su/api/articles.php?page={current_page}'
        xbmc.log(f"\n\n [scraper_pinoyteleseryesu] CURRENT URL FOR SCRAPING {api_url}", xbmc.LOGINFO)

        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        base_url = "https://www.pinoylive.su/"

        articles = data
        for item in articles:
            full_url = urljoin(base_url, item.get('url'))

            title = item.get('title')
            article_url = full_url
            thumbnail = item.get('thumbnail')
            xbmc.log(f"\n\n [scraper_pinoyteleseryesu] Load the dETAILS URL {article_url}", xbmc.LOGINFO)

            shows_list.append({
                'url': article_url,
                'title': title,
                'image': thumbnail
            })
        # Step 3: Load the HTML page for "Next" link

        html_url = f'https://www.pinoylive.su/home.php?page={current_page}'
        #xbmc.log(f"\n\n [scraper_pinoyteleseryesu] Load the HTML page for Next link {html_url}", xbmc.LOGINFO)

        html_response = requests.get(html_url, headers=headers, timeout=10)
        #xbmc.log(f"\n [scraper_pinoyteleseryesu] 2nd Url {html_url}", xbmc.LOGINFO)

        next_page_match = re.search(r'<a\s+href="([^"]+)"\s+class="next"[^>]*>Next</a>', html_response.text, re.IGNORECASE)
        #xbmc.log(f"\n\n [scraper_pinoyteleseryesu] Found next href: {next_page_match}", xbmc.LOGINFO)

        if next_page_match:
            next_href = next_page_match.group(1)
            #xbmc.log(f"\n\n [scraper_pinoyteleseryesu] next_page_match: {next_href}", xbmc.LOGINFO)

            # Extract page number from href URL
            page_match = re.search(r'page=(\d+)', next_href)
            if page_match:
                next_page_number = page_match.group(1)
                next_api_url = f'https://www.pinoylive.su/api/articles.php?page={next_page_number}'
                # Construct the API URL for next page                
                #xbmc.log(f"\n\n [scraper_pinoyteleseryesu] Found NEXTPAGE next_api_url: {next_api_url}", xbmc.LOGINFO)    

            xbmc.log(f"\n\n [scraper_pinoyteleseryesu] NEXT PAGE COLOR: {color}", xbmc.LOGINFO)
            next_pages.append({
                'url': next_api_url,
                'label': label,
                'color': color
            })

    except Exception as e:
        xbmc.log(f"[scraper_pinoyteleseryesu] Error scraping {url}: {e}", xbmc.LOGERROR)

    #xbmc.log(f"[scraper_pinoyteleseryesu]  {shows_list}: [Next Pages] {next_pages}", xbmc.LOGINFO)    

    return shows_list, next_pages
