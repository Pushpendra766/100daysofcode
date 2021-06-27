from flask import Flask, render_template, request
import requests
import smtplib

USER_NAME = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

BLOG_URL = "https://api.npoint.io/cac45e683ffb29c5cfa0"

posts = (requests.get(BLOG_URL)).json()

app = Flask(__name__)

def send_mail(name, email, phone, message):
    message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=PASSWORD)
        connection.sendmail(from_addr=USER_NAME, to_addrs="TO EMAIL ADDRESS", msg=f"Subject: New message\n\n{message}")

@app.route('/')
def get_all_post():
    return render_template("index.html", posts=posts)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html')


@app.route('/about')
def about_us_page():
    return render_template('about.html')

@app.route('/post/<int:index>')
def read_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
            break
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)