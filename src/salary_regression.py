from sklearn.linear_model import LinearRegression
import numpy as np
from data.data_keys import YEAR  # Import YEAR key from data_keys.py


class SalaryRegression:
    """
    Performs linear regression on salary data to predict future salaries.

    Attributes:
        data (dict): The loaded salary data for a specific degree.
        model (LinearRegression): Linear regression model instance from scikit-learn.
    """

    def __init__(self, data):
        """
        Initialize SalaryRegression with the provided data.

        Args:
            data (dict): The salary data dictionary for a degree.
        """
        self.data = data
        self.model = LinearRegression()

    def perform_regression(self, key):
        """
        Perform linear regression on a specified salary metric.

        Args:
            key (str): The salary metric key (e.g., MEAN_SALARY, MEDIAN_SALARY).

        Returns:
            tuple: A tuple containing:
                - future_years (ndarray): Future years (2024-2028) for predictions.
                - predicted_salaries (ndarray): Predicted salary values for the future years.
        """
        # Extract year data using the YEAR key
        years = np.array(self.data[YEAR]).reshape(-1, 1)
        # Extract salary data for the specified metric
        salaries = np.array(self.data[key])

        # Fit the linear regression model
        self.model.fit(years, salaries)

        # Predict future salaries for the years 2024-2028
        future_years = np.arange(2024, 2029).reshape(-1, 1)
        predicted_salaries = self.model.predict(future_years)

        return future_years, predicted_salaries
