from flask import Flask, render_template, request, Response
from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)

db = client.user_db  #database name user_do is created
user_db_collection = db.user_data  #collection user_data is created

def fill_form(username, description):
    user_data = {
        'name' : username,
        'desc' : description
    }
    result = user_db_collection.insert_one(user_data)
    print(f'Task inserted with id: {result.inserted_id}')

def read_data():
    res = user_db_collection.find()
    print('This is the data present:')
    for docs in res:
        print(f'{docs["name"]}: {docs["desc"]}')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route("/submit", methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    description = request.form.get('description')
    fill_form(username, description)
    read_data()
    # if username == "Kaustav" and password == "123":
    #     return render_template("Welcome.html", name = username)

    valid_user = {
        'Kaustav' : '812004',
        'Gaurav' : '2580',
        'Vishesh' : '6392'
    }

    if username in valid_user and password == valid_user[username]:
        return render_template('Welcome.html', name = username)
    else:
        return render_template('login.html')
        # return Response("Invalid username or password", mimetype='text/plain')
if __name__ == '__main__':
    app.run(debug = True)