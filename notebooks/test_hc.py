# Import classes using precise module indications. For example:
from highcharts_core.chart import Chart
from highcharts_core.global_options.shared_options import SharedOptions
from highcharts_core.options import HighchartsOptions
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.series.bar import BarSeries
import pandas as pd

# Create a chart object
my_chart = Chart()

# from a Pandas dataframe
df = pd.DataFrame({'name': ['a', 'b', 'c'], 'data': [1, 2, 3]})
my_chart.add_series(BarSeries(df, 'name', 'data'))

# add optiona
my_chart.set_options(
    HighchartsOptions(
        title={'text': 'My Chart'},
        plotOptions={
            'bar': BarOptions(
                dataLabels={'enabled': True}
            )
        }
    )
)

# Render the chart
my_chart.render()