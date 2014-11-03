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
