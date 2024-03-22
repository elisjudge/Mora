import utils.hiragana._standard as hs
import utils.hiragana._standard_choon as hsc
import utils.hiragana._standard_yoon as hsy
import utils.hiragana._diacritic as hd
import utils.hiragana._diacritic_choon as hdc
import utils.hiragana._diacritic_yoon as hdy

from itertools import product


def get_hiragana_list():
    """ builds list of valid hiragana mora including long vowels """
    return (hs.get_standard_characters() + hsc.get_standard_choon() +
            hsy.get_standard_yoon() + hd.get_diacritic() +
            hdy.get_diacritic_yoon() + hdc.get_diacritic_choon())


def create_hiragana_pairlist(n_pairs:int = 2):
    """ creates every possible combination of hiragana mora and long vowels """
    hiragana_list = get_hiragana_list()
    combination_hiragana_list = ["".join(combination) for combination in list(product(hiragana_list, 
                                            repeat=n_pairs))]
    return combination_hiragana_list
    

def read_pairlist(pairlist):
    for pair in pairlist:
        yield pair


def initialize_hiragana_pairlist_dictionary():
    hiragana_pairlist = {}
    pairlist = create_hiragana_pairlist()
    pairlist_length = 0
    for pair in read_pairlist(pairlist):
        if pair not in hiragana_pairlist:
            hiragana_pairlist[pair] = {'count': 0, 'words': []}
            pairlist_length+=1


    return hiragana_pairlist, pairlist_length


