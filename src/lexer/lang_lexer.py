
import re
import sys

# ('for_loop', 
#   ('for_loop_setup', 
#       ('var_assign', 
#           'i', ('num', 0)
#       ), 
#       ('num', 15)), 
#   ('if_stmt', 
#       ('inf', 
#           ('var', 'i'), 
#           ('num', 2)), 
#               ('print', 
#                   ('string', '"salut"'))))

class Token():
    def __init__(self, _type, _value, _lineno, _index):
        self._type = _type
        self._value = _value
        self._lineno = _lineno
        self._index = _index

    def __repr__(self):
        return f'Token(type="{self._type}", value="{self._value}", lineno="{self._lineno}", index="{self._index}")'

class LangLexer():
    token_exprs = [
        (r'[ \t]+',                 None),
        (r'#[\n]*',                 None), # Comments
        (r'\n',                     'NEWLINE'), # New Line
        
        (r'<-',                     'SET'),
        (r';',                      'SEMICOL'),
        
        (r'\(',                     'LPAR'),
        (r'\)',                     'RPAR'),
        (r'\{',                     'LBRACE'),
        (r'\}',                     'RBRACE'),

        (r'\+',                     'PLUS'),
        (r'-',                      'MINUS'),
        (r'\*',                     'MUL'),
        (r'/',                      'DIV'),
        
        (r'<=',                     'INFEQ'),
        (r'<',                      'INF'),
        (r'>=',                     'SUPEQ'),
        (r'>',                      'SUP'),
        (r'!=',                     'NOTEQ'),
        (r'==',                     'EQEQ'),
        
        (r'et',                     'AND'),
        (r'ou',                     'OR'),
        (r'non',                    'NOT'),

        (r'Fin si',                 'ENDIF'),
        (r'Si',                     'IF'),
        (r'faire',                  'THEN'),
        (r'Sinon',                  'ELSE'),
        (r'Fin pour',               'ENDFOR'),
        (r'Pour',                   'FOR'),
        (r'jusqu\'a',               'TO'),
        (r'Fin',                    'END'),

        (r'afficher',               'PRINT'),
        (r'\".*?\"',                'STRING'),
        (r'[0-9]+',                 'INT'),
        (r'[A-Za-z][A-Za-z0-9_]*',  'ID'),
    ]

    def __init__(self, characters):
        self.characters = characters

    def lex(self, characters = None):
        if characters is None:
            characters = self.characters

        pos = 0
        linepos = 0
        noline = 0
        tokens = []

        while pos < len(characters):
            match = None
            for token_expr in LangLexer.token_exprs:
                pattern, tag = token_expr

                regex = re.compile(pattern)
                match = regex.match(characters, pos)

                if match:
                    text = match.group(0)
                    if tag:
                        if tag == 'NEWLINE':
                            noline += 1
                            linepos = 0
                            break

                        token = Token(_type=tag, _value=text, _lineno=noline, _index=linepos)
                        tokens.append(token)
                    break
                
            if not match:
                sys.stderr.write(f'Illegal character: {characters[pos]} at {linepos} line {noline}\\n')
                sys.exit(1)
            else:
                last_pos = pos
                pos = match.end(0)
                linepos += (pos - last_pos)

        return tokens
            