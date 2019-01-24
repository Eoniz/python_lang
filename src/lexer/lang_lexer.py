import sys
import re

RESERVED    = 'RESERVED'
INT         = 'INT'
ID          = 'ID'
STRING      = 'STRING'

token_exprs = [
    (r'[ \n\t]+',               None),
    (r'#[^\n]*',                None),

    (r'\=',                     RESERVED),
    (r'\(',                     RESERVED),
    (r'\)',                     RESERVED),
    (r'\+',                     RESERVED),
    (r'\-',                     RESERVED),
    (r'\*',                     RESERVED),
    (r'/',                      RESERVED),
    (r'<=',                     RESERVED),
    (r'>=',                     RESERVED),
    (r'<',                      RESERVED),
    (r'>',                      RESERVED),
    (r'=',                      RESERVED),
    (r'!=',                     RESERVED),
    (r'and',                    RESERVED),
    (r'or',                     RESERVED),
    (r'not',                    RESERVED),
    (r'if',                     RESERVED),
    (r'then',                   RESERVED),
    (r'else',                   RESERVED),
    (r'while',                  RESERVED),
    (r'do',                     RESERVED),
    (r'end',                    RESERVED),

    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',  ID),
    (r'\"(.*?)\"',              STRING),
]

def lex(characters, token_exprs):
    pos = 0
    tokens = []

    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write(f'Illegal character: {characters[pos]} \n')
            sys.exit(1)
        else:
            pos = match.end(0)
        
    return tokens

def imp_lex(characters):
    return lex(characters, token_exprs)