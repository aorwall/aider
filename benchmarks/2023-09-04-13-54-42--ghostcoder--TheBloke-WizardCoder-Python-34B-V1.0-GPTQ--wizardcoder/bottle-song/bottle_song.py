def recite(start, take=10):
    lyrics = """{num} green bottles hanging on the wall,
{num} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {next_num} green bottles hanging on the wall.

{next_num} green bottles hanging on the wall,
{next_num} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {after_next_num} green bottles hanging on the wall."""

    output = ""
    current_bottle = start
    while take > 0:
        next_bottle = current_bottle - 1 if current_bottle > 1 else "no more"

        after_next_bottle = current_bottle - 2 if current_bottle > 2 else "no more"

        output += lyrics.format(num=current_bottle, next_num=next_bottle, after_next_num=after_next_bottle)
        output += "\n\n"

        current_bottle -= 1
        take -= 1

    return output[:-1] # remove last newline character