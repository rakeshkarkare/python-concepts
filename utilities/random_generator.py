import random
import string
from translate import Translator
from random_word import RandomWords


def random_string(string_length):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


def random_words():
    r = RandomWords()
    return r.get_random_word()


def translate_text_in_arabic(data):
    translator = Translator(from_lang="english", to_lang="arabic")
    arabic_text = translator.translate(data)
    return arabic_text
