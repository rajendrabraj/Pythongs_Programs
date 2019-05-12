import pygal

# Show a Stacked Line Chart

line_chart = pygal.StackedLine(fill=True)


line_chart.title = 'Multiple Stocks Compare'
# X range axis data
line_chart.x_labels = map(str, range(2010, 2020))
#Chart Values
line_chart.add('DHFL', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Ashok Leyland',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('Wipro',      [385.8, 384.6, 384.7, 174.5,   166, 158.6, 154.7, 144.8, 136.2, 126.6, 120.1])
line_chart.add('Icici',  [14.2, 15.4, 15.3,  78.9,    99, 110.4,  228.9,  325.8,  326.7,  416.8,  387.5])

line_chart.render_in_browser()
line_chart.render_to_file("D:\\Rajendra_2019\\Python_docs\\Sample_Chart.SVG")


line_chart.render_to_file("D:\\Rajendra_2019\\Python_docs\\JPG_Chart.jpg")
line_chart.render_to_file("D:\\Rajendra_2019\\Python_docs\\JPG_Chart.png")