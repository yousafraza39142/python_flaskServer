from flask import Flask, Response
import json
from flask import jsonify, abort, request

app = Flask(__name__)


# import logging
#
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

def get_students():
    with open('data.json') as json_file:
        data = json.load(json_file)

    if request.method == "GET":
        json_file.close()
        return jsonify(data["data"])


def student_add():
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

    return Response("Student Created", status=201, mimetype='application/json')


def get_by_id(stu_id):
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
    return Response("Not Found", status=404, mimetype='application/json')


def update_std(stu_id):
    updated = bool(0)
    id = int(stu_id)
    with open('data.json') as json_file:
        data = json.load(json_file)

    # del
    newData = request.json

    index = 0
    for std in data["data"]:
        if std["id"] == id:
            updated = bool(1)
            if newData["name"] != "":
                data["data"][index]["name"] = newData["name"]
            if newData["email"] != "":
                data["data"][index]["email"] = newData["email"]
            if newData["year"] < 0:
                data["data"][index]["year"] = newData["year"]
        index += 1

    # print(data)
    json_file.close()

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

    if (updated):
        return Response('Updated', status=200, mimetype='application/json')
    else:
        return Response("Not found", status=404, mimetype='application/json')


def delete_student(stu_id):
    deleted = bool(0)
    id = int(stu_id)
    with open('data.json') as json_file:
        data = json.load(json_file)

    # del
    print(type(data["data"]))

    index = 0
    for std in data["data"]:
        if std["id"] == id:
            del data["data"][index]
            deleted = bool(1)
        index += 1

    print(data)
    json_file.close()

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

    if deleted:
        return Response('Deleted', status=200, mimetype='application/json')
    else:
        return Response('Not Found', status=404, mimetype='application/json')


@app.route('/students/', methods=['POST', 'GET'])
def students_route():
    if request.method == "GET":
        return get_students()
    elif request.method == "POST":
        return student_add()


@app.route('/students/<stu_id>', methods=['PUT', 'GET', 'DELETE'])
def student_id_route(stu_id):
    if request.method == "GET":
        return get_by_id(stu_id)
    elif request.method == "PUT":
        return update_std(stu_id)
    elif request.method == "DELETE":
        return delete_student(stu_id)


if __name__ == '__main__':
    app.run()
