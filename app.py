from flask import Flask, g, render_template, request
import sqlite3

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
    query_type = request.form['queryType']
    print(query_type)
    # TODO: Implement the query logic based on query_type

    querystr = 'SELECT * FROM Routes WHERE AVG_STARS < {} ORDER BY AVG_STARS DESC'.format(query_type)
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
    
    if query_type == 'query1':
        rows = query_db('SELECT * FROM Routes WHERE AVG_STARS > 4.5')

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
