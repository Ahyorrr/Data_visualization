from d6 import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()

# rolling the dice and adding to list
result = []
for value in range(50000):
    max_result = die_1.roll() + die_2.roll() + die_3.roll()
    result.append(max_result)
# measuring frequency of rolls and adding to list
frequencies = []
max_num_sides = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_num_sides+1):
    frequency = result.count(value)
    frequencies.append(frequency)

x_axis = list(range(3, max_num_sides+1))
data = [Bar(x=x_axis, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of results'}

my_layout = Layout(title='Chart showing the frequency of three d6 dice',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6_D6_D6.html')
