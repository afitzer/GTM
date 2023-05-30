import plotly.express as px
import pandas as pd
import sqlite3

conn = sqlite3.connect('C:/Users/alexp/Documents/GTM/db.sqlite3')

flights = "SELECT name, cost FROM earnings_flight"
hotels = "SELECT name, cost FROM earnings_hotel"
events = "SELECT name, cost FROM earnings_event"
flight_df = pd.read_sql_query(flights, conn)
hotels_df = pd.read_sql_query(hotels, conn)
events_df = pd.read_sql_query(events, conn)

conn.close()

flight_df['type'] = 'Flight'
hotels_df['type'] = 'Hotel'
events_df['type'] = 'Event'

df = pd.concat([flight_df, hotels_df, events_df])

fig = px.bar(df, x='cost', y='name', color='type', height=600, width=1000, template="simple_white", 
        color_discrete_sequence=px.colors.qualitative.G10,
        title="Costs by Trip",
        labels=dict(
                     name="Trip Name", cost="Trip Cost (US$)"))

fig.update_layout(font_family="Rockwell",
                  legend=dict(orientation="h", title="", y=1.1, x=1, xanchor="right", yanchor="bottom"))

fig.update_xaxes(tickprefix="$")

fig.write_html("C:/Users/alexp/Documents/GTM/earnings/templates/earnings/chart.html")