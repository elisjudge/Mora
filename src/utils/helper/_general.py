import re

def contains_kanji(input_string:str) -> bool:
    """Will check an entire string of text and return True if the string contains ANY kanji"""
    kanji_pattern = re.compile(r'[\u4e00-\u9faf]')
    match = kanji_pattern.search(input_string)
    return bool(match)

          
def is_hiragana(character:str) -> bool:
    """Will check a character and return True if it is hiragana."""
    hiragana_pattern = re.compile(r'^[\u3041-\u3096]+$')
    return bool(hiragana_pattern.match(character))


def is_katakana(character:str) -> bool:
    """Will check a character and return True if it is katakana."""
    katakana_pattern = re.compile(r'^[\u30A1-\u30FC]+$')
    return bool(katakana_pattern.match(character))