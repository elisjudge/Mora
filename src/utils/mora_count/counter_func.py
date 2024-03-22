import utils.helper._general as general
import utils.helper._readers as reader
import utils.helper._writers as writer
import config


def build_mora_count_stats()-> dict:
    """ Initialize the mora count stats"""
    stats_table = {
          'total': 0,
          'err': 0,
          'expr': 0
     }
    return stats_table


def build_mora_count_table()-> dict:
    """ Initialize the mora count table"""
    mora_count_table = {}
    return mora_count_table  


def build_mora_error_table()-> dict:
    """ Initialize error table"""
    mora_error_table = {'err': []}
    return mora_error_table  


def build_mora_expression_table()-> dict:
    """ Initialize the expressions table"""
    mora_expr_table = {'expr': []}
    return mora_expr_table  


def count_mora(text) -> int:
    """
    Counts number of mora in Japanese word. If any character
    is not hiragana or katakana. Returns zero.
    """
    mora_count = 0
    for c in text:
        if general.is_hiragana(c) and c not in ["ゃ","ゅ","ょ"]:
            mora_count += 1
        elif general.is_katakana(c) and c not in ["ャ","ュ","ョ",
                                          "ァ","ィ","ゥ",
                                          "ェ","ォ"]:
            mora_count += 1
        elif not general.is_katakana(c) and not general.is_hiragana(c):
            return 0
    return mora_count


def is_valid(mora_count) -> bool:
    """Helper function to write to main word pool"""
    if mora_count == "-1" or mora_count == "0":
        return False
    return True


def preprocess_line_and_count_mora(line:list) -> str:
    """ This will sort out erroneous dictionary entries and expressions from 
    legitimate words. Expressions refer to entries that do not have a kana field
    but also contain kanji. Entries that are non expressions that do not have a kana 
    field will be written using kana only e.g. loan words"""

    word_field = line[0]
    kana_field = line[1]
    if len(kana_field) == 0:
        if general.contains_kanji(word_field):
            
            mora_count = "-1"
        else:
            mora_count = str(count_mora(word_field))
    else:
        mora_count = str(count_mora(kana_field))
    return mora_count


def populate_mora_count_tables(line:list, mora_count_table:dict, mora_error:dict, mora_expr:dict,
                               stats_table:dict, mora_count:str):  
    """ Main function to write to mora count table"""
    word = line[0]
    kana = line[1]
    if mora_count in mora_count_table:
        mora_count_table[mora_count].append({'word': word, 'kana': kana})
        stats_table[mora_count] += 1
    elif mora_count == "0":
        mora_error['err'].append({'word': word, 'kana': kana})
        stats_table['err'] += 1
    elif mora_count == "-1":
        mora_expr['expr'].append({'word': word, 'kana': kana})
        stats_table['expr'] += 1
    elif mora_count not in mora_count_table:
        mora_count_table[mora_count] = []
        mora_count_table[mora_count].append({'word': word, 'kana': kana})
        stats_table[mora_count] = 1
    stats_table['total'] += 1


def write_mora_count_files(mora_count_table:dict, mora_stats:dict, errors:dict, expressions:dict):
    
    write_files = [(config.MORA_COUNT_PATH, mora_count_table), 
                    (config.MORA_COUNT_STATS_PATH, mora_stats),
                    (config.MORA_COUNT_ERROR_PATH, errors),
                    (config.MORA_COUNT_EXPRESSION_PATH, expressions),
                    ]
    for path, data in write_files:
            writer.write_file(path, data)
    
    for key in mora_count_table.keys():
        try:
            if int(key):
                    path = config.MORA_COUNT_COUNTS_PATH + f'{key}_mora.json'
                    writer.write_file(path, 
                                      mora_count_table[key])
        except ValueError:
            continue


def loaded_dictionary():
    return reader.read_json_lines(config.DICTIONARY_PATH)