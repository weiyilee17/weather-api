from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def api(station, date):
    return {
        "station": station,
        "date": date
    }


if __name__ == '__main__':
    app.run(debug=True, port=5001)
