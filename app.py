# Flask app launcher
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'Raqeem is running'

if __name__ == '__main__': app.run()