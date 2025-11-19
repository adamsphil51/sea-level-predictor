import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (all years)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = list(range(df['Year'].min(), 2051))
    ax.plot(years_extended, [slope * year + intercept for year in years_extended], 'r', label='Fit all years')

    # Second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = list(range(2000, 2051))
    ax.plot(years_recent_extended, [slope_recent * year + intercept_recent for year in years_recent_extended], 'g', label='Fit 2000+')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save figure
    fig.savefig('sea_level_plot.png')
    return fig
