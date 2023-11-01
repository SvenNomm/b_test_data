import os
import json


def data_reader(file_name):
    print('Loading file: ', file_name)
    with open(file_name) as test_results_file:
        motion_data = json.load(test_results_file)

    return motion_data