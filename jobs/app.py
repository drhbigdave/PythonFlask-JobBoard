from flask import Flask, render_template

app = Flask(__name__)

@app_route('/')
@app_rout('/jobs')
def jobs():
    return render_template('index.html')
