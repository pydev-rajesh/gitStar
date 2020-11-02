from flask import Flask, render_template
import csv
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("result.csv")
    df = df.dropna(how='any')
    data = df.to_dict(orient='records')
   
    return render_template('index.html', data=data)

if __name__ == '__main__':
        app.run(debug=True)