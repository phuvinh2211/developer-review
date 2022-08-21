from flask import g, Markup
from flask import (Blueprint, render_template, make_response,
                   redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
from operator import itemgetter
from tw33t.views.utils import log_search
import os

'''
Twitter API Settings
'''


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


'''
Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''


@app.route('/get_tweets/<screen_name>/', methods=['GET'])
def get_tweets(screen_name):
    if request.method == 'GET':
        try:
            t = Twitter(auth=OAuth2(bearer_token=os.getenv("BEARER_TOKEN")))
            query = t.statuses.user_timeline(
                screen_name=screen_name, count=3)

        except:
            return jsonify([{'creation_date': '-/-/-', 'content': 'User is not exist'}])

        result = []
        for q in query:
            creation_date = list(
                itemgetter(2, 1, 5)
                (q['created_at']
                 .split(' ')
                 )
            )
            creation_date = '/'.join(creation_date)

            content = q['text']
            result.append(
                {
                    'content': content,
                    'creation_date': creation_date
                }
            )

        # Logging
        log_search(screen_name, result)

        return jsonify(result)

    return redirect(url_for('index'))
