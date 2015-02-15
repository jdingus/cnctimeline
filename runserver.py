from flask import Flask, render_template
app = Flask(__name__)

import datetime as dt
import gviz_api

@app.route('/timeline/')
def timeline():
    description = [('Start', 'datetime'),('Stop', 'datetime'),('Part Number', 'string'),('CNC', 'string')]

    data = [(dt.datetime(2015, 02, 15, 12, 30,25, tzinfo=None),dt.datetime(2015, 02, 15, 12, 45,45, tzinfo=None),'60556-105','570')]

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Creating a JavaScript code string
    jscode = data_table.ToJSCode("data")
    print jscode
    return render_template('template.html', data=jscode)

if __name__ == '__main__':
    # Set up the development server on port 5000.
    port = 5000
    app.debug = True
    app.run(port=port)
