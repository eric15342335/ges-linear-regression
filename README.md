# Salary Prediction and Trend Analyzer

This project provides a modular solution for analyzing and predicting salary trends using linear regression. It allows dynamic loading of various datasets and visualizing both historical salary data and future salary predictions.

## Screenshots

![qfin-mean-salary](img/qfin_Mean%20Salary_salary_trend.png)

![actuarsc-mean-salary](img/actuarsc_Mean%20Salary_salary_trend.png)

![cs-mean-salary](img/cs_Mean%20Salary_salary_trend.png)

## Features

- **Modular Design**: The project is structured for easy maintenance and extension.
- **Linear Regression**: Uses `scikit-learn` to predict salary trends for future years.
- **Visualizations**: Generates plots using `matplotlib` to visualize salary trends and predictions.
- **Dynamic Data Loading**: Easily switch between different datasets using a simple interface.
- **Save Plot Feature**: Save the generated plots as high-quality 300 DPI images.

## Installation

1. Clone the repository.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the salary prediction and trend visualization, execute the `main.py` script with the necessary arguments:

```bash
python main.py <degree_name> <salary_metric> [--save-plot]
```

### Arguments

- `<degree_name>`: The name of the degree for which data should be loaded. This corresponds to a specific dataset (e.g., `qfin`, `cs`, `actuarsc`).
- `<salary_metric>`: The salary metric to analyze. You can choose from the following options:
  - `"Mean Salary"`
  - `"Median Salary"`
  - `"Highest Salary"`
  - `"Lowest Salary"`
- `--save-plot`: (Optional) If provided, the plot will be saved as a 300 DPI PNG image instead of being displayed. The image will be saved in the current directory with a filename pattern like `<degree_name>_<salary_metric>_salary_trend.png`.

### Example Usage

**1. Display salary trends for Quantitative Finance (QFIN) graduates and the Mean Salary:**

```bash
python main.py qfin "Mean Salary"
```

This command will display a plot showing historical and predicted salary trends for QFIN graduates, specifically focusing on the mean salary.

**2. Save a plot for Actuarial Science graduates and the Median Salary as a 300 DPI PNG image:**

```bash
python main.py actuarsc "Median Salary" --save-plot
```

This command will save the plot as a PNG image named `actuarsc_Median Salary_salary_trend.png` in the current directory.

### Available Salary Metrics

- **Mean Salary**
- **Median Salary**
- **Highest Salary**
- **Lowest Salary**

### Available Datasets

The following datasets are currently available for analysis:

- **qfin**: Quantitative Finance
- **cs**: Computer Science
- **actuarsc**: Actuarial Science

You can add more datasets to the project by creating new data files in the `data/` directory, following the format used in the existing dataset files (e.g., `qfin_data.py`).

## Output

The program will generate a plot showing both historical salary data and predicted trends for the next few years (e.g., 2024-2028). The plot includes:

- **Actual salary data** from previous years.
- **Predicted salary data** for future years.

If the `--save-plot` option is used, the plot will be saved as a PNG image at 300 DPI resolution.

## Modifying the Project

The project is designed to be modular, allowing users to easily switch between datasets and salary metrics. To add a new dataset:

1. Create a new file in the `data/` directory (e.g., `new_degree_data.py`).
2. Follow the format of the existing data files (`qfin_data.py`, `cs_data.py`, etc.).
3. Update the `main()` function call or use the CLI to specify the new dataset.
