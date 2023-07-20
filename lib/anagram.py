class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        anagram_list = []

        char_list = sorted([char for char in self.word])

        for anagram in anagrams:
            if char_list == sorted(anagram):
                anagram_list.append(anagram)
                
        return anagram_list

word = Anagram("listen")
result = word.match(["listen", "poison", "hello"])
print(result)
