from matplotlib.pyplot import show
import streamlit as st
import datetime
import yfinance as yf

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


from plots import plot_history, plot_candles, plot_forecast


symbols = [
           'FLRY3.SA',
            'ITSA4.SA',
            'ARZZ3.SA',
           'BPAC11.SA',#'BPAC11F.SA',
           'SQIA3.SA',#'SQIA3F.SA',
           'TAEE11.SA',#'TAEE11F.SA',
           'VIIA3.SA',
           'LAME4.SA',#'LAME4F.SA',
          'PETR4.SA',#'PETR4F.SA',
           'BRKM5.SA',#'BRKM5F.SA',
           'LREN3.SA',#'LREN3F.SA',
          'RADL3.SA',# 'RADL3F.SA',
           'ENBR3.SA',#'ENBR3F.SA',
           'EQTL3.SA',
           'WEGE3.SA'#'WEGE3F.SA'
]

def get_stock_data(symbol,
                   start = None,
                   end = None,
                   t_delta_days = None,
                   verbose = False):
  if t_delta_days is None:
    t_delta = datetime.timedelta(days=2000)
  else:
    t_delta = datetime.timedelta(days=t_delta_days)

  if start is None:
    start = (datetime.datetime.now() - t_delta).strftime('%Y-%m-%d')

  if end is None:
    end = datetime.datetime.now().strftime('%Y-%m-%d')

  print('symbol: {}, start: {}, end: {}, delta: {}'.format(symbol, start, end, t_delta))
  df = yf.download(symbol, start=start, 
                    end=end)

  df['Date'] = df.index
  df.reset_index(drop=True, inplace = True)
  return df


def prophet_forecast(
                      data,
                     n_years = 1
                     ):
  
  period = n_years * 365

  df_train = data[['Date', 'Close']]
  df_train = df_train.rename(
      columns = {'Date': 'ds',
                 'Close': 'y'}
  )

  m = Prophet()
  m.fit(df_train)
  future = m.make_future_dataframe(periods = period)

  y = m.predict(future)
  
  return y, m


st.title('Brazilian Stock Forecast')

selected_stock = st.selectbox('Select a symbol for prediction',
    symbols)

# slider selection of number of years
n_years = st.slider('Years of prediction: ', 1 ,4)

# getting the data for the selected symbol
df = get_stock_data(selected_stock)

st.subheader('Raw data')
st.write(df.head())

# candlestick
st.write('Candlestick for {}'.format(selected_stock))
fig1 = plot_candles(df, selected_stock)
st.plotly_chart(fig1)

# apply model
y, m = prophet_forecast(data=df,
                            n_years=n_years)

# Forecast
st.write('Forecast for {}'.format(selected_stock))
fig2 = plot_forecast(y,
                    period = 365*n_years)
st.pyplot(fig2)
st.write(y)

