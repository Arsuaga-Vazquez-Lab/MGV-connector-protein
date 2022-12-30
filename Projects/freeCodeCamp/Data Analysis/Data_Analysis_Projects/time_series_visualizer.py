import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

# Read data into df
# Set date as index
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) 
& (df['value'] < df['value'].quantile(0.975))]

df.index = pd.to_datetime(df.index)


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots()
  plt.plot(df.index, df['value'])
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
  df_bar['month'] = pd.DatetimeIndex(df_bar.index).month_name()
  df_bar['month_num'] = pd.DatetimeIndex(df_bar.index).month
  df_bar = df_bar.sort_values(by=['month_num'])
  # Draw bar plot
  fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
  ax = sns.barplot(x="year",
                   y="value",
                   hue="month",
                   data=df_bar,
                   palette="tab10",
                   ci=None)
  ax.set_xlabel("Years")
  ax.set_ylabel("Average Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]
  df_box['month_num'] = pd.to_datetime(df_box.month, format='%b').dt.month
  df_box = df_box.sort_values('month_num')

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2)
  sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  sns.boxplot(data=df_box, x="month", y="value", ax=axes[1])
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")
  fig.savefig('box_plot.png')
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
