"""
Estimate the number PI using a basic Monte Carlo simulation.
This script simulates random points within a square and estimates the value of pi
based on how many points fall inside a unit circle inscribed within the square.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def mc_method(n: int = 1000) -> float:
    """
    Estimate the value of pi using the Monte Carlo method.

    The Monte Carlo simulation generates random points in a square and counts how many
    fall inside a unit circle. The ratio of points inside the circle to total points
    is used to estimate pi.

    :param n: Number of random points to generate (default is 1000).
    :return: Estimated value of pi.
    """
    # Define the boundaries for the square
    min, max = -1, 1

    # Generate random x and y coordinates for the points
    randx = [np.random.uniform(min, max) for _ in np.arange(n)]
    randy = [np.random.uniform(min, max) for _ in np.arange(n)]

    # Create a list of (x, y) coordinate pairs
    rand = [randx, randy]
    t_rand = np.transpose(rand)  # Transpose to get pairs of points

    # Count how many points fall inside the unit circle
    count = 0
    for r in t_rand:
        z = np.sqrt(r[0] ** 2 + r[1] ** 2)  # Distance from the origin
        if z < 1:  # Point is inside the unit circle
            count += 1

    # The ratio of points inside the circle to total points is used to estimate pi
    ratio = count / n

    # The area of the square is 2*2=4, the area of the circle is r**2 * pi
    # which is just equal to pi. This means that the ratio of the areas
    # times 4 is equal to pi
    pi = ratio * 4

    print(f"Estimated Pi: {pi}")
    return pi


def create_plots(df: pd.DataFrame):
    """
    Create and display plots using Matplotlib to visualize the Monte Carlo simulation results.

    :param df: DataFrame containing sample sizes, estimates of pi, and deviations.
    """
    # Enable LaTeX rendering for text in the plot
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.size'] = 12  # Adjust font size for clarity
    plt.rcParams['legend.fontsize'] = 10

    # Create a figure and axes for two subplots (one for estimates, one for deviations)
    fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [3, 1]})

    # First subplot: Plot estimate of pi
    axes[0].plot(df['n'], df['estimate'] * 0 + np.pi, color='xkcd:grey', label='True Pi')  # Line for the true value of pi
    axes[0].plot(df['n'], df['estimate'], color='xkcd:blue', label=r'Estimate of $\pi$')  # Line for estimated values of pi
    axes[0].set_ylabel(r'Estimate of $\pi$')  # Label y-axis
    axes[0].legend()  # Display the legend
    axes[0].set_xscale('log')  # Set x-axis to logarithmic scale
    axes[0].grid(True, which="both", linestyle='--', linewidth=0.5)  # Add grid to the plot
    axes[0].set_xticks([])  # Remove x-axis numbers from the top plot

    # Second subplot: Plot deviation from true pi
    axes[1].plot(df['n'], df['deviation'] * 0, color='xkcd:grey')  # Line at zero for reference
    axes[1].plot(df['n'], df['deviation'], color='green', label=r'Deviation from True $\pi$')  # Line for deviation values
    axes[1].set_xlabel('Sample size n')  # Label x-axis
    axes[1].set_ylabel('Deviation')  # Label y-axis
    axes[1].set_ylim(-0.5, 0.5)  # Limit the y-axis to the range [-0.5, 0.5]
    axes[1].legend()  # Display the legend
    axes[1].set_xscale('log')  # Set x-axis to logarithmic scale
    axes[1].grid(True, which="both", linestyle='-', linewidth=0.3)  # Add grid to the plot

    # Adjust layout for better spacing between subplots
    plt.tight_layout()

    # Save the plot as a high-quality PNG file
    plt.savefig("estimation_of_pi.png", dpi=300, bbox_inches='tight')

    # Display the plot
    plt.show()


def main():
    """
    Main function to run the Monte Carlo simulation, estimate pi, and generate plots.
    """
    # Define the sample sizes to be used in the simulation (logarithmic scale)
    test_n = np.logspace(1, 5, 300)  # Sample sizes from 10 to 100,000
    print(f"Test sample sizes: {test_n}")

    # List to store the estimates of pi
    pi_est = []

    # Run the Monte Carlo simulation for each sample size
    for n in test_n:
        pi = mc_method(int(n))  # Estimate Pi for each sample size
        pi_est.append(pi)

    # Create a DataFrame to store the results
    df = pd.DataFrame(test_n, columns=["n"])
    df["estimate"] = pi_est

    # Calculate the deviation from the true value of pi
    true_pi = np.pi
    df["deviation"] = true_pi - df["estimate"]

    # Print the DataFrame for reference
    print(df)

    # Create and display the plots
    create_plots(df)

    return 0


if __name__ == '__main__':
    main()
