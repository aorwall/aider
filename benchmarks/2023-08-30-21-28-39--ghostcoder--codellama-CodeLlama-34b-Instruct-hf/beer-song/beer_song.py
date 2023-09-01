def recite(start, take=1):
    verses = []
    for i in range(start, start-take, -1):
        verses.append(verse(i))
    return verses


def verse(bottles):
    if bottles == 0:
        return 'No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.'
    elif bottles == 1:
        return '1 bottle of beer on the wall, 1 bottle of beer. Take it down and pass it around, no more bottles of beer on the wall.'
    elif bottles > 1:
        return f'{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, {bottles-1} bottles of beer on the wall.'
