import random
import string
import time
import json
from flask import Flask, request

app = Flask(__name__)


class Notification:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.createdAt = time.time()


notifications = {}


@app.route("/notifications/add", methods=["POST"])
def add_notification():
    id = get_id()
    jsonData = request.json
    notificationObj = Notification(id, jsonData)
    notifications[id] = notificationObj
    return json.dumps({"id": id, "success": "true"})


@app.route("/notifications/remove", methods=["POST"])
def remove_notifications():
    jsonData = request.json
    id = jsonData['id']
    if id in notifications:
        del notifications[id]
        return json.dumps({"success": "true"})
    else:
        return json.dumps({"success": "false"})


@app.route("/notifications/list")
def list_notifications():
    return json.dumps([x.__dict__ for x in notifications.values()])


@app.route("/notifications/clear")
def clear_notifications():
    global notifications
    notifications = {}
    return json.dumps({"success": "true"})


# TODO: Clear by type, clear by age
# Types should have a form of inheritance:
# E.g. message => message/email message/facebook message/facebook/image


def get_id():
    id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                 range(32))
    if id not in notifications:
        return id
    else:
        return get_id()


app.run('0.0.0.0', 8181, threaded=True)
