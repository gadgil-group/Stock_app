
import yfinance as yf
import streamlit as st
import datetime
from bokeh.plotting import figure
import numpy as np
import pandas as pd
import altair as alt

st.write("""
# TDI Stock Price App
""")


# user input
st.sidebar.write("""
# Select plot parameters
""")
tickerSymbol = st.sidebar.text_input('Tickr (e.g. GOOGL)', 'GOOGL')
start_d = st.sidebar.date_input("Stard date",datetime.date(2015, 7, 6))
end_d = st.sidebar.date_input("End date",datetime.date(2019, 8, 6))


#get data on ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start_d, end=end_d)

#define plot info
st.write("""
### Stock Closing Price from""", start_d, """to """, end_d)
df = tickerDf.reset_index()
c = alt.Chart(df).mark_line().encode(x='Date', 
                                        y=alt.Y('Close', axis=alt.Axis(format='$', title='Close price ($)')), 
                                        tooltip=['Open', 'High', 'Low', 'Close', 'Volume']).interactive()
st.altair_chart(c, use_container_width=True)

#x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
#    y=alt.Y('y', axis=alt.Axis(format='$', title='dollar amount'))
 #   alt.Y('Close', axis=alt.Axis(format='$', title='Close price ($)'))


