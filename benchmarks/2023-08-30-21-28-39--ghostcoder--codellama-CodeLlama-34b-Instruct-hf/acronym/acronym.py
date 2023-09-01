def abbreviate(words):
    return ''.join([word[0] for word in words.split()])

def test_consecutive_delimiters(self):
    self.assertEqual(abbreviate("Something - I made up from thin air"), "SIMUFTA")

def test_lowercase_words(self):
    self.assertEqual(abbreviate("Ruby on Rails"), "ROR")

def test_punctuation_without_whitespace(self):
    self.assertEqual(abbreviate("Complementary metal-oxide semiconductor"), "CMOS")

def test_underscore_emphasis(self):
    self.assertEqual(abbreviate("The Road _Not_ Taken"), "TRNT")
