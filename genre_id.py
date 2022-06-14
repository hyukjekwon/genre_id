# Author: Hyuk-Je Kwon

import sys
import requests
import csv
import time

artist_column = 3
song_column = 1

# searches song and returns 1st result response
def search(query):
    link = 'https://itunes.apple.com/search?term={}&limit=1'.format(query.replace('.', '').replace(' ', '+'))
    resp = requests.get(link)
    print(link, resp)
    return resp.content.decode()

# returns num results
def results(resp):
    idx = resp.index('resultCount')
    return int(resp[idx:].split('"')[1].replace(',\n ', '')[1:])

# takes in response as string, spits out genre
def get_genre(resp):
    idx = resp.index('primaryGenreName')
    return resp[idx:].split('"')[2]

def make_new_csv(csvname):
    rows = []
    with open(csvname, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                rows.append(row)
                continue
            naptime = 1
            time.sleep(naptime)
            song = row[song_column]
            artist = row[artist_column]
            query = song + ' ' + artist
            resp = ''
            while not resp:
                time.sleep(naptime) # exponential backoff
                resp = search(query)
                naptime *= 2
            genre = get_genre(resp)
            row[7] = genre
            rows.append(row)

    with open('new_' + csvname, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

if '__main__' == __name__:
    flag = sys.argv[1]
    if flag == '-csv':
        csvname = sys.argv[2]
        make_new_csv(csvname)
    else:
        query = ' '.join([flag] + sys.argv[2:])
        resp = search(query)
        if results(resp) == 0:
            print('No results found. Try another query.')
        else:
            print(get_genre(resp))