import pytest
from aux_functions import is_only_letters, has_no_duplicate_letter, does_not_end_with_s, \
                          word_to_list_of_bools


def test_is_only_letters():
    v = is_only_letters('apsodi')
    assert v == True

    v = is_only_letters('aps4odi')
    assert v == False

    v = is_only_letters('aps-odi')
    assert v == False

    v = is_only_letters('apsodi.')
    assert v == False

test_is_only_letters()


def test_has_no_duplicate_letter():
    v = has_no_duplicate_letter('abcdf')
    assert v == True

    v = has_no_duplicate_letter('abacdf')
    assert v == False

test_has_no_duplicate_letter()

def test_does_not_end_with_s():
    v = does_not_end_with_s('abcdf')
    assert v == True

    v = does_not_end_with_s('abcdfs')
    assert v == False

test_does_not_end_with_s()

def test_word_to_list_of_bools():
    b = word_to_list_of_bools('abcde')
    assert b == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

test_word_to_list_of_bools()