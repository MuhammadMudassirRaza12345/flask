from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list_data = [{"id":1, "name":"write todo list app"}]

@app.route(rule='/todo/api/v1/fetch_todo', methods=['GET'])
def fetch_todo():
    return jsonify(todo_list_data)

@app.route(rule='/todo/api/v1/create_todo', methods=['POST'])
def create_todo():
    if request.method == "POST":
        data = request.get_json()
        todo_list_data.append(data)
        return jsonify(todo_list_data)

@app.route(rule='/todo/api/v1/delete/<int:todo_id>/', methods=['GET'])
def delete_todo(todo_id):
    find_index = -1
    for index, todo in enumerate(todo_list_data):
        if todo['id'] == todo_id:
            find_index = index
    if find_index != -1:
        del todo_list_data[find_index]
    return jsonify(todo_list_data)


    



if __name__=='__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)