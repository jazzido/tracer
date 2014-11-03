import sys

from tracer import process_csv

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >>sys.stderr, "Usage: %s <input.csv> <output.kml>" % sys.argv[0]
        exit(1)

    with open(sys.argv[1], 'r') as f:
        process_csv(f, sys.argv[2])
