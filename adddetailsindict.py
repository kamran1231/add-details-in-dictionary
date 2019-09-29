

dict1 = {}

name = input('enter the name: ')
age = int(input('enter the age: '))
fav_movie = input('enter your fav movies: ').split(',')
fav_songs = input('enter your fav songs: ').split(',')

dict1['name'] = name
dict1['age'] = age
dict1['fav_movie'] = fav_movie
dict1['fav_songs'] = fav_songs

for key,value in dict1.items():
    print(f'{key} : {value}')