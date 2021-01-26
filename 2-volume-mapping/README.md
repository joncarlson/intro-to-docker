Uses the mEditor API to retrieve one or more collections

### Usage

* Create a text file in the `data` directory
* Add one or more collection entry IDs, one per line
* Build the docker image: `docker build -t volume-mapping ./`
* Run using the command: `docker run -e MEDITOR_API_URL={PATH_TO_MEDITOR_API} -v "$PWD/data:/data" volume-mapping`
