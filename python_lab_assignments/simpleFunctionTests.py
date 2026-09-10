# Name: Yashvi Himanshu Gaglani

from simpleFunctions import euclid, isbn


def test_euclid_1():
    assert euclid(48, 18) == 6


def test_euclid_2():
    assert euclid(17, 5) == 1


def test_euclid_3():
    assert euclid(1, 5) == 1


def test_euclid_4():
    assert euclid(5, 1) == 1


def test_euclid_5():
    assert euclid(7, 7) == 7


def test_isbn_1():
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2]) is True


def test_isbn_2():
    assert isbn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is True


def test_isbn_3():
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 3]) is False


def test_isbn_4():
    assert isbn([1, 2, 3, 4, 5, 6, 7, 8, 9]) is False


def test_isbn_5():
    assert isbn([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) is False
