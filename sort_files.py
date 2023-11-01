# this code sorts files to the folders corresponding to the different tests

import os
import shutil
from name_eriser import name_eriser


path = '/Users/svennomm/Downloads/Tablet_andmed_2022_12_02/'
test_names = ['plines', 'Letters_a_big', 'Letters_a_small', 'Letters_k_big', 'Letters_k_small', 'Letters_s_big',
              'Letters_s_small', 'spiral', 'plcontinue', 'pltrace', 'poppelreuter1_bowl', 'poppelreuter1_thing',
              'poppelreuter2_axe', 'poppelreuter2_thing', 'multicube', 'signature', 'name','hexagon']


#destination_path = '/Users/svennomm/kohalikTree/Data/MotorFunctionsAnalysis/brasil_processed_Dec_2022/' # this should exist before running the code.


destination_path = '/Users/svennomm/kohalikTree/Data/MotorFunctionsAnalysis/brasil_22_processed_Oct_2023/'
for name in test_names:
    if not os.path.isdir(destination_path + name):
        os.makedirs(destination_path + name)


recorded_folders = os.listdir(path)
for folder_name in recorded_folders:
    if os.path.isdir(path + folder_name):
        folder_content = os.listdir(path + folder_name)
        for file_name in folder_content:
            if os.path.isfile(path + folder_name + '/' + file_name):
                for name in test_names:
                    if name in file_name:
                        new_name = name_eriser(file_name)
                        #shutil.copy(path + folder_name + '/' + file_name, destination_path + name + '/')
                        shutil.copyfile(path + folder_name + '/' + file_name, destination_path + name + '/' + new_name)
                        print('Hello')

