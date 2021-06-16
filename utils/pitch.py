#import bokeh
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn


def draw_pitch(figure_width=700,
               figure_height=350,
               pitch_width=104,
               pitch_height=68,
               pitch_color="#B3DE69",
               line_color="grey"):

    p = figure(width=figure_width,
               height=figure_height,
               toolbar_location="below")

    #Empty pitch
    p.rect(x=pitch_width / 2.,
           y=pitch_height / 2.,
           width=pitch_width,
           height=pitch_height,
           fill_color=pitch_color,
           line_width=2,
           line_color=line_color)

    #Penalty Area Left
    p.circle(16.5,
             pitch_height / 2.,
             size=50,
             fill_color=pitch_color,
             line_width=2,
             line_color=line_color)
    ##Big rectangle
    p.rect(x=16.5 / 2.,
           y=pitch_height / 2.,
           width=16.5,
           height=40.3,
           fill_color=pitch_color,
           line_width=2,
           line_color=line_color)
    ##Small rectangle
    p.rect(x=5.5 / 2.,
           y=pitch_height / 2.,
           width=5.5,
           height=18.3,
           fill_color=pitch_color,
           line_width=2,
           line_color=line_color)
    ##Goal post
    p.rect(x=0,
           y=pitch_height / 2.,
           width=0.5,
           height=7.3,
           fill_color=line_color,
           line_width=2,
           line_color=line_color)
    ##Penalty spot
    p.circle(11,
             pitch_height / 2.,
             size=2,
             fill_color=line_color,
             line_width=2,
             line_color=line_color)

    #Penalty Area right
    p.circle((pitch_width - 16.5),
             pitch_height / 2.,
             size=50,
             fill_color=pitch_color,
             line_width=2,
             line_color=line_color)
    p.rect(x=pitch_width - (16.5 / 2.),
           y=pitch_height / 2.,
           width=16.5,
           height=40.3,
           fill_color=pitch_color,
           line_width=2,
           line_color=line_color)
    ##Small rectangle
    p.rect(x=pitch_width - (5.5 / 2.),
           y=pitch_height / 2.,
           width=5.5,
           height=18.3,
           fill_color=pitch_color,
           line_width=2,
           line_color=line_color)
    ##Goal post
    p.rect(x=pitch_width,
           y=pitch_height / 2.,
           width=0.5,
           height=7.3,
           fill_color=line_color,
           line_width=2,
           line_color=line_color)
    ##Penalty spot
    p.circle((pitch_width - 11),
             pitch_height / 2.,
             size=2,
             fill_color=line_color,
             line_width=2,
             line_color=line_color)

    #middle of pitch
    p.circle(pitch_width / 2.,
             y=pitch_height / 2.,
             size=100,
             fill_color=pitch_color,
             line_width=2,
             line_color=line_color)
    p.circle(pitch_width / 2.,
             y=pitch_height / 2.,
             size=2,
             fill_color=line_color,
             line_width=2,
             line_color=line_color)
    p.line([pitch_width / 2., pitch_width / 2.], [0, pitch_height],
           line_width=2,
           line_color=line_color)

    return p
