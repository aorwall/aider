def verse(num):
    if num == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\n" \
               "Go to the store and buy some more, 99 bottles of beer on the wall."
    else:
        return f"{num} bottles of beer on the wall, {num} bottles of beer.\n" \
               "Take one down and pass it around, {next_num} bottles of beer on the wall.\n".format(
                   next_num=num - 1)


def recite(start, take=1):
    verses = [verse(i) for i in range(start, start-take-1, -1)]
    return "\n".join(verses)


if __name__ == '__main__':
    print(recite(99, 10))
