# ch25.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#histograms

# It can also be used by passing in a Pandas Dataframe as the first
# argument, and specifying the name of the column to use for the
# data. The column name can be provided as the second positional
# argument:

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Histogram(df, 'hp', title="HP Distribution")

output_file("/tmp/ch25.html",)

show(p)
