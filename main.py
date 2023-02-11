from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def api(station, date):

    # Add padding 0s in front of station until it meets 6 char
    data_frame = read_csv(f'data_small/TG_STAID{station.zfill(6)}.txt', skiprows=20, parse_dates=['    DATE'])

    temperature = data_frame.loc[data_frame['    DATE'] == date]['   TG'].squeeze() / 10

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == '__main__':
    app.run(debug=True, port=5001)
