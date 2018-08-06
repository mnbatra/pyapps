from bokeh.plotting import figure, output_file, show
from motiondetector import df
from bokeh.models import DatetimeTickFormatter
from bokeh.models import HoverTool,ColumnDataSource

df["Startstr"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Endstr"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds =   ColumnDataSource(df)
htool = HoverTool(tooltips=[("Start","@Startstr"),("End","@Endstr")])
p = figure(height=200,width=1000, x_axis_type="datetime",title="Motion Graph")

p.add_tools(htool)
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1
q=p.quad(left="Startstr", right="Endstr", bottom=0, top=1, color = "green", source=cds)
output_file("rectangles.html")
show(p)
