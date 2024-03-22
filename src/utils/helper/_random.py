import random

def get_random_int(min_value, max_value):
    return random.randint(min_value, max_value)


def generate_random_trial_seeds(seed_number, n_trials = 100):
    random.seed(seed_number)
    range_start = 0
    range_end = n_trials + 1
    num_unique_numbers = n_trials
    return random.sample(range(range_start, range_end), num_unique_numbers)


def generate_random_word_seeds(seed_number, n_words):
    random.seed(seed_number)
    range_start = 0
    range_end = n_words
    num_unique_numbers = n_words
    return random.sample(range(range_start, range_end), num_unique_numbers)
    

