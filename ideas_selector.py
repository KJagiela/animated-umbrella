import json
import random

from flask import Flask, request


app = Flask(__name__)


with open('ideas.json') as fp:
    all_ideas = json.load(fp)


def get_productivity(ideas, is_productive):
    if is_productive:
        return ideas['productive']
    if is_productive == 0:
        return ideas['relaxing']
    return {**ideas['productive'], **ideas['relaxing']}


def get_activity(ideas, is_potato):
    if is_potato:
        return ideas['potato']
    if is_potato == 0:
        return ideas['active']
    return ideas['potato'] + ideas['active']


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    is_potato = data.get('potato', None)
    is_productive = data.get('productive', None)
    activities = get_activity(
        get_productivity(all_ideas, is_productive),
        is_potato,
    )
    choice = random.choice(activities)
    return {'resp': choice}


if __name__ == '__main__':
    app.run(host='0.0.0.0')