import pandas as pd
import matplotlib.pyplot as plt

# Constant for the CSV file path
CSV_FILE = None


# Function to load data from a CSV file
def load_data(CSV_FILE):
    """This function loads data from a CSV file."""
    data_frame = pd.read_csv(CSV_FILE)
    return data_frame


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(data_frame):
    """This function plots the pie chart."""
    # Group by Industry and sum Net Worth
    industry_net_worth = data_frame.groupby("Industry")["Net Worth (in billions)"].sum()

    # Plot the pie chart
    industry_net_worth.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats(data_frame):
    """This function prints summary statistics."""
    sum_stats = data_frame.describe()
    print(sum_stats)


def grab_mean(data_frame, col):
    """This function is meant to grab the mean from the summary stats."""
    return data_frame[col].mean()


def grab_min(data_frame, col):
    """This function is meant to grab the minimum net worth from the summary stats."""
    return data_frame[col].min()


def grab_std(data_frame, col):
    """This function is meant to grab the standard deviation from the summary stats."""
    return data_frame[col].std()


def grab_max(data_frame, col):
    """This function is meant to grab the maximum networth from the summary stats."""
    return data_frame[col].max()


def mini_project_2():
    """This function runs the main workflow."""
    data_frame = load_data()
    plot_pie_chart(data_frame)
    summary_stats(data_frame)
