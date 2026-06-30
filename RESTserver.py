from flask import Flask, jsonify ,request

app = Flask(__name__)

customers = [
    {"id": 1, "name": "anant", "age": 19},
    {"id": 2, "name": "krishnav", "age": 20},
    {"id": 3, "name": "aarav", "age": 19},
    {"id": 4, "name": "saksham", "age": 18}
]
@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)
@app.route("/customers/<int:customer_id>", methods = {"GET"})
def get_customers_by_id(customer_id):
    customer = next((c for c in customers if c["id"]== customer_id),None)
    if customer is None:
        return jsonify({"error!": "the customer is not there"}), 404
    return jsonify(customer)
@app.route("/customers", methods = ["POST"])
def add_customer():
    new_customer = request.get_json()
    new_customer["id"]= len(customers) + 1
    customers.append(new_customer)
    return jsonify(new_customer),201
if __name__ == "__main__":
    app.run(port = 5000 , debug = True )



