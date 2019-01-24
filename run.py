from src.lexer.lang_lexer import LangLexer

file = open('./exemples/basic/hello_world.lang')

data = file.read()

file.close()

lexer = LangLexer(data)
tokens = lexer.lex()
for token in tokens:
    print(token)