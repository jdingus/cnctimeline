from flask import Flask, render_template
app = Flask(__name__)

import datetime as dt
import gviz_api
import sqlite3 as lite
from dateutil.parser import *

@app.route('/timeline/')
def timeline():
    description = [('Start', 'datetime'),('Stop', 'datetime'),('Part Number', 'string'),('CNC', 'string')]

    # data = [(dt.datetime(2015, 02, 15, 12, 30,25, tzinfo=None),dt.datetime(2015, 02, 15, 12, 45,45, tzinfo=None),'60556-105','570')]
    data = query_list_data()

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Creating a JavaScript code string
    jscode = data_table.ToJSCode("data")
    # print jscode
    return render_template('template.html', data=jscode)

def query_list_data():
    ''' Query entried in the db '''
    con = lite.connect('test.db',detect_types=lite.PARSE_DECLTYPES|lite.PARSE_COLNAMES)
    with con:
        cur = con.cursor()    
        query = 'SELECT start_time,stop_time,part1_num,cnc_id FROM [data] LIMIT 500'
        cur.execute(query)
        all_data = []
        results = cur.fetchall()
        for item in results:
            all_data.append(item)
        return all_data
        # print results[0][2]
        # print results
        # for item in results[0:1][0]:
        #     print item
        # results=[]
        # for row in cur:
        #     results.append(row)
        # return results  
def convert_to_datetime():
    pass

if __name__ == '__main__':
    # Set up the development server on port 5000.

    port = 5000
    app.debug = True
    app.run(port=port)
