import argparse
from src.data_importer import DataImporter
from src.salary_regression import SalaryRegression
from src.salary_plotter import SalaryPlotter
from data.data_keys import (
    MEAN_SALARY,
    MEDIAN_SALARY,
    HIGHEST_SALARY,
    LOWEST_SALARY,
)  # Import salary metric keys


def main(degree_name, salary_metric, save_plot):
    """
    Load data, perform regression, and plot salary trends.

    Args:
        degree_name (str): Name of the degree for which data should be loaded (e.g., "qfin").
        salary_metric (str): The salary metric to analyze (e.g., MEAN_SALARY).
        save_plot (bool): Whether to save the plot as a 300 DPI image.

    Returns:
        None
    """
    # Load the data for the specified degree
    importer = DataImporter(degree_name)
    data = importer.load_data()

    # Perform linear regression on the specified salary metric
    regressor = SalaryRegression(data)
    future_years, predicted_salaries = regressor.perform_regression(salary_metric)

    # Plot the salary trends and predictions
    plotter = SalaryPlotter(data, future_years, predicted_salaries)
    plotter.plot_salary_trends(
        salary_metric, f"{salary_metric} of {degree_name.upper()} Graduates"
    )

    # Save the plot if --save-plot is provided, otherwise show it
    if save_plot:
        filename = f"{degree_name}_{salary_metric}_salary_trend.png"
        print(f"Saving plot to {filename} at 300 DPI...")
        plotter.save_plot(
            f"{salary_metric} Trends and Predictions for {degree_name.upper()} Graduates",
            filename,
        )
    else:
        plotter.show_plot(
            f"{salary_metric} Trends and Predictions for {degree_name.upper()} Graduates"
        )


if __name__ == "__main__":
    # Setup the argument parser
    parser = argparse.ArgumentParser(
        description="Perform salary trend analysis and regression for different degrees."
    )
    parser.add_argument(
        "degree_name", type=str, help="Name of the degree (e.g., qfin, cs, actuarsc)"
    )
    parser.add_argument(
        "salary_metric",
        type=str,
        choices=[MEAN_SALARY, MEDIAN_SALARY, HIGHEST_SALARY, LOWEST_SALARY],
        help="The salary metric to analyze (e.g., Mean Salary, Median Salary, Highest Salary, Lowest Salary)",
    )
    parser.add_argument(
        "--save-plot",
        action="store_true",
        help="Save the plot as a 300 DPI image instead of displaying it.",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.degree_name, args.salary_metric, args.save_plot)
