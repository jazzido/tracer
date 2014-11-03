import csv, itertools, sys, uuid, os
from datetime import datetime, timedelta

from flask import Flask, render_template, request
from simplekml import Kml, Snippet, Types

app = Flask(__name__)

CATEGORICAL_COLORS = ['ff1f77b4','ffaec7e8','ffff7f0e','ffffbb78','ff2ca02c','ff98df8a','ffd62728','ffff9896','ff9467bd','ffc5b0d5','ff8c564b','ffc49c94','ffe377c2','fff7b6d2','ff7f7f7f','ffc7c7c7','ffbcbd22','ffdbdb8d','ff17becf','ff9edae5']

def format_date(d):
    return d.isoformat().split('.')[0]

def create_kml(start_dt, traces):
    mintime = datetime(2100,1,1)
    maxtime = datetime(1901,1,1)

    kml = Kml(name="Tracer")
    doc = kml.newdocument()

    fol = doc.newfolder(name="Traces")

    i = 0
    for id_, trace in traces:
        trace = list(trace)
        trk = fol.newgxtrack(name='Trace id: %s' % id_)

        times = [start_dt + timedelta(seconds=int(p['time'])) for p in trace]
        trk.newwhen([format_date(t) for t in times])

        places = [
            (float(p['lon']), float(p['lat']), 0)
            for p in trace
        ]
        trk.newgxcoord(places)

        mintime = min([mintime] + times)
        maxtime = max([maxtime] + times)

        trk.altitudemode = 'relativeToGround'

        trk.stylemap.normalstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
        trk.stylemap.normalstyle.linestyle.color = CATEGORICAL_COLORS[i % len(CATEGORICAL_COLORS)]
        trk.stylemap.normalstyle.linestyle.width = 6
        trk.stylemap.highlightstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
        trk.stylemap.highlightstyle.iconstyle.scale = 1.2
        trk.stylemap.highlightstyle.linestyle.color = CATEGORICAL_COLORS[i % len(CATEGORICAL_COLORS)]
        trk.stylemap.highlightstyle.linestyle.width = 8

        i += 1

    doc.lookat.gxtimespan.begin = format_date(mintime)
    doc.lookat.gxtimespan.end   = format_date(maxtime)

    #doc.lookat.longitude, doc.lookat.latitude = list(list(traces)[0][1])[0]

    return kml.kml()


def process_csv(uploaded_file, outfile, start_dt=None):
    if start_dt is None:
        start_dt = datetime.now()

    r = csv.DictReader(uploaded_file)
    records = list(r)

    g = itertools.groupby(sorted(records,
                                 key=lambda r: r.get('id')),
                          key=lambda r: r.get('id'))

    with open(outfile, 'w') as f:
        f.write(create_kml(start_dt, g))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kml', methods=['POST'])
def upload_kml():
    outfname = str(uuid.uuid1()) + '.kml'
    process_csv(request.files['file'],
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'static',
                             outfname))
    return outfname



if __name__ == '__main__':
    app.run(debug=True)
