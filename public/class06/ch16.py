# ch16.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#box-plots

# The BoxPlot can be used to summarize the statistical properties of
# different groups of data. The label specifies a column in the data
# to group by, and a box plot is generated for each group:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label='cyl',
            title="MPG Summary (grouped by CYL)")

output_file("boxplot.html")

show(p)


