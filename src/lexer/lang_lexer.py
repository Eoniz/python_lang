
import re
import sys

#
#
#class OldLexer(Lexer):
#    tokens = { NUMBER, ID, PRINT, STRING, IF, THEN, ELSE, FOR, FUN, TO, EQEQ}
#    ignore = ' \t'
#
#    literals = { '{', '}', '<', '>','=', '+', '-', '/', '*', '(', ')', ',', ';' }
#
#    # Define tokens
#    TO = r"jusqu'a"
#    STRING = r'\".*?\"'
#
#    EQEQ = r'=='
#
#    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
#    ID['Fonction'] = FUN
#    ID['Si'] = IF
#    ID['Sinon'] = ELSE
#    ID['Pour'] = FOR
#    ID['faire'] = THEN
#    ID['afficher'] = PRINT
#
#    def __init__(self):
#        self.nesting_level = 0
#
#    @_(r'\{')
#    def LBRACE(self, t):
#        t.type = '{'      # Set token type to the expected literal
#        self.nesting_level += 1
#        return t
#
#    @_(r'\}')
#    def RBRACE(self, t):
#        t.type = '}'      # Set token type to the expected literal
#        self.nesting_level -=1
#        return t
#
#    @_(r'\d+')
#    def NUMBER(self, t):
#        t.value = int(t.value)
#        return t
#
#    @_(r'#.*')
#    def COMMENT(self, t):
#        pass
#
#    @_(r'\n+')
#    def newline(self,t ):
#        self.lineno += t.value.count('\n')
#
#    def error(self, t):
#        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
#        self.index += 1
#    

#    ID['Fonction'] = FUN
#    ID['Si'] = IF
#    ID['Sinon'] = ELSE
#    ID['Pour'] = FOR
#    ID['faire'] = THEN
#    ID['afficher'] = PRINT

class Token():
    def __init__(self, _type, _value, _lineno, _index):
        self._type = _type
        self._value = _value
        self._lineno = _lineno
        self._index = _index

    def __repr__(self):
        return f"Token(type={self._type}, value={self._value}, lineno={self._lineno}, index={self._index})"

class LangLexer():
    RESERVED    = 'RESERVED'
    INT         = 'INT'
    ID          = 'ID'
    STRING      = 'STRING'  
    NEW_LINE    = 'NEW_LINE'

    token_exprs = [
        (r'[ \t]+',                 None),
        (r'#[\n]*',                 None), # Comments
        (r'\n',                  NEW_LINE), # New Line
        (r'\:=',                    RESERVED),
        (r'\(',                     RESERVED),
        (r'\)',                     RESERVED),
        (r'\{',                     RESERVED),
        (r'\}',                     RESERVED),
        (r';',                      RESERVED),
        (r'\+',                     RESERVED),
        (r'-',                      RESERVED),
        (r'\*',                     RESERVED),
        (r'/',                      RESERVED),
        (r'<=',                     RESERVED),
        (r'<',                      RESERVED),
        (r'>=',                     RESERVED),
        (r'>',                      RESERVED),
        (r'=',                      RESERVED),
        (r'!=',                     RESERVED),
        (r'==',                     RESERVED),
        (r'and',                    RESERVED),
        (r'or',                     RESERVED),
        (r'not',                    RESERVED),
        (r'Si',                     RESERVED),
        (r'faire',                  RESERVED),
        (r'Sinon',                  RESERVED),
        (r'Pour',                   RESERVED),
        (r'jusqu\'a',               RESERVED),
        (r'Fin',                    RESERVED),
        (r'\".*?\"',                STRING),
        (r'[0-9]+',                 INT),
        (r'[A-Za-z][A-Za-z0-9_]*',  ID),
    ]

    """
    Structure of a Token :
    (type='', value='', lineno='', index='')
    """

    def __init__(self, characters):
        self.characters = characters

    def lex(self, characters = None):
        if characters is None:
            characters = self.characters

        pos = 0
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
                        if tag == 'NEW_LINE':
                            noline += 1
                            pos = 0
                            break

                        token = Token(_type=tag, _value=text, _lineno=noline, _index=pos)
                        tokens.append(token)
                    break
                
            if not match:
                sys.stderr.write(f'Illegal character: {characters[pos]} at {pos} line {noline}\\n')
                sys.exit(1)
            else:
                pos = match.end(0)

        return tokens
            