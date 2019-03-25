
class TextTools:

    # counts the vowels in a body of text
    @staticmethod
    def vowel_counter(text_in):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_counter = 0
        for char in text_in:
            if vowels.__contains__(str(char).lower()):
                vowel_counter += 1
        return vowel_counter

    # counts the words in a body of text

    @staticmethod
    def word_counter(text_in):
