
class CanaryDictionary(object):

    def __init__(self):
        self.dictionary = {'millo': 'maiz',
                           'papa': 'patata',
                           'baifo': 'cabra',
                           'godo': 'miguel'}

    def search_word(self, word):
        return self.dictionary.get(word, None)
