import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word


# @pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected


#tests authored by Lauren below

def test_single_word():
    actual= first_repeated_word("hello")
    expected = None
    assert actual == expected

def test_multiple_repeats():
    actual = first_repeated_word("cat dog cat dog")
    expected = "cat"
    assert actual == expected

def test_long_sentence():
    actual = first_repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = "it"
    assert actual == expected

def test_my_smallest_meaningful_example():
    actual = first_repeated_word("the cat and the dog")
    expected = "the"
    assert actual == expected

def test_special_characters():
    actual = first_repeated_word("!!!?!#@$$%$&^*(){}[]!!!??")
    expected = None
    assert actual == expected

def test_immediate_repeat():
    actual = first_repeated_word("June June July July")
    expected = "june"
    assert actual == expected
