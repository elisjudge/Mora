import config
import os
import utils.helper._exists as exists


files = [config.HIRAGANA_PAIRLIST_PATH,
        config.KATAKANA_PAIRLIST_PATH,
        config.PAIRLIST_STATS_PATH,
        config.MORA_COUNT_PATH,
        config.MORA_COUNT_STATS_PATH,
        config.MORA_COUNT_ERROR_PATH,
        config.MORA_COUNT_EXPRESSION_PATH,

        config.FREQ_OUT_PATH,
        config.MORA_PAIR_HIRAGANA,
        config.MORA_PAIR_KATAKANA,
        config.MORA_PAIR_STATS,
        config.MORA_PAIR_MIXED,
        config.MORA_PAIR_UNASSIGNED,
        config.MORA_PAIR_UNKNOWN,
        config.WORDPOOL_PATH]



for file in files:
    if exists.path_exists(file):
        os.remove(file)
