from flask import Flask
import vsearch

app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return "Hello MF."

@app.route('/search4')
def do_search() ->str:
    return str(vsearch.search4vowels('get it work,mother fucker!'))

app.run()
