from flask import Flask, jsonify, request
import json
app = Flask(__name__)

with open('anim.json') as json_data:
    data = json.load(json_data)


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Your cock and bull story was not found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/titles')
def  titles():
    result = []
    for animation in data['animations']:
        result.append(animation['Original title'])
    return result


@app.route('/ids/<int:animationid>')
def ids(animationid):
    for animation in data['animations']:
        if animationid == animation["ID"]:
            return animation
    return not_found()


@app.route('/titles/<keyword>')
def gimmie_moovies(keyword):
    result = []
    for animation in data['animations']:
        for _keyword in animation['Keywords']:
            if _keyword == keyword:
                result.append(animation['Original title'])
    return result


@app.route('/studios/<int:id>', methods = ['PUT'])
def illegal_studio_swap(id):
    studio = request.args.get("studio")
    if not studio:
        return not_found
    for animation in data['animations']:
        if id == animation['ID']:
            animation["Studio"] = studio
            return 'Your illegal studio swap has unfortunately succeeded'
    return not_found()
