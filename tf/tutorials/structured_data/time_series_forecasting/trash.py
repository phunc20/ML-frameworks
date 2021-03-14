"""
### Wind velocity
One thing that should stand out is the `min` value of columns `wv (m/s)` and `max. wv (m/s)`. This `-9999` is
likely erroneous. There's a separate wind direction column (`wd (deg)`), so the velocity should be `>=0`.
Replace it with zero.


## Inspect and Cleanup
Statistics.


`subplots=False` will plot all three curves in the same plot.



**(!1)** There is some problem: `df = df[5::6]` was correct logic, but unluckily the CSV file has missing
data. You could propose another way to try to extract the right data with the right time.


This tutorial will just deal with **hourly predictions**, so start by **sub-sampling** the data from 10 minute intervals to 1h:


"""


import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras

plt.style.use("dark_background")
mpl.rcParams.keys("figure.facecolor") = "k"

def set_default(figsize=(10, 10), dpi=100):
    plt.style.use(['dark_background', 'bmh'])
    plt.rc('axes', facecolor='k')
    plt.rc('figure', facecolor='k')
    plt.rc('figure', figsize=figsize, dpi=dpi)



mpl.rcParams["axes.edgecolor"] = "w"
mpl.rcParams["axes.facecolor"] = "w"
mpl.rcParams["ytick.color"] = "w"
mpl.rcParams["xtick.color"] = "w"
#mpl.rcParams["grid.color"] = "w"
#mpl.rcParams["grid.color"] = "w"
#mpl.rcParams["axes.titlecolor"] = "w"
#mpl.rcParams["axes.labelcolor"] = "w"
mpl.rcParams["text.color"] = "w"
mpl.rcParams["figure.figsize"] = (8,6)
mpl.rcParams["axes.grid"] = False

zip_path = keras.utils.get_file(
    origin="https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip",
    fname="jena_climate_2009_2016.csv.zip",
    extract=True,
)
zip_path

csv_path, _ = os.path.splitext(zip_path)


zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)

# Let's get the file path to jena_climate_2009_2016.csv, i.e. without the .zip
# Besides, let's remove the .zip file
csv_path, _ = os.path.splitext(zip_path)
!rm {zip_path}
csv_path

import pandas as pd
df = pd.read_csv(csv_path)
df.head()

# slice [start:stop:step], starting from index 5 take every 6th record.
df = df[5::6]
date_time = pd.to_datetime(df.pop("Date Time"), format="%d.%m.%Y %H:%M:%S")
df

plot_cols = ["T (degC)", "p (mbar)", "rho (g/m**3)"]
plot_features = df[plot_cols]
plot_features.index = date_time
_ = plot_features.plot(subplots=True)

## Take a closer look
n_first = 480
plot_features = df[plot_cols][:n_first]
plot_features.index = date_time[:n_first]
_ = plot_features.plot(subplots=True)

wv = df["wv (m/s)"]
bad_wv = wv < 0.0
wv[bad_wv] = 0.0

max_wv = df["max. wv (m/s)"]
bad_max_wv = max_wv < 0.0
max_wv[bad_max_wv] = 0.0

df["wv (m/s)"].min(), df["max. wv (m/s)"].min()



