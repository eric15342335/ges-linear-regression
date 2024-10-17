import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns

# Data provided in the script
salary_data = {
    "Year": [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Average Basic Salary (QFin)": [25147, 23733, 30810, 35062, 33645, 39727, 44006, 56559],
    "Median Basic Salary (QFin)": [20000, 20000, 28000, 30000, 30000, 25000, 35000, 47758],
    "Minimum Basic Salary (QFin)": [14000, 15000, 15000, 17000, 24000, 16000, 20000, 32170],
    "Maximum Basic Salary (QFin)": [55000, 53000, 80000, 98000, 50000, 75000, 70000, 91000],
    "Average Gross Salary (QFin)": [28763, 29428, 32443, 37376, 34112, 40537, 52430, 58651],
    "Median Gross Salary (QFin)": [20000, 25542, 28000, 30000, 30000, 25000, 48667, 52342],
    "Minimum Gross Salary (QFin)": [15000, 15000, 16167, 17000, 24000, 17680, 20000, 35387],
    "Maximum Gross Salary (QFin)": [100000, 76333, 80000, 111167, 50000, 77188, 91583, 91000],
    "Average Basic Salary (HKU)": [25522, 24097, 25522, 26403, 26929, 27467, 29680, 30821],
    "Median Basic Salary (HKU)": [20000, 18500, 20000, 20000, 20000, 21340, 23325, 25000],
    "Average Gross Salary (HKU)": [26456, 24965, 26456, 27175, 27956, 28921, 30919, 31982],
    "Median Gross Salary (HKU)": [20042, 19979, 20042, 21125, 22000, 22750, 25000, 25000],
    "Total Graduates (QFin)": [24, 25, 27, 28, 30, 35, 29, 33],
    "Respondents (QFin)": [24, 22, 25, 23, 23, 28, 25, 24],
    "Percentage Respondents (QFin)": [100, 88, 93, 82, 77, 80, 86, 73]
}

# Create a DataFrame
df = pd.DataFrame(salary_data)

# Global variables for models
model_basic = None
model_gross = None

# Function to plot salary trends
def plot_salary_trends(y_column, ylabel, title, ax=None, color='blue'):
    if ax is None:
        ax = plt.gca()
    ax.plot(df["Year"], df[y_column], label=ylabel, color=color)
    ax.set_xlabel("Year")
    ax.set_ylabel("Salary (HKD)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

# Trend Analysis and Prediction for Basic Salary (All types)
def plot_salary_predictions(df, y_column, label, ax=None):
    global model_basic  # Ensure the model is accessible globally
    if ax is None:
        ax = plt.gca()

    # Linear regression
    X = df["Year"].values.reshape(-1, 1)
    y = df[y_column].values
    model_basic = LinearRegression()
    model_basic.fit(X, y)

    # Predict for future years (2024-2028)
    future_years = np.arange(2024, 2029).reshape(-1, 1)
    predicted_salaries = model_basic.predict(future_years)

    # Plot actual and predicted values
    ax.plot(df["Year"], y, label=f"{label} (Actual)", color="blue")
    ax.plot(future_years, predicted_salaries, label=f"{label} (Predicted)", color="red", linestyle="--")
    ax.set_xlabel("Year")
    ax.set_ylabel("Salary (HKD)")
    ax.legend()
    ax.grid(True)

# Plot salary predictions for mean, median, min, and max basic salaries
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

plot_salary_predictions(df, "Average Basic Salary (QFin)", "Average Basic Salary", ax=axs[0, 0])
plot_salary_predictions(df, "Median Basic Salary (QFin)", "Median Basic Salary", ax=axs[0, 1])
plot_salary_predictions(df, "Minimum Basic Salary (QFin)", "Minimum Basic Salary", ax=axs[1, 0])
plot_salary_predictions(df, "Maximum Basic Salary (QFin)", "Maximum Basic Salary", ax=axs[1, 1])

fig.suptitle("HKU Quantitative Finance Basic Salary Predictions (2024-2028)")
plt.tight_layout()
plt.savefig("hkufin_salary_predictions.png", dpi=300)
plt.show()

# Weighted Linear Regression for Median Salary Predictions
def plot_weighted_median_salary(df):
    X = df["Year"].values.reshape(-1, 1)
    y = df["Median Basic Salary (QFin)"].values

    # Apply exponentially decreasing weights (more weight to earlier years)
    # Weights are higher for earlier years, reducing the impact of recent outliers.
    weights = np.exp(-0.3 * (df["Year"].values[-1] - df["Year"].values))

    # Fit a weighted linear regression model
    model_weighted = LinearRegression()
    model_weighted.fit(X, y, sample_weight=weights)

    # Predict for future years (2024-2028)
    future_years = np.arange(2024, 2029).reshape(-1, 1)
    predicted_salaries_weighted = model_weighted.predict(future_years)

    # Plot actual and predicted values
    plt.figure(figsize=(12, 6))
    plt.plot(df["Year"], y, label="Median Basic Salary (QFin) (Actual)", color="blue")
    plt.plot(future_years, predicted_salaries_weighted, label="Weighted Median Basic Salary (Predicted)", color="red", linestyle="--")
    plt.xlabel("Year")
    plt.ylabel("Salary (HKD)")
    plt.title("Weighted Prediction of HKU Quantitative Finance Median Basic Salary (2024-2028)")
    plt.legend()
    plt.grid(True)

    plt.show()

plot_weighted_median_salary(df)

# Respondent Data Visualization
plt.figure(figsize=(12, 6))
ax1 = plt.subplot(111)
ax1.plot(df["Year"], df["Respondents (QFin)"], label="Number of Respondents (QFin)", color="blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Respondents")

ax2 = ax1.twinx()
ax2.plot(df["Year"], df["Percentage Respondents (QFin)"], label="Percentage of Respondents (QFin)", color="orange")
ax2.set_ylabel("Percentage of Respondents (%)")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.title("HKU Quantitative Finance Graduate Respondents")
plt.grid()
plt.show()

# Salary Distribution Analysis - Basic Salaries
plt.figure(figsize=(12, 6))
sns.histplot(df["Average Basic Salary (QFin)"], bins=10, color="blue", label="Average Basic Salary (QFin)", kde=True)
sns.histplot(df["Median Basic Salary (QFin)"], bins=10, color="green", label="Median Basic Salary (QFin)", kde=True)
plt.xlabel("Salary (HKD)")
plt.ylabel("Frequency")
plt.title("Distribution of HKU QFin Graduate Basic Salaries")
plt.legend()
plt.grid(True)
plt.show()

# Conclusion and Future Predictions
future_year = 2024

# Make sure model_basic is defined globally
predicted_basic_salary_2024 = model_basic.predict([[future_year]])
print(f"Predicted Average Basic Salary for {future_year}: {predicted_basic_salary_2024[0]:.2f} HKD")
