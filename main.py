# this is the main file for brasialia data experiment

import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import json
import numpy as np


path = '/Users/svennomm/kohalikTree/Data/MotorFunctionsAnalysis/2022_05_Jaguarao3Tablet/'
path_add = 'tablet_22017/'

path_reference_images = '/Users/svennomm/kohalikTree/Data/MotorFunctionsAnalysis/ref_imgs/'
ref_file_name = path_reference_images + 'honey.png'
#ref_file_name = path_reference_images + 'cuboid.png'
img = mpimg.imread(ref_file_name)

file_name = path + path_add + '20220505-210915-Neusa 22017-hexagon-MS.json'
print(os.path.getsize(file_name))

#file_name = path + path_add + ''
#with open(file_name) as f:
#    d = json.load(f)
#data = d['data']

with open(file_name, 'r') as f:
    data = json.load(f)

keys = data.keys()
drawing = data['data']
erasing = data['erasedStrokes']
#stroke = drawing[0][0]

test_data_frame = pd.DataFrame()

for i in drawing:
    stroke = pd.DataFrame(i)
    test_data_frame = pd.concat([test_data_frame, stroke])


#fig = plt.subplots()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#imgplot = plt.imshow(img)
ax.scatter(test_data_frame['x'], test_data_frame['y'], test_data_frame['t'])
#imgplot = plt.imshow(img)
plt.show()

fig = plt.subplots()
imgplot = plt.imshow(img)
plt.scatter(test_data_frame['x'], test_data_frame['y'])
plt.show()

print("That's all folks!!!")