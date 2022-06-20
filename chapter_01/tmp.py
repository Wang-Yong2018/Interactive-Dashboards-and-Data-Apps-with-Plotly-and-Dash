import pandas as pd
import math
import numpy as np
max_id = 27
df = pd.DataFrame(range(1, max_id+1), columns=['id'])



def get_entropy(x):
    entropy = 1/x * math.log(1/x, 2)
    return entropy


df['entropy'] = -df['id'].apply(lambda x: 1/ * math.log(1/27, 2))

print(df)
print(df.sum())