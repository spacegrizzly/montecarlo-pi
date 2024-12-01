# montecarlo-pi

This project estimates the mathematical constant π (Pi) using a basic Monte Carlo simulation. The simulation randomly generates points inside a square and calculates how many of those points fall inside a unit circle inscribed within the square. The ratio of points inside the circle to total points is used to estimate the value of π.

## Requirements

To run this project, you need to install the following Python libraries:
- `numpy`
- `matplotlib`
- `pandas`

You can install them using `pip`:

```bash
pip install numpy matplotlib pandas
```


## How It Works

The Monte Carlo method works by randomly generating points in a square that bounds a unit circle. The ratio of points that fall inside the circle to the total number of points can be used to estimate the value of π.

The method relies on the following geometric principle:

-   The area of a unit circle $A_c=π A_c​= π$.
-   The area of the square with sides of length 2 it $A_s=4$.
-   The ratio of the areas is $A_c / A_s = π/4$​, so $4 \cdot$ $A_c /A_s$ is an approximation for the value of $\pi$​.

## Structure of the Project

-    Monte Carlo Simulation (mc_method):
        This function generates n random points in a square, checks how many fall inside a unit circle, and estimates the value of π based on the ratio.

-    Plotting Function (create_plots):
        This function generates two plots using matplotlib:
            A plot showing the estimated values of π for different sample sizes (logarithmic scale).
            A plot showing the deviation between the estimated and true values of π.

-    Main Function (main):
        This function runs the Monte Carlo simulation for a series of logarithmically spaced sample sizes. It calculates the estimates of π, the deviations from the true value of π, and generates the plots.

## Running the Simulation
Clone this repository or download the script.
To run the simulation, execute the script:
    
```
python estimate_pi.py
```

This will:
- Run the Monte Carlo simulation for sample sizes ranging from 10 to 100,000 (logarithmically spaced).
- Print the results of each simulation (estimated value of π and deviations).
  - Generate two plots:
  -  The estimated value of π for different sample sizes.
  - The deviation of the estimates from the true value of π.

The plots will be saved as a PNG image (estimation_of_pi.png) and displayed on the screen.

## Example Output

Test sample sizes: [1.00000000e+01 1.12201873e+01 1.26081913e+01 1.41952824e+01 ...]
Estimated Pi: 3.141598
...

Example Plots

- Estimated Pi: A plot showing how the estimated value of π improves as the number of random samples increases. The x-axis is logarithmic, and the y-axis shows the estimate of π.
- Deviation from True Pi: A plot showing the deviation of the estimated value from the true value of π over time.

## File Output

The results of the simulation, including the plots, are saved as:

    estimation_of_pi.png (high-quality PNG image of the plots).

## Conclusion

This simple Monte Carlo simulation provides an easy-to-understand approach to estimating π. As the number of random samples increases, the estimate converges towards the true value of π, demonstrating the power of statistical methods.
