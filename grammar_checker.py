import const


class GrammarChecker:

    def __init__(self, grammar: dict):
        self.grammar = grammar

    def __get_entry(self, word: str):
        for i in range(len(word)):
            j = i
            while j <= len(word) and word[i:j] not in self.grammar:
                j += 1
            if j != len(word) + 1:
                return i, j

        return -1, -1

    def is_belongs_to_grammar(self, word: str):
        while word != const.ZERO_CHAR:
            print(word)
            i, j = self.__get_entry(word)
            if i == -1 or j == -1:
                return False
            word = word[:i] + self.grammar[word[i:j]] + word[j:]

        print(word)
        return True
