import glass
from flask import request
import requests
import image
import json
app = glass.Application(
    name="vision",
    client_id="636544669967.apps.googleusercontent.com",
    client_secret="y4QTTT6DE8wCYjZFKfKX-2Bb")

@app.web.route("/")
def index():
    return """<a href="/glass/oauth/authorize">Login</a>"""

@app.web.route("/process", methods=['POST'])
def process():
    picture = request.files['pic'].read()
    request.files['pic'].seek(0)
    r = requests.post('http://localhost:3350/swt/detect.words', picture)
    boxes = json.loads(r.text)
    image.mask_image(request.files['pic'], boxes)
    return "YO"

@app.subscriptions.action("SHARE")
def share():
    print "Recieved SHARE"

@app.subscriptions.login
def login(user):
    print "user : %s" % user.token
    print user.session
    user.contacts.insert(displayName="Vision for Glass", id="vision-for-glass")
    user.timeline.post(text="Hello World!")

if __name__ == '__main__':
    app.run(port=8080)
