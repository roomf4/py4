# ch15.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#stacking

# Groups in the data may be visually stacked using the stack parameter:

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Bar(df, label='origin', values='mpg', agg='mean', stack='cyl',
        title="Avg MPG by ORIGIN, stacked by CYL", legend='top_right')

output_file("/tmp/ch15.html")

show(p)
