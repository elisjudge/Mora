import utils.mora_count.counter_func as cf

def mora_counter(): 
    mora_count_table = cf.build_mora_count_table()
    mora_stats = cf.build_mora_count_stats()
    errors = cf.build_mora_error_table()
    expressions = cf.build_mora_expression_table()
    
    for line in cf.loaded_dictionary():
                    mora_count = cf.preprocess_line_and_count_mora(line)
                    cf.populate_mora_count_tables(line,
                                                mora_count_table,
                                                errors,
                                                expressions,
                                                mora_stats,
                                                mora_count)                           
                    
    cf.write_mora_count_files(mora_count_table,mora_stats,errors,expressions)

    