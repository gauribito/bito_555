# api_vulnerabilities.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/update')
def update():
    user_id = request.args.get('id')  # No validation
    new_role = request.args.get('role')  # No auth check
    # ...process update...
    return "Updated"

# No CSRF protection
@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    # ...process transfer...
    return "Done"
