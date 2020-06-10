from flask import Flask, request, jsonify

# init app
app = Flask(__name__)

@app.route('/')
def root():
    return "Rest Api with google app engine, mongodbAtlas and Flask"

# Run server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)