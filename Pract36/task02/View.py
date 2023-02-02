def display_album(album):
    print(f'{album.year} - {album.title}')


def display_artist(artist):
    print(f'{artist.title}: ')
    for num, album in enumerate(artist.albums, 1):
        print(num, end=". ")
        display_album(album)


def display_artists(artists):
    print(f'Groups: ')
    for num, artist in enumerate(artists, 1):
        print(f'{num}. {artist.title}')


def display_menu(titles):
    for number, title in enumerate(titles, 1):
        print(f'{number}. {title}', end=" ")


def get_int_query(desc=None):
    query = input(f'{desc}: ')
    return query if query.isdigit() else False


def get_str_query(desc=None):
    query = input(f'{desc}: ')
    return query if query != '' else False
