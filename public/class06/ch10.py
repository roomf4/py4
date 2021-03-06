# ch10.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#bar-charts

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Bar(df, 'cyl', values='mpg', title="Total MPG by CYL")

output_file("/tmp/ch10.html")

show(p)
