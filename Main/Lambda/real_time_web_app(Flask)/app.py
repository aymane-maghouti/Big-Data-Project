from flask import Flask, render_template
from get_Data_from_hbase import get_last_record_from_hbase


app = Flask(__name__)


@app.route('/')
def index():
    last_record = get_last_record_from_hbase()
    return render_template('index.html',last_record=last_record)


if __name__ == '__main__':
    app.run(debug=True)