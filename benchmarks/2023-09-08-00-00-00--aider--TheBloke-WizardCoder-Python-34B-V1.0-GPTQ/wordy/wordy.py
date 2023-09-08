def answer(question):
    try:
        words = question.split()
        result = 0
        sign = '+'
        for word in words:
            if word in ['plus', 'minus', 'multiplied', 'divided']:
                sign = word
            elif word.isdigit():
                if sign == 'plus':
                    result += int(word)
                elif sign == 'minus':
                    result -= int(word)
                elif sign == 'multiplied':
                    result *= int(word)
                elif sign == 'divided':
                    result /= int(word)
            else:
                raise InvalidSyntaxError("syntax error")
        return result
    except InvalidSyntaxError as e:
        raise e
    except Exception as e:
        raise ValueError("unknown operation")

# Exception messages
class WordProblemError(Exception):
    pass

class UnsupportedOperationError(WordProblemError):
    pass

class InvalidSyntaxError(WordProblemError):
    pass
