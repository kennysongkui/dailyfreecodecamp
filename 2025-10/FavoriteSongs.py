'''
Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).
'''

def favorite_songs(playlist):
    new_arr = sorted(playlist, key=lambda x: x['plays'], reverse=True)
    songs = []
    for song in new_arr[:2]:
        songs.append(song['title'])

    # print(new_arr[0]['plays'])
    # print(new_arr)
    # print(type(new_arr))
    # print(songs)
    playlist = songs[:]


    return playlist

t = favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])
print(t)
