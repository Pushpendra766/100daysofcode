from flask import Flask, render_template
from post import Post
import requests

blogs = requests.get(url="https://api.npoint.io/283bc734ab20e7ae7bfe").json()
blog_objects = []
for blog in blogs:
    blog_obj = Post(blog['id'], blog['title'], blog['subtitle'], blog['body'])
    blog_objects.append(blog_obj)


app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/post/<int:index>")
def get_blog(index):
    requested_post = None
    for blog_post in blog_objects:
        if blog_post.id == index:
            requested_post = blog_post
            break
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
