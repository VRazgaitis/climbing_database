import sql_queries
import re
import webbrowser
import requests
from lxml import html, etree

def scrape_MP_route_img(route_url):
    """
    Given a Mountain Project (MP) climbing route URL, returns a URL of an image of the climbing route.
    
    Args:
    - route_url (string): A URL of a climbing route page on MP

    Returns:
    - list of strings: A list of strings that are URL's to images of the climbing route
    - None: if image was not found 
    """
    response = requests.get(route_url)
    tree = html.fromstring(response.content)
    div_elements = tree.xpath('//div')
    route_image_urls = []
    # Loop through the div elements and filter by 'id' that starts with 'carousel-item-' followed by numbers
    for div in div_elements:
        div_id = div.get('id')
        if div_id and re.match(r'^carousel-item-\d+$', div_id):
            img_url = div.get('style')
            if img_url and 'background-image:' in img_url:
                img_url = img_url.split("'")[1]
            elif not img_url:
                img_url = div.get('data-src')
            if not img_url:
                continue
            route_image_urls.append(img_url)
    if not route_image_urls:  # add a stock photo if image scrape failed
        route_image_urls.append('https://cdn.climbing.com/wp-content/uploads/2016/03/burr102411-024jpg-1024x683.jpg?width=1200')
    return route_image_urls

if __name__ == "__main__":
    ### EXAMPLE USAGE ###
    mp_route_url = sql_queries.get_route_url("Coffindaffer's Dream")
    route_img_urls = scrape_MP_route_img(mp_route_url)
    webbrowser.open(route_img_urls[0])  # variable number of img url's depending on the MP page
