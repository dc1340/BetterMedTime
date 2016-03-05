#!/usr/bin/env python
import numpy as np
from bokeh.plotting import Figure
from bokeh.charts import Area
import scipy
from bokeh.models import ColumnDataSource, HBox, VBoxForm, ImageURL
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.io import curdoc
import pandas as pd
from bokeh.models import HoverTool, PanTool, BoxZoomTool, WheelZoomTool, ResetTool, PreviewSaveTool

# example data for an area plot
data = dict(
    drugA=[102, 103, 107, 125, 170, 200, 170, 125, 50, 0, 0, 0, 0, 0],
    drugB=[12, 33, 47, 15, 126, 121, 144, 233, 254, 225, 226, 267, 110, 130],
    drubC=[22, 43, 10, 25, 26, 101, 114, 203, 194, 215, 201, 227, 139, 160],
)

tools = [PanTool(), BoxZoomTool(), WheelZoomTool(), ResetTool(),
         HoverTool(), PreviewSaveTool()]
p = Figure(plot_height=500, plot_width=500,
           tools=tools, x_range=[0, 24])  # x_range=[0, 4*np.pi], y_range=[-2.5, 2.5]
p.grid.grid_line_alpha = 0
area = Area(data, legend='top_left', title="Plasma Concentration over Time", xlabel="Time", ylabel="Concentration")
