import unittest

import const
from grammar_checker import GrammarChecker


class TestGrammarChecker(unittest.TestCase):
    def setUp(self):
        self.grammar_checker = GrammarChecker(const.GRAMMAR)

    def test_in_grammar_1(self):
        self.assertEqual(True, self.grammar_checker.is_belongs_to_grammar('abba⊥'))

    def test_in_grammar_2(self):
        self.assertEqual(True, self.grammar_checker.is_belongs_to_grammar('ab⊥'))

    def test_not_in_grammar_1(self):
        self.assertEqual(False, self.grammar_checker.is_belongs_to_grammar('abe⊥'))

    def test_not_in_grammar_2(self):
        self.assertEqual(False, self.grammar_checker.is_belongs_to_grammar('a⊥'))

    def test_not_in_grammar_3(self):
        self.assertEqual(False, self.grammar_checker.is_belongs_to_grammar('b'))


if __name__ == '__main__':
    unittest.main()
