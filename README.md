
# Final Project - Automobile Sales Analysis and Dashboard

This repository contains two Python scripts for analyzing and visualizing historical automobile sales data. The first script provides a comprehensive analysis of the data using various visualizations, and the second script creates an interactive web-based dashboard using Dash.

## Module5-P1-FinalProject.py

### Overview
This script performs a thorough analysis of historical automobile sales, including trends over time, the impact of recessions, and correlations with factors such as GDP, consumer confidence, and advertising expenditure.

### Key Functions
- **fetch_data()**: Downloads the dataset from a cloud-hosted CSV and loads it into a Pandas DataFrame.
- **plot_sales_over_time(df)**: Generates a line plot of automobile sales over the years, highlighting recession periods.
- **plot_vehicle_type_trends(df)**: Visualizes trends in sales across different vehicle types, comparing recession and non-recession periods.
- **plot_sales_comparison(df)**: Compares average automobile sales during recession and non-recession periods using a bar plot.
- **plot_gdp_variations(df)**: Displays side-by-side line plots for GDP variations during recession and non-recession periods.
- **plot_seasonality_bubble_chart(df)**: Creates a bubble chart to show the impact of seasonality on automobile sales.
- **plot_recession_sales_side_by_side(df)**: Produces scatter plots for the relationship between vehicle prices, consumer confidence, and sales during recessions.
- **plot_advertising_expenditure_pie(df)**: Shows a pie chart for advertising expenditure during recession and non-recession periods.
- **plot_advertisement_expenditure_by_vehicle_type(df)**: Visualizes the share of advertising expenditure by vehicle type during recessions.

---

## Module5-P2-FinalProject.py

### Overview
This script builds an interactive dashboard using Dash to visualize automobile sales statistics. The dashboard allows the user to explore yearly trends, recession impacts, and more.

### Features
- **Dropdown Options**: Users can choose between "Yearly Statistics" and "Recession Period Statistics". If "Yearly Statistics" is selected, the user can also choose a specific year.
- **Dynamic Visualizations**: The dashboard updates charts dynamically based on user selections.

### Key Visualizations
- **Recession Period Statistics**:
  1. Line chart: Average automobile sales fluctuation over recession periods.
  2. Bar chart: Average number of vehicles sold by vehicle type during recessions.
  3. Pie chart: Total advertising expenditure share by vehicle type during recessions.
  4. Bar chart: Effect of unemployment rate on vehicle type and sales.

- **Yearly Statistics**:
  1. Line chart: Yearly automobile sales.
  2. Line chart: Total monthly automobile sales for the selected year.
  3. Bar chart: Average number of vehicles sold by vehicle type for the selected year.
  4. Pie chart: Total advertisement expenditure by vehicle type for the selected year.

---

### How to Run
1. Ensure you have the necessary Python libraries installed:
   ```
   pip install dash plotly pandas
   ```
2. Run `Module5-P1-FinalProject.py` to generate various plots analyzing automobile sales data.
3. Run `Module5-P2-FinalProject.py` to launch the interactive dashboard. Access the dashboard by navigating to `http://127.0.0.1:8050/` in your browser.
