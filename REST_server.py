from flask import Flask,jsonify,request

app = Flask(__name__)

employees = [
    {"id": 1 , "name": "Anant", "domain": "ai generative"},
    {"id": 2 , "name": "Krishnav", "domain": "Finance"},
    {"id": 3 , "name": "saksham", "domain": "web development"}
]
next_id = 4

def get_employee(employee_id):
    return next((e for e in employees if e["id"]== employee_id),None)

@app.route("/employees", methods = ["GET"])
def get_employee_via_domain():
    domain = request.args.get("domain")
    if domain:
        result = [d for d in employees if d["domain"].lower() == domain.lower()]
    else:
        result = employees
    return jsonify(result), 200

@app.route("/employees/<int:employee_id>" , methods = ["GET"])
def get_employe_via_id(employee_id):
    employee = get_employee(employee_id)
    if employee is None:
        return jsonify({"error!": f"employee {employee_id} not found"}), 404
    return jsonify(employee), 200

@app.route("/employees", methods = ["POST"])
def add_employee():
    global next_id
    data = request.get_json(silent = True)
    if not data or "name" not in data or "domain" not in data:
        return jsonify({"error!": "name and domain are required"}), 400
    new_employee = {
        "id": next_id,
        "name":data["name"],
        "domain": data["domain"]
    }
    employees.append(new_employee)
    next_id +=1
    return jsonify(new_employee), 201
@app.route("/employees/<int:employee_id>", methods = ["PUT"])
def update_employee(employee_id):
    employee = get_employee(employee_id)
    if employee is None:
        return jsonify ({"error!": f"the employee {employee_id} not found"}), 404
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error!":"request body required"}), 400
    employee["name"]= data.get("name", employee["name"])
    employee["domain"]= data.get("domain", employee["domain"])
    return jsonify(employee), 200
@app.route("/employees/<int:employee_id>", methods = ["DELETE"])
def delete_employee(employee_id):
    employee = get_employee(employee_id)
    if employee is None:
        return jsonify({"error!": f"employee {employee_id} not found"}), 404
    employees.remove(employee)
    return jsonify({"message": f"employee {employee_id} deleted successfully"}), 200
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error!":"resource not found"}), 404

if __name__ == "__main__":
    app.run(port = 5000, debug = True)