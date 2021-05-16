# Try to figure out meaning of 'origin'
import pandas as pd
import numpy as np

cars = pd.read_csv(
    'https://s3-us-west-2.amazonaws.com/learn-assets.galvanize.com/gSchool/ds-curriculum/precourse/autos_mpg.csv')

print(cars['origin'].value_counts())

# 1    249
# 3     79
# 2     70

cars_origin = cars.groupby('origin')
# three_origin = cars_origin.filter(lambda x: x == 3)
print(cars.loc[cars['origin'] == 3])

# for name, group in cars_origin.loc('origin'=3):
#     print(name)
#     print(group)
