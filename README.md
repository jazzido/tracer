# Tracer

Given a CSV with columns

  - `id` (unique identifier of the vehicle)
  - `time` (timestamp in seconds)
  - `lon` (longitude)
  - `latitude` (latitude)

Generates a KML containing [`gx:track`](https://developers.google.com/kml/documentation/kmlreference#gxtrack) elements.

## Installation

Install the requirements listed in `requirements.txt` with `pip install -r requirements.txt`

## Running as a web application

```
python tracer.py
```

Then, go to http://localhost:5000

## Running as a command line application

```
python csv2kml.py input.csv output.kml
```

## License

© 2014 Manuel Aristarán. Distributed under the terms of the MIT License

Developed as part of the requirements for [MIT course 1.204 "Computer Modeling: Human Mobility and Networks"](https://stellar.mit.edu/S/course/1/fa14/1.204/index.html)
