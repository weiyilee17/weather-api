from flask import Flask, render_template
from pandas import read_csv

app = Flask(__name__)

data_frame = read_csv('dictionary.csv')


@app.route('/')
def home():
    return render_template('translator_home.html')


@app.route('/api/v1/<word>')
def translate(word):

    target = data_frame.loc[data_frame['word'] == word]

    return {
        "definition": target['definition'].squeeze(),
        "word": word
    }


if __name__ == '__main__':
    app.run(debug=True, port=5002)
