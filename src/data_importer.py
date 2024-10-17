import importlib


class DataImporter:
    """
    Dynamically loads salary data for a given degree.

    Attributes:
        degree_name (str): The name of the degree (e.g., "qfin", "cs", etc.).
    """

    def __init__(self, degree_name):
        """
        Initialize the DataImporter with the specified degree.

        Args:
            degree_name (str): The name of the degree (e.g., "qfin", "cs", etc.).
        """
        self.degree_name = degree_name

    def load_data(self):
        """
        Dynamically load the salary data for the given degree.

        Returns:
            dict: The salary data for the specified degree.

        Raises:
            ValueError: If no data is found for the provided degree name.
        """
        try:
            # Dynamically load the module corresponding to the degree
            module = importlib.import_module(f"data.{self.degree_name}_data")
            return module.data
        except ModuleNotFoundError:
            raise ValueError(f"No data found for degree: {self.degree_name}")
