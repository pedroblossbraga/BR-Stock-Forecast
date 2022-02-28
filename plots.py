import matplotlib.pyplot as plt

def plot_history(df):
  plt.figure(figsize=(16,8))
  plt.title('Close Price History')
  plt.plot(df['Close'])
  plt.xlabel('Date', fontsize=18)
  plt.ylabel('Close Price (Reais)', fontsize=18)
  plt.show()
