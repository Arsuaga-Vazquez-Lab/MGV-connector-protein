import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    reg_2050 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = reg_2050.slope
    b = reg_2050.intercept
    x = pd.Series(range(1880, 2051))
    y = m * x + b

    # Create second line of best fit
    df_2000_2050 = df.loc[df['Year'] >= 2000]
    reg_2000 = linregress(df_2000_2050['Year'],
                          df_2000_2050['CSIRO Adjusted Sea Level'])
    m2 = reg_2000.slope
    b2 = reg_2000.intercept
    x2 = pd.Series(range(2000, 2051))
    y2 = m2 * x2 + b2

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='mediumpurple')
    plt.plot(x, y, c='blue')
    plt.plot(x2, y2, c='yellow')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
