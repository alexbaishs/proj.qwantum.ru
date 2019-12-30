from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

application = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []

@application.route("/", methods=['GET'])
def hello():
   return render_template('index.html')

@application.route("/main", methods=['GET'])
def main():
   return render_template('main.html', messages=messages)
   
@application.route("/add_message", methods=['POST'])
def add_message():
   text = request.form['text']
   tag = request.form['tag']
    
   messages.append(Message(text, tag))
    
   return redirect(url_for('main'))
   

if __name__ == "__main__":
   application.run(host='0.0.0.0')