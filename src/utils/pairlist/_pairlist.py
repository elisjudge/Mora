import config
import utils.helper._writers as writer

from utils.hiragana import _hiragana as h
from utils.katakana import _katakana as k


def create_pairlist():
    """ This will create the base pairlist files along with simple statistics"""
    hiragana_pairlist, h_pairlist_length = h.initialize_hiragana_pairlist_dictionary()
    writer.write_file(config.HIRAGANA_PAIRLIST_PATH, hiragana_pairlist)
    

    katakana_pairlist, k_pairlist_length = k.initialize_katakana_pairlist_dictionary()
    writer.write_file(config.KATAKANA_PAIRLIST_PATH, katakana_pairlist)
    

    pairlist_stats = {"hiragana": {"total": h_pairlist_length},
                          "katakana": {"total": k_pairlist_length}}
    writer.write_file(config.PAIRLIST_STATS_PATH, pairlist_stats)

