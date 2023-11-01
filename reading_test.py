import os
import pickle as pkl

# path = 'C:/Users/Sven/Google Drive/Teaching/Machine_Learning_2023/practice_01/data_01/'
path = '/Users/svennomm/Library/CloudStorage/GoogleDrive-sven.nomm@gmail.com/My Drive/Teaching/Machine_Learning_2023/practice_01/data_01/'
fname = path + 'one_gaussian.pkl'
file_handle = open(fname, 'rb')
set_1 = pkl.load(file_handle)
print('hello')