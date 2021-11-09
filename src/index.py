from flask import Flask, render_template
from flask_socketio import SocketIO, send


app =Flask(__name__)

app.config['SECRET_KEY']= "2Dsf33kL"
socketio=SocketIO(app)

@app.route("/")
def index():
    return  render_template('index.html')

@app.route("/hi")
def hi():
    socketio.send("hi")
    return  render_template('index.html')

@socketio.on('message')
def handlemessage(msg):
    print("mensage",msg)
    send(msg,broadcast=True)
if __name__=='__main__':
    socketio.run(app)