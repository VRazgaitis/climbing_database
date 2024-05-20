import sql_queries
import re
import webbrowser
import requests
from lxml import html

def scrape_MP_route_img(route_url):
    """
    Given a Mountain Project (MP) climbing route URL, returns a URL of an image of the climbing route.
    
    Args:
    - route_url (string): A URL of a climbing route page on MP

    Returns:
    - string: A URL of an image of the climbing route
    - None: if image was not found 
    """
    response = requests.get(route_url)
    tree = html.fromstring(response.content)
    div_elements = tree.xpath('//div')
    # Loop through the div elements and filter by 'id' that starts with 'carousel-item-' followed by numbers
    for div in div_elements:
        div_id = div.get('id')
        if div_id and re.match(r'^carousel-item-\d+$', div_id):
            style_string = div.get('style')
            if style_string:
                return style_string.split("'")[1]

if __name__ == "__main__":
    ### EXAMPLE USAGE ###
    mp_route_url = sql_queries.get_route_url("Apollo Reed")
    route_img_url = scrape_MP_route_img(mp_route_url)
    if route_img_url:
        webbrowser.open(route_img_url)