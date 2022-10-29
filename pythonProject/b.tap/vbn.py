import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


sns.set(style="darkgrid", palette="muted")
def simulate_linear_data(
    start, stop, N, beta_0, beta_1, eps_mean, eps_sigma_sq
):
    """
    Simulate a random dataset using a noisy
    linear process.

    Parameters
    ----------
    N: `int`
        Number of data points to simulate
    beta_0: `float`
        Intercept
    beta_1: `float`
        Slope of univariate predictor, X

    Returns
    -------
    df: `pd.DataFrame`
        A DataFrame containing the x and y values.
    """
    # Create a pandas DataFrame with column 'x' containing
    # N uniformly sampled values between 0.0 and 1.0
    df = pd.DataFrame(
        {"x":
            np.linspace(start, stop, num=N)
        }
    )
    # Use a linear model (y ~ beta_0 + beta_1*x + epsilon) to
    # generate a column 'y' of responses based on 'x'
    df["y"] = beta_0 + beta_1*df["x"] + np.random.RandomState(s).normal(
        eps_mean, eps_sigma_sq, N
    )
    return df
def plot_simulated_data(df):
    """
    Plot the simulated data with sns.lmplot()

    Parameters
    ----------
    df: `pd.DataFrame`
        A DataFrame containing the x and y values.
    """
    # Plot the data, and a frequentist linear regression fit
    # using the seaborn package
    sns.lmplot(x="x", y="y", data=df, height=10)
    plt.xlim(0.0, 1.0)
    plt.show()
if __name__ == "__main__":
    # These are our "true" parameters
    beta_0 = 1.0  # Intercept
    beta_1 = 2.0  # Slope

    # Simulate 100 data points between 0 and 1, with a variance of 0.5
    start = 0
    stop = 1
    N = 100
    eps_mean = 0.0
    eps_sigma_sq = 0.5

    # Fix Random Seed
    s = 42

    # Simulate the "linear" data using the above parameters
    df = simulate_linear_data(
        start, stop, N, beta_0, beta_1, eps_mean, eps_sigma_sq
    )
    plot_simulated_data(df)