import experiment._experiment_func as ef
import config

def run_experiment1():
    """ This will load all available words at once and randomly select words to fill
    the mora pair lists for both wago and gairaigo based words"""
    wordpool = ef.load_wordpool()
    ef.generate_random_trial_seeds(config.N_TRIALS)
    n_words = ef.get_number_words()
    word_list_no = 1
    for seed in ef.load_trial_seeds():
        ef.generate_random_word_locations(seed, n_words)
        wago_pairlist, gairaigo_pairlist = ef.load_pairlists()
        result = ef.initialize_result_stats()
        print(f"{word_list_no}: ", end="")

        for word_location in ef.load_word_locations():
            ef.add_word_to_pairlist(str(word_location), wordpool, wago_pairlist, gairaigo_pairlist)
            if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
                break

        if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
            ef.generate_experiment_result(word_list_no, wago_pairlist, gairaigo_pairlist, result, experiment_no=1)
            print("Success")
        else:
            print("Uh oh, One of the lists didn't fill")
        
        word_list_no += 1

    #clean up
    ef.delete_word_location()

def run_experiment2():
    """ This experiement will be similar to experiment 1, but this time it will take
    from the ranked word pools first and will only extract unranked words if there are
    empty spaces in the mora pair list after all ranked words are exhausted."""
    ranked_wordpool = ef.load_ranked_wordpool()
    ef.generate_random_trial_seeds(config.N_TRIALS)
    n_words = ef.get_number_words()
    rank_n_words = ef.get_number_ranked_words()
    unranked_n_words = n_words - rank_n_words
    word_list_no = 1
    for seed in ef.load_trial_seeds():
        ef.generate_random_word_locations(seed, rank_n_words)
        wago_pairlist, gairaigo_pairlist = ef.load_pairlists()
        result = ef.initialize_result_stats()
        print(f"{word_list_no}: ", end="")

        for word_location in ef.load_word_locations():
                ef.add_word_to_pairlist(str(word_location), ranked_wordpool, wago_pairlist, gairaigo_pairlist)
                if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
                    break

        if not ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
            ef.generate_random_word_locations(seed, unranked_n_words)
            unranked_wordpool = ef.load_unranked_wordpool()
            for word_location in ef.load_word_locations():
                ef.add_word_to_pairlist(str(word_location), unranked_wordpool, wago_pairlist, gairaigo_pairlist)
                if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
                    break

        if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
            ef.generate_experiment_result(word_list_no, wago_pairlist, gairaigo_pairlist, result, experiment_no=2)
            print("Success")
        else:
            print("Uh oh, One of the lists didn't fill")
        word_list_no += 1


def preprocess_experiment3_data():
    ef.create_nth_pairlists()
    ef.create_nth_wordpools()


def run_experiment3():
    """ This experiement will be similar to experiment 2, but this time it will use shortened
    pair lists based on top nth percentile of mora pair appearance in word pool."""
    
    ranked_wordpool = ef.load_nth_ranked_wordpool()
    ef.generate_random_trial_seeds(config.N_TRIALS)
    n_words = ef.get_number_words()
    rank_n_words = ef.get_number_ranked_words()
    unranked_n_words = n_words - rank_n_words
    word_list_no = 1
    for seed in ef.load_trial_seeds():
        ef.generate_random_word_locations(seed, rank_n_words)
        wago_pairlist, gairaigo_pairlist = ef.load_nth_pairlists()
        result = ef.initialize_result_stats()
        print(f"{word_list_no}: ", end="")

        for word_location in ef.load_word_locations():
                ef.add_word_to_pairlist(str(word_location), ranked_wordpool, wago_pairlist, gairaigo_pairlist)
                if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
                    break

        if not ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
            unranked_wordpool = ef.load_nth_unranked_wordpool()
            ef.generate_random_word_locations(seed, unranked_n_words)
            for word_location in ef.load_word_locations():
                ef.add_word_to_pairlist(str(word_location), unranked_wordpool, wago_pairlist, gairaigo_pairlist)
                if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
                    break

        if ef.is_pairlists_full(wago_pairlist, gairaigo_pairlist):
            ef.generate_experiment_result(word_list_no, wago_pairlist, gairaigo_pairlist, result, experiment_no=3)
            print("Success")
        else:
            print("Uh oh, One of the lists didn't fill")
        word_list_no += 1
        
    

