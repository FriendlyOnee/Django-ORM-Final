from django import template
import string

register = template.Library()
CENSORED_WORDS = ['редиска',
                  'блять',
                  'ебать',
                  'бля']


@register.filter()
def curse_filter(string_to_check):
    checked_string = ''
    for word in string_to_check.split():
        for check_word in CENSORED_WORDS:
            if check_word in word.lower():
                last_chars = ''
                for char in reversed(word):
                    if char not in string.punctuation:
                        break
                    last_chars += char
                last_chars = last_chars[::-1]
                new_word = word[0] + (len(word.translate(str.maketrans('', '', string.punctuation))) - 1) * "*"
                checked_string += new_word + f"{last_chars} "
                break
        else:
            checked_string += word + " "
    return checked_string
