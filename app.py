from flask import Flask
import webbrowser
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
def open_browser():
    webbrowser.open('diet_recommender.py')
    return 'diet_recommender.py'
if __name__ == '__main__':
    app.run(debug=True,threaded=True)
    open_browser()
