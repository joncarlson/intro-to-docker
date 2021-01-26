import os
import requests
import json
import sys

DIRECTORY = './data'
MODEL = 'Collection Metadata'
APIURL = os.environ.get('MEDITOR_API_URL')
EXTENSIONS = ('.txt')

def main():
    collections = getCollectionsFromDataFiles()

    if len(collections) == 0:
        sys.exit('No collections found!')

    for collection in collections:
        params = {
            'model': MODEL,
            'title': collection,
        }

        print('Retrieving ' + collection + ' from mEditor')

        request = requests.get(url = APIURL + '/getDocument', params = params)
        filename = DIRECTORY + '/' + collection + '.json'

        with open(filename, 'w') as file:
            json.dump(request.json(), file, indent=2)
            print('Created file: ' + filename)

def getCollectionsFromDataFiles():
    collections = []  

    for subdir, dirs, files in os.walk(DIRECTORY):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext != '' and ext in EXTENSIONS:
                file = open(os.path.join(subdir, file), 'r')
                collections.extend(file.read().splitlines())

    return collections 

if __name__ == "__main__":
    main()