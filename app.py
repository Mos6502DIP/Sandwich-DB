from flask import *
import json
from werkzeug.utils import secure_filename
import os
import datetime

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/thumbnails/'




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



@app.route('/')
def dashboard():  # put application's code here
    blogs = load_json("blogs.json")
    return render_template("landing.html", blogs=blogs)

@app.route('/upload', methods=['GET', 'POST'])
def upload_blog():  # put application's code here
    if request.method == 'POST':

        blog_title = request.form['blog_name']
        blog_description = request.form['description']
        blog = request.form['blog']


        blogs = load_json('blogs.json')

        if blog_title in blogs:
            return "Blog already exists"

        else:

            blogs[blog_title] = {}
            blogs[blog_title]["Blog"] = blog
            blogs[blog_title]["Description"] = blog_description
            blogs[blog_title]["Date"] = get_date()

            file = request.files['file']
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)

            blogs[blog_title]["thumbnail"] = "thumbnails/"+file.filename

            save_json(blogs, 'blogs.json')

            return redirect('/')
    else:
        return render_template("upload_form.html")

@app.route('/blog/<string:blog_title>')
def blog(blog_title):
    blogs = load_json('blogs.json')
    if blog_title in blogs:
        image = blogs[blog_title]["thumbnail"]
        print(image)
        return render_template("blog.html", blog=blogs[blog_title], blog_title=blog_title, image=image)
    else:
        return redirect(url_for('/'))

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
