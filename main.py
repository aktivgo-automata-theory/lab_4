import const
from grammar_checker import GrammarChecker

if __name__ == '__main__':
    grammar_checker = GrammarChecker(const.GRAMMAR)

    word = input("input word: ")

    print(grammar_checker.is_belongs_to_grammar(word))
