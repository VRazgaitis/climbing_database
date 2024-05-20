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
    SELECT URL 
    FROM Routes 
    WHERE RouteName= ? 
    '''
    cur.execute(query, (routename,))
    route_url = cur.fetchall()[0][0]
    conn.close()
    return route_url
