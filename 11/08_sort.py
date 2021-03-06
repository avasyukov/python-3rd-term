import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.1,
                    'B': pd.Timestamp('20200901'),
                    'C': pd.Series(1, index=list(range(4)), dtype=np.float32),
                    'D': 42 * np.arange(4),
                    'E': 'foo'})
print(df)
print("=================")
print(df.sort_values(by='D', ascending=False))
print("=================")
print(df.loc[df['D'] > 42].sort_values(by='D', ascending=True))
