from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)

stations_data_frame = read_csv('data_small/stations.txt', skiprows=17)


@app.route('/')
def home():
    return render_template('home.html', stations=stations_data_frame[['STAID', 'STANAME                                 ']].to_html())


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


@app.route('/api/v1/<station>')
def get_all_station_data(station):
    data_frame = read_csv(f'data_small/TG_STAID{station.zfill(6)}.txt', skiprows=20, parse_dates=['    DATE'])

    return data_frame.to_dict(orient='records')


@app.route('/api/v1/<station>/year/<year>')
def get_station_yearly_data(station, year):
    data_frame = read_csv(f'data_small/TG_STAID{station.zfill(6)}.txt', skiprows=20)

    data_frame['DATE_STRINGIFIED'] = data_frame['    DATE'].astype(str)
    yearly_data = data_frame['DATE_STRINGIFIED'].str.startswith(str(year))

    return data_frame[yearly_data].to_dict(orient='records')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
