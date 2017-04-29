
from canarydictionary import CanaryDictionary


def test_dictionary():
    dictionary = CanaryDictionary()
    millo = dictionary.search_word('millo')
    assert millo == 'maiz'
    papa = dictionary.search_word('papa')
    assert papa == 'patata'
    baifo = dictionary.search_word('baifo')
    assert baifo == 'cabra'
    godo = dictionary.search_word('godo')
    assert godo == 'miguel'
    guagua = dictionary.search_word('guagua')
    assert guagua == 'autobus'


def test_nodictionary():
    dictionary = CanaryDictionary()
    noword = dictionary.search_word('noword')
    assert noword is None
