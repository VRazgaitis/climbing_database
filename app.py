from flask import *
import sqlite3
import populateDB

# Initialize the App
app = Flask(__name__)

def get_db():
    '''
    Establish and return a Database Connection.
    '''
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Database/MyClimb.db')
        db.row_factory = sqlite3.Row
        setattr(g, '_database', db)
    return db

@app.teardown_appcontext
def close_connection(exception):
    '''
    Close the connection to the Database when the app is closed or when a request
    is completed.
    '''
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    '''
    Query the database and either return all the records or a single record.
    '''
    db = get_db()
    cursor = db.execute(query, args)
    rows = cursor.fetchall()
    db.commit()
    cursor.close()
    if rows:
        if one:
            return rows[0]
        return rows
    return None

@app.route("/")
def index():
    '''
    Display the landing page.
    '''
    return render_template('index.html')

@app.route('/api/submit-ratings-query', methods=['POST'])
def submit_ratings_query():
    '''
    Handle the form submission for interactive ranking query
    '''
    query_type = request.form['queryDecimal']
    query_relation = request.form['queryRelation']
    print(query_type, query_relation)
    # TODO: Implement the query logic based on query_type

    querystr = 'SELECT * FROM Routes WHERE AVG_STARS {} {} ORDER BY AVG_STARS DESC'.format(query_relation, query_type)
    rows = query_db(querystr)
    return render_template('results.html', type=query_type, rows=rows)

@app.route('/api/submit-query', methods=['POST'])
def submit_query():
    '''
    Handle the form submission for queries.
    '''
    query_type = request.form['queryType']
    print(query_type)
    # TODO: Implement the query logic based on query_type
    
    match query_type:
        case 'query1':
            rows = query_db('SELECT * FROM Routes WHERE Difficulty < {}'.format(populateDB.convert_YDS_to_int('5.11')))
        case 'query2':
            rows = query_db('''SELECT * FROM Routes AS R 
                            INNER JOIN Equipment_used AS E on R.RouteName = E.RouteName
                            WHERE E.ProductName = "Climbing Helmet"''')
        case 'query4':
            rows = query_db('''SELECT T."ClimberName", R."RouteName", R."Difficulty_Rating", R."URL" 
                            FROM "Ticks" T JOIN Routes R ON R."RouteName" = T."RouteName" 
                            ORDER BY "Difficulty" desc LIMIT 1''')
        case 'query5':
            rows = query_db('''SELECT R."RouteName", R.Location, G."MainGeology", R."AVG_STARS" 
                            FROM "Routes" R JOIN "Common_geologies" G ON G."Region" = R."Region" 
                            WHERE G."MainGeology" LIKE "%Sandstone" 
                            ORDER BY "AVG_STARS" desc LIMIT 5''')
        case 'query6':
            rows = query_db('''SELECT URL, RouteName, Difficulty_Rating, Region, MAX("AVG_STARS") AS HighestRating
                               FROM Routes WHERE "Difficulty_Rating" LIKE '5.10%'
                               GROUP BY Region''')
            
    return render_template('results.html', type=query_type, rows=rows)

@app.route('/api/relation/<string:table_name>')
def relation(table_name):
    '''
    Return the records within a given relation from the Database as a rendered HTML page.
    '''
    rows = query_db(f'SELECT * FROM {table_name}')
    
    return render_template('relation.html', type=table_name, rows=rows)

@app.route('/user-query')
def custom():
    '''
    Display the page custom query page.
    '''
    return render_template('custom.html')

@app.route('/api/user-query')
def user_query():
    '''
    Return json object which includes information for a custom query.
    '''
    pass

if __name__ == '__main__':
    app.run(debug=True)
