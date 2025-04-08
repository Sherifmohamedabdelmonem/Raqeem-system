from flask import Blueprint

auth = Blueprint('auth', __name__)

# مثال لمسار تسجيل الدخول
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "صفحة تسجيل الدخول"# auth.py logic here
