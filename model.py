# dependencies

import pandas as pd
import numpy as np

from sklearn.externals import joblib

lr = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')