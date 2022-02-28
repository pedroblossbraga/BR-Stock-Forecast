import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as py

def plot_history(df):
  fig = plt.figure(figsize=(16,8))
  plt.title('Close Price History')
  plt.plot(df['Date'], df['Close'])
  plt.xlabel('Date', fontsize=18)
  plt.ylabel('Close Price (Reais)', fontsize=18)
  
  return fig


def plot_forecast(y_hat,
                  period=365):
  fig = plt.figure(figsize=(15,4))
  plt.title('Predictions',
            fontsize = 18)

  plt.plot(y_hat[['ds']], y_hat[['yhat']],
          label=r'$y$',
          color='blue')

  plt.plot(y_hat[['ds']], y_hat[['trend']],
          label='trend',
          color='orange')

  plt.fill_between(
      y_hat['ds'][-period:],
      y_hat['yhat_lower'][-period:],
      y_hat['yhat_upper'][-period:],
      color='blue',
      alpha=0.3
  )
  plt.legend(loc='best',
            fontsize=18)
  return fig



def plot_candles(df, s):
  trace = go.Candlestick(x=df['Date'],
                         open=df['Open'],
                         high=df['High'],
                         low=df['Low'],
                         close=df['Close'])
  layout = go.Layout(
      title= f'Candlestick ({s})',
      title_x = 0.5,
      xaxis = dict(
          rangeslider = dict(
              visible = False
          )
      )
  )
  data = [trace]

  fig = go.Figure(data=data, layout=layout)
  #py.iplot(fig)
  return fig
