import requests
BASE_URL = "http://127.0.0.1:5000"
def get_employees():
    response = requests.get(f"{BASE_URL}/employees")
    print("all employees",response.status_code , response.json())
def get_employees_by_domain(domain):
    response = requests.get(f"{BASE_URL}/employees", params = {"domain": domain})
    print(f"employees in {domain} domain", response.status_code, response.json())
def get_employee_by_id(employee_id):
    response = requests.get(f"{BASE_URL}/employees/{employee_id}")
    print(f"employee {employee_id}", response.status_code, response.json())
def add_employee(name, domain):
    new_employee = {"name": name, "domain": domain}
    response = requests.post(f"{BASE_URL}/employees", json = new_employee)
    print("created", response.status_code, response.json())
def update_employee(employee_id, **fields):
    response = requests.put(f"{BASE_URL}/employees/{employee_id}",json = fields)
    print(f"updated employee {employee_id}", response.status_code, response.json())
def delete_employee(employee_id):
    response = requests.delete(f"{BASE_URL}/employees/{employee_id}")
    print(f"deleted employee {employee_id}", response.status_code, response.json())
if __name__ == "__main__":
    print("__get all__")
    get_employees()
    print("__get by domain__")
    get_employees_by_domain("IT")
    print("__get by id__")
    get_employee_by_id(2)
    print("__add employee__")
    add_employee("ishaan", "IT")
    print("__update employee__")
    update_employee(2, name = "ishaan", domain = "IT")
    print("__delete employee__")
    delete_employee(2)
    print("__confirm deletion__")
    get_employee_by_id(2)