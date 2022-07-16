import pandas as pd

#1 import the data
data_frame = pd.read_csv('data.csv')
data_frame.shape #18207 rows, 89 columns

data_frame.describe() #count,mean,max etc...
data_frame.values # get all the values of the data

data_frame[data_frame["Age"]>40].head() # filtering with Age > 40

#2 Clean the data
df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value']) # get data with specific columns

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

wage = df1['Wage'].replace('[\€,]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€,]', '', regex=True).apply(value_to_float)
df1['Wage'] = wage
df1['Value'] = value
df1['difference'] = df1['Value'] - df1['Wage']
df1.sort_values('difference', ascending=False)

# for visualization
import seaborn as sns
sns.set()
graph = sns.scatterplot(x='Wage', y='Value')

# for interactive visualization
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

TOOLTIPS = [
    ("index", "$index"),
    ("(Wage,Value)", "(@Wage, @Value)"),
    ("Name", "@Name"),
]

hover = HoverTool(tooltips=[TOOLTIPS])

p = figure(title="Soccer 2019", x_axis_label='Wage', y_axis_label='Value', plot_width=700, plot_height=700, tools=[hover])
p.circle('Wage', 'Value', size=10, source=df1)
show(p)

#so far, we are handling data science part.

#source
#https://github.com/aneagoie/ML-Notes/blob/master/soccer.ipynb