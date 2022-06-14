# genre_id
A script that uses Itunes' response API to return the genre of any given song.

# requirements
You will need the ```requests``` library for this script to work.
```
pip install requests
```

# usage
To get the genre of multiple songs in a spreadsheet:

```
python3 genre_id -csv yourcsv.py
```

To get the genre of a single song:

```
python3 genre_id query
```

The query can be anything you would use to look for the song. I would personally recommend making it song + artist for best results.

i.e.
```
python3 genre_id industry baby lil nas x
```
# contact
Email me for any questions: hyukjekwon@umass.edu
