from flask import Flask, render_template, session
from config import Config
from routes.auth import auth
from routes.orders import orders
from routes.inventory import inventory
from routes.accounting import accounting
from routes.finance import finance
from routes.language import language

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

app.register_blueprint(auth)
app.register_blueprint(orders)
app.register_blueprint(inventory)
app.register_blueprint(accounting)
app.register_blueprint(finance)
app.register_blueprint(language)

@app.context_processor
def inject_language():
    lang = session.get('lang', 'ar')
    return dict(lang=lang)

@app.route('/')
def dashboard():
    lang = session.get('lang', 'ar')
    return render_template(f'{lang}/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
