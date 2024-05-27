import re
import webbrowser
import requests
from lxml import html, etree
import sqlite3

def get_route_url(routename):
    """
    Makes a query to the database, to retrieve the URL of the Mountain Project (MP) page for the 
    specified climbing route.

    ***WARNING***
    No error checking on unsuccessful DB queries

    Args:
    - routename (string): the name of a climbing route from the Routes schema in the database.

    Returns:
    - string: A URL of the specified Route's MP page
    """
    conn = sqlite3.connect(database='Database/MyClimb.db')
    cur = conn.cursor()
    query='''
    SELECT MP_URL 
    FROM Routes 
    WHERE RouteName= ? 
    '''
    cur.execute(query, (routename,))
    route_url = cur.fetchall()[0][0]
    # print(route_url)
    conn.close()
    return route_url

def scrape_MP_route_img(route_url):
    """
    Given a Mountain Project (MP) climbing route URL, scrapes the images carousel
    and returns a list of all but the first image
    
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

def populate_imgs_list(route_url):
    """
    Given a Mountain Project (MP) climbing route URL, returns a list of URL's of all images of the 
    climbing route on the MP page.
    
    Args:
    - route_url (string): A URL of a climbing route page on MP

    Returns:
    - list of strings: URL's to images of the climbing route
    - None: if image was not found 
    """
    response = requests.get(route_url)
    tree = html.fromstring(response.content)
    div_elements = tree.xpath('//div')
    route_image_urls = []
    for div in div_elements:
        # isolate photo cards 
        if div.get('class') == 'col-xs-4 col-lg-3 card-with-photo':
            for child in div.iterchildren():
                if child.get('class') == 'card-with-photo photo-card':
                    # get the URL of a MP photo page
                    img_page_url=child.get('href')
                    img_url=scrape_img_url(img_page_url)
                    route_image_urls.append(img_url)
    return route_image_urls

def scrape_img_url(url):
    """
    Given a Mountain Project (MP) photo page URL, scrapes the webpage and returns only the 
    URL of of the image itself.

    Example photo page: 
    https://www.mountainproject.com/photo/122807545/levi-on-coffindaffers-dream-photo-by-at-crimp-scampi
    
    Args:
    - url (string): A URL of a climbing route photo **page** on MP

    Returns:
    - url (string): A URL of a climbing route **photo**
    """
    response = requests.get(url)
    tree = html.fromstring(response.content)
    div_elements = tree.xpath('//div')
    for div in div_elements:
        if div.get('class') == 'expand text-xs-center':
            for child in div.iterchildren():
                img_link=child.get('href')
                return img_link

if __name__ == "__main__":
    ### EXAMPLE USAGE ###
    mp_route_url = get_route_url("A Brief History of Climb")
    img_urls = populate_imgs_list(mp_route_url)
    for url in img_urls[:3]:
        webbrowser.open(url)
