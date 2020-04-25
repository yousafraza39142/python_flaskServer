from flask import Flask
import json
from flask import jsonify, abort, request
app = Flask(__name__)


# import logging
#
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)


@app.route('/students')
def students():
    with open('data.json') as json_file:
        data = json.load(json_file)

    if request.method == "GET":
        json_file.close()
        return jsonify(data["data"])


@app.route('/students/<stu_id>')
def student_by_id(stu_id):
    with open('data.json') as json_file:
        data = json.load(json_file)
    global id
    try:
        id = int(stu_id)
    except:
        abort(400)
    for d in data["data"]:
        if (d["id"] == id):
            json_file.close()
            return d
    json_file.close()
    abort(404)


@app.route('/students/post')
def studentsAdd():
    with open('data.json') as json_file:
        data = json.load(json_file)
    currentId = int(data["id"])

    print(request.json)
    jsonObj = json.dumps(request.json, indent=2)
    print(data)
    dat = data["data"]
    jsonObj = request.json
    jsonObj["id"] = currentId
    currentId += 1
    dat.append(jsonObj)
    data["data"] = dat
    data["id"] = currentId
    print(data)
    json_file.close()
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

    return jsonify("done")


@app.route('/students/delete/<stu_id>')
def deleteStudent(stu_id):
    id = int(stu_id)
    with open('data.json') as json_file:
        data = json.load(json_file)

    # del
    print(type(data["data"]))

    index = 0
    for std in data["data"]:
        if std["id"] == id:
            del data["data"][index]
        index += 1

    print(data)
    json_file.close()

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

    return jsonify("done")


@app.route('/students/update/<stu_id>')
def UpdateStd(stu_id):
    id = int(stu_id)
    with open('data.json') as json_file:
        data = json.load(json_file)

    # del
    newData = request.json

    index = 0
    for std in data["data"]:
        if std["id"] == id:
            if newData["name"] != "":
                data["data"][index]["name"] = newData["name"]
            if newData["email"] != "":
                data["data"][index]["email"] = newData["email"]
            if newData["year"] < 0:
                data["data"][index]["year"] = newData["year"]
        index += 1

    print(data)
    json_file.close()

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

    return jsonify("done")


if __name__ == '__main__':
    app.run()