import matplotlib.pyplot as plt
from data.data_keys import YEAR  # Import YEAR key from data_keys.py


class SalaryPlotter:
    """
    Plots actual and predicted salary trends using matplotlib.

    Attributes:
        data (dict): The loaded salary data for a specific degree.
        future_years (ndarray): Future years for which predictions were made.
        predicted_salaries (ndarray): The predicted salary values for the future years.
    """

    def __init__(self, data, future_years, predicted_salaries):
        """
        Initialize SalaryPlotter with the provided data, future years, and predicted salaries.

        Args:
            data (dict): The salary data dictionary for a degree.
            future_years (ndarray): Future years (2024-2028) for predictions.
            predicted_salaries (ndarray): Predicted salary values for the future years.
        """
        self.data = data
        self.future_years = future_years
        self.predicted_salaries = predicted_salaries

    def plot_salary_trends(self, key, label, color="blue"):
        """
        Plot actual and predicted salary trends.

        Args:
            key (str): The salary metric key (e.g., MEAN_SALARY, MEDIAN_SALARY).
            label (str): Label for the plot (e.g., "Mean Salary of QFIN Graduates").
            color (str, optional): Color for the actual salary plot. Defaults to "blue".

        Returns:
            None
        """
        # Extract year data using the YEAR key
        years = self.data[YEAR]
        salaries = self.data[key]

        # Plot actual salary data
        plt.plot(years, salaries, marker="o", label=f"{label} (Actual)", color=color)

        # Plot predicted salary data
        plt.plot(
            self.future_years,
            self.predicted_salaries,
            marker="o",
            label=f"{label} (Predicted)",
            linestyle="--",
            color="red",
        )

        # Add labels and grid
        plt.xlabel("Year")
        plt.ylabel("Salary")
        plt.legend()
        plt.grid(True)

    def show_plot(self, title):
        """
        Display the plot with the given title.

        Args:
            title (str): Title of the plot.

        Returns:
            None
        """
        plt.title(title)
        plt.show()

    def save_plot(self, title, filename):
        """
        Save the plot as a 300 DPI PNG image.

        Args:
            title (str): Title of the plot.
            filename (str): Filename for the saved plot.

        Returns:
            None
        """
        plt.title(title)
        plt.savefig(filename, dpi=300)
        plt.close()
