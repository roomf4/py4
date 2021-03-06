# ch19.py

# ref: As with Bar charts, the color can also be given a column name,
# in which case the boxes are shaded automatically according to the
# group:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label='cyl', color='cyl',
            title="MPG Summary (grouped and shaded by CYL)")

output_file("/tmp/ch19.html")

show(p)
