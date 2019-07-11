import dash
import dash_html_components as html
import dash_core_components as dcc
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from pygal.style import Style	
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
response_dict=r.json()
repo_dicts=response_dict['items']


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
    ),
    html.Div(id='slider-output-container')
])


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


names,plot_dicts=[],[]
i=0
for repo_dict in repo_dicts:
    if i <value:
        i=i+1 
        names.append(repo_dict['name'])

        description = repo_dict['description']
        if not description:
            description = 'No description provided'

        plot_dict={
            'value':repo_dict['stargazers_count'],
            'label':description,
            'xlink':repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)
    else: break
#=========Configuration==============
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
# my_config.show_y_guides=False
my_config.width=1000
#====================================

my_style=LS('#333366',base_style=LCS,title_font_size=24,label_font_size=14,major_label_font_size=18,truncate_label=15)

chart=pygal.Bar(my_config,style=my_style)
chart.title="Most Stared Python Projects on Github"
chart.x_labels=names
chart.y_title='The number of stars'
chart.add('',plot_dicts)

if __name__ == '__main__':
    app.run_server(debug=True)

