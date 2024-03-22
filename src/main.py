import experiment.experiments as e
import utils.dictionary.wordpool as wordpool
import time


def main():
    if not wordpool.is_wordpool():
        wordpool.generate_wordpool()
    wordpool.generate_ranked_wordpools()
    e.run_experiment1()
    e.run_experiment2()
    e.preprocess_experiment3_data()
    e.run_experiment3()



if __name__ == "__main__":
    start_wall, start_cpu = time.perf_counter(), time.process_time()
    main()
    end_wall, end_cpu = time.perf_counter(), time.process_time()
    wall = end_wall - start_wall
    cpu = end_cpu - start_cpu
    print(f'Wall Time: {wall}')
    print(f'CPU Time: {cpu}')
