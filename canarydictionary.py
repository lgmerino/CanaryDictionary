
class CanaryDictionary(object):

    def __init__(self):
        self.dictionary = {'millo': 'maiz',
                           'papa': 'patata',
                           'baifo': 'cabra',
                           'godo': 'miguel',
                           'guagua': 'autobus'}

    def search_word(self, word):
        return self.dictionary.get(word, None)
