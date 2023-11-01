import pandas as pd
import numpy as np


def get_dataframe(motion_data):
    motion_data_frame = pd.DataFrame()
    stroke_nr = 0
    for j in motion_data['data']:
        stroke = pd.DataFrame(j)
        stroke['stroke_nr'] = pd.Series([stroke_nr for x in range(len(stroke.index))], dtype='float64')
        stroke_nr =+ 1
        #print(stroke)
        #motion_data_frame = motion_data_frame.append(stroke)
        motion_data_frame = pd.concat([motion_data_frame, stroke])

    return motion_data_frame
