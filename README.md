# genre_id
A script that uses Itunes' response API to return the genre of any given song.

# requirements
You will need the ```requests``` library for this script to work.
```
pip install requests
```

# usage
### To get the genre of multiple songs in a spreadsheet:

```
python3 genre_id.py -csv yourcsv.csv
```
Assuming all of the songs exist on Itunes, it should create a new csv file containing the genres of each song.
You may need to change the columns for where you have songs/artists/genres stored. You will need to edit these manually(see lines 8-10).

### To get the genre of a single song:

```
python3 genre_id.py query
```

The query can be anything you would use to look for the song. I would personally recommend making it song + artist for best results.

i.e.
```
python3 genre_id.py industry baby lil nas x
```
The response: 
```
https://itunes.apple.com/search?term=industry+baby+lil+nas+x&limit=1 <Response [200]>
Hip-Hop/Rap
```
# contact
Email me for any questions: hyukjekwon@umass.edu
