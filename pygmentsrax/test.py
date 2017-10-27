from lexer import RaxLexer

lx = RaxLexer()
print (list(lx.get_tokens('`print project [.#1*2] {1..10};')))
