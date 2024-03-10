import pandas as pd
import numpy as np
df = pd.read_csv('submission_kernel02.csv')

def recuperer_score_par_ID(id):
        df2 = df[df['SK_ID_CURR'] == id]
        list = df2['TARGET'].values.tolist()
        return list