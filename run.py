from src.lexer.lang_lexer import *

def open_file(filename):
    _file = open(filename, 'r')
    data = _file.read()
    _file.close()

    return data


def run():
    data = open_file(sys.argv[1])

    tokens = imp_lex(data)

    for token in tokens:
        print(token)

run()