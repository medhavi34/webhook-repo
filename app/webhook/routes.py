from flask import Blueprint, jsonify, request
import dateutil.parser as p 
from app import extensions


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

def get_date(date):
    vals = p.parse(date)
    if vals.day%10 == 1: 
        return vals.strftime('%dst %B %Y - %I:%M %p')
    elif vals.day%10 == 2: 
        return vals.strftime('%dnd %B %Y - %I:%M %p')
    elif vals.day%10 == 3: 
        return vals.strftime('%drd %B %Y - %I:%M %p')
    else: 
        return vals.strftime('%dth %B %Y - %I:%M %p')  


@webhook.route('/receiver', methods=["POST"])
def receiver():
    pr = 'pull_request'
    data = None
    if (request.headers['content-type'] =='application/json'):
        my_info = request.json
        if (request.headers['X-GitHub-Event'] == pr):
            data = {
                "request_id": str(my_info[pr]['id']),
                "author":my_info['sender']['login'],
                "to_branch":my_info[pr]['head']['ref'],
                "from_branch":my_info[pr]['base']['ref'],
                "action":"PULL_REQUEST",
                "timestamp":get_date(my_info[pr]['updated_at'])
            }

        elif (request.headers['X-GitHub-Event'] == 'push'):
            data = {
                "request_id": my_info['after'],
                "author":my_info['pusher']['name'],
                "to_branch":my_info['ref'].split('/')[-1],
                "from_branch":my_info['repository']['default_branch'],
                "action":"PUSH",
                "timestamp":get_date(my_info['repository']['updated_at'])
            }

        extensions.insert(data)

        return {},200

@webhook.route('/receiver', methods=["GET"])
def send():
    return "The webhook reciever is working!"