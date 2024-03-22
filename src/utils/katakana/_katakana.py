import utils.katakana._standard as ks
import utils.katakana._standard_choon as ksc
import utils.katakana._standard_yoon as ksy
import utils.katakana._diacritic as kd
import utils.katakana._diacritic_choon as kdc
import utils.katakana._diacritic_yoon as kdy
import utils.katakana._foreign_sounds as kfs
import utils.katakana._foreign_sound_choon as kfsc

from itertools import product


def get_katakana_list():
    """ builds list of valid katakana mora including long vowels """
    return (ks.get_standard_characters() + ksc.get_standard_choon() +
            ksy.get_standard_yoon() + kd.get_diacritic() +
            kdy.get_diacritic_yoon() + kdc.get_diacritic_choon()
            + kfs.get_foreign_sounds() + kfsc.get_foreign_choon_sounds())


def create_katakana_pairlist(n_pairs:int = 2):
    """ creates every possible combination of katakana mora and long vowels """
    katakana_list = get_katakana_list()
    combination_katakana_list = ["".join(combination) for combination in list(product(katakana_list,
                                            repeat=n_pairs))]
    return combination_katakana_list


def read_pairlist(pairlist):
    for pair in pairlist:
        yield pair


def initialize_katakana_pairlist_dictionary():
    katakana_pairlist = {}
    pairlist = create_katakana_pairlist()
    pairlist_length = 0
    for pair in read_pairlist(pairlist):
        if pair not in katakana_pairlist:
            katakana_pairlist[pair] = {'count': 0, 'words': []}
            pairlist_length+=1
            
    return katakana_pairlist, pairlist_length