import random

from flask import *
import sqlite3
import json
from werkzeug.utils import secure_filename
import os
import bisect
import datetime


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/thumbnails/'


def upload_sandwich(name, title, author, description, blog, thumbnail, date):
    conn = sqlite3.connect("sandwich.db")
    cursor = conn.cursor()
    cursor.execute('''
            INSERT OR IGNORE INTO sandwiches (name, description, blog, author, thumbnail, date, title)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, description, blog, author, thumbnail, date, title))

    conn.commit()




def get_sandwiches():

    conn = sqlite3.connect('sandwich.db')
    cursor = conn.cursor()
    query = "SELECT * FROM Sandwiches"
    cursor.execute(query)
    rows = cursor.fetchall()

    sandwiches = {}
    for sandwich in rows:

        sandwiches[sandwich[1]] = {}
        sandwiches[sandwich[1]]['Description'] = sandwich[2]
        sandwiches[sandwich[1]]['Blog'] = sandwich[3]
        sandwiches[sandwich[1]]['Author'] = sandwich[4]
        sandwiches[sandwich[1]]['thumbnail'] = sandwich[5]
        sandwiches[sandwich[1]]['Date'] = sandwich[6]


    conn.close()
    return sandwiches

def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def save_json(dict, filename):
    with open(filename, 'w') as f:
        json.dump(dict, f)
        f.close()


def get_date():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y-%H:%M:%S")

def get_sandwiches_random(amount):
    sarnies = get_sandwiches()
    keys = sorted(list(sarnies.keys()))
    sandwiches = {}
    for i in range(amount):
        pop = random.randint(0, len(keys) - 1)
        index = keys[pop]
        sandwiches[index] = sarnies[index]
        keys.pop(pop)

    return sandwiches



@app.route('/')
def dashboard():  # put application's code here
    blogs = get_sandwiches_random(12)
    print(blogs)
    return render_template("landing.html", blogs=blogs)

@app.route('/sandwiches')
def mcsandwiches():  # put application's code here
    blogs = get_sandwiches()
    items = len(blogs)

    return render_template("sandwiches.html", blogs=blogs, items=items)

@app.route('/upload', methods=['GET', 'POST'])
def upload_blog():  # put application's code here
    if request.method == 'POST':

        blog_title = request.form['blog_name']
        blog_description = request.form['description']
        blog = request.form['blog']
        author = request.form['author']




        file = request.files['file']
        filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filename)

        thumbnail = "thumbnails/"+file.filename


        upload_sandwich(blog_title, blog_title, author, blog_description, blog, thumbnail,get_date())
        return redirect(f"/blog/{blog_title}")

    else:
        return render_template("upload_form.html")

@app.route('/blog/<string:blog_title>')
def blog(blog_title):
    blogs = get_sandwiches()
    if blog_title in blogs:
        image = blogs[blog_title]["thumbnail"]
        print(image)
        print(blogs[blog_title]['Author'])
        return render_template("blog.html", blog=blogs[blog_title], blog_title=blog_title, image=image)
    else:
        return redirect(url_for('/'))

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
