import re
import sys

def parse(gpxFName):
    coords = []
    with open(gpxFName, 'rU') as fpIn:
        for line in fpIn:
            if 'trkpt lat' in line:
                matches = re.search(r'.*lat=\"(.*\d+.\d+)\" lon=\"(.*\d+.\d+)\"', line)
                lat = float(matches.groups(0)[0])
                lon = float(matches.groups(0)[1])
                coords.append([lat, lon])
    return coords

def main():
    if len(sys.argv) < 2:
        print('Usage: %s gpxFName' % sys.argv[0])
        return
    
    coords = parse_gpx(sys.argv[1])
    print(coords)

if __name__ == "__main__":
    main()