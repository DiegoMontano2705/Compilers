# pip install antlr4-python3-runtime
# antlr4 -Dlanguage=Python2 LittleDuckGrammar.g4
# Diego Fernando Montaño Pérez

import sys
from antlr4 import *
from LittleDuckGrammarLexer import LittleDuckGrammarLexer
from LittleDuckGrammarParser import LittleDuckGrammarParser

class MyGrammarListener(ParseTreeListener):
    def enterKey(self, ctx):
        pass
    def exitKey(self, ctx):
        pass
    def enterValue(self, ctx):
        pass
    def exitValue(self, ctx):
        pass

class KeyPrinter(MyGrammarListener):     
    def exitKey(self, ctx):         
        print("Oh, a key!") 

def main():
    #Open test file
    namef = "HW3/ANTLR4_LittleDuck/fail.txt"

    input_stream = FileStream(namef)
    lexer = LittleDuckGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LittleDuckGrammarParser(stream)
    tree = parser.program()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main()