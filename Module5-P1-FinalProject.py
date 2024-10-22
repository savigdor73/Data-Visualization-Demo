import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import seaborn as sns
import numpy as np

# URL of the data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

def fetch_data():
    # Download the data using requests
    resp = requests.get(URL)
    text = io.BytesIO(resp.content)
    # Read the data into a DataFrame
    df = pd.read_csv(text)
    print('Data downloaded and read into a DataFrame!')
    return df

# Call the function to fetch data
df = fetch_data()

def plot_sales_over_time(df):
    if 'Year' in df.columns and 'Automobile_Sales' in df.columns and 'Recession' in df.columns:
        # Group the data by year and sum the sales for each year
        sales_per_year = df.groupby('Year')['Automobile_Sales'].sum().reset_index()

        # Merge the recession data back into the sales data
        sales_per_year = pd.merge(sales_per_year, df[['Year', 'Recession']].drop_duplicates(), on='Year', how='left')

        # Create a line plot with data points
        plt.figure(figsize=(10, 6))
        plt.plot(sales_per_year['Year'], sales_per_year['Automobile_Sales'], marker='o', color='blue')

        # Set the title and axis labels
        plt.title('Automobile Sales Over Time with Recession Annotations')
        plt.xlabel('Year')
        plt.ylabel('Total Automobile Sales')

        # Calculate an offset for text positioning above the data points
        offset = sales_per_year['Automobile_Sales'].max() * 0.02  # 2% of the maximum sales value

        # Annotate the recession years where Recession == 1
        for idx, row in sales_per_year.iterrows():
            if row['Recession'] == 1:
                # Get the sales value for the recession year
                sales_value = row['Automobile_Sales']
                year = row['Year']
                # Add text annotation above the data point
                plt.text(year, sales_value + offset, 'Recession', ha='center', va='bottom', fontsize=9, color='red')

        # Add x-ticks for all years and color them based on recession
        years = sales_per_year['Year'].tolist()
        recession_years = sales_per_year[sales_per_year['Recession'] == 1]['Year'].tolist()
        xtick_colors = ['red' if year in recession_years else 'black' for year in years]
        
        # Set the xticks with colors
        plt.xticks(years, rotation=45, ha='right', fontsize=9)
        ax = plt.gca()
        for xtick, color in zip(ax.get_xticklabels(), xtick_colors):
            xtick.set_color(color)

        # Adjust layout to prevent clipping
        plt.tight_layout()

        # Display the plot
        plt.show()
    else:
        print("The required columns 'Year', 'Automobile_Sales', and 'Recession' are not present in the dataset.")

def plot_vehicle_type_trends(df):
    # Check if 'Recession' column exists
    if 'Recession' in df.columns:
        # Filter the data for Recession = 1 and group by year and vehicle type to get averages
        recession_data = df[df['Recession'] == 1]
        non_recession_data = df[df['Recession'] == 0]

        # Group by year and vehicle_type, calculating the average sales for both recession and non-recession periods
        recession_grouped = recession_data.groupby(['Year', 'Vehicle_Type'], as_index=False)['Automobile_Sales'].mean()
        non_recession_grouped = non_recession_data.groupby(['Year', 'Vehicle_Type'], as_index=False)['Automobile_Sales'].mean()

        # Get unique vehicle types for subplots
        vehicle_types = df['Vehicle_Type'].unique()

        # Create subplots in a grid of 2 columns
        fig, axes = plt.subplots(len(vehicle_types) // 2 + len(vehicle_types) % 2, 2, figsize=(14, 10), sharex=True)

        # Flatten axes for easier iteration
        axes = axes.flatten()

        for i, vehicle in enumerate(vehicle_types):
            # Filter data by vehicle type
            recession_vehicle_data = recession_grouped[recession_grouped['Vehicle_Type'] == vehicle]
            non_recession_vehicle_data = non_recession_grouped[non_recession_grouped['Vehicle_Type'] == vehicle]
            
            # Plot recession data with red solid lines
            axes[i].plot(recession_vehicle_data['Year'], recession_vehicle_data['Automobile_Sales'], label='Recession', color='red', linestyle='-')
            
            # Plot non-recession data with default line
            axes[i].plot(non_recession_vehicle_data['Year'], non_recession_vehicle_data['Automobile_Sales'], label='Non-Recession', color='blue', linestyle='--')
            
            # Set title and labels
            axes[i].set_title(f'{vehicle}')
            axes[i].set_ylabel('Sales')
            axes[i].legend()

        # Remove any empty subplots (if the number of vehicle types is odd)
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])

        # Set common labels
        plt.xlabel('Year')
        plt.suptitle('Automobile Sales Trends by Vehicle Type (Recession vs Non-Recession)')
        plt.tight_layout()
        plt.show()
    else:
        print("The 'Recession' column is not present in the dataset.")

# Define the function
def plot_sales_comparison(df):
    # Group the data by Recession and Vehicle_Type and calculate the average Automobile_Sales
    grouped_df = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()

    # Create the bar chart using seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Vehicle_Type', y='Automobile_Sales', hue='Recession', data=grouped_df)

    # Set the labels and title
    plt.xlabel('Vehicle Type')
    plt.ylabel('Average Automobile Sales')
    plt.title('Average Automobile Sales During Recession and Non-Recession Periods')

    # Customize the x-axis labels
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_gdp_variations(df):
    # Filter data based on Recession periods
    rec_data = df[df['Recession'] == 1]
    non_rec_data = df[df['Recession'] == 0]
    
    # Create figure and subplots
    fig = plt.figure(figsize=(12, 6))
    
    # Subplot 1: GDP Variation during Recession Period
    ax0 = fig.add_subplot(1, 2, 1)  # First plot
    sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
    ax0.set_xlabel('Year')
    ax0.set_ylabel('GDP')
    ax0.set_title('GDP Variation during Recession Period')
    
    # Subplot 2: GDP Variation during Non-Recession Period
    ax1 = fig.add_subplot(1, 2, 2)  # Second plot
    sns.lineplot(x='Year', y='GDP', data=non_rec_data, label='Non-Recession', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP')
    ax1.set_title('GDP Variation during Non-Recession Period')
    
    # Adjust layout
    plt.tight_layout()
    plt.show()

def plot_seasonality_bubble_chart(df):
    # יצירת תרשים הבועות
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Month'], df['Automobile_Sales'], s=df['Seasonality_Weight'] * 1000, 
                alpha=0.6, color='blue', edgecolor='black')  # הוספת קווי מתאר שחורים

    # כותרות ותיוגים
    plt.title('Seasonality impact on Automobile Sales', fontsize=14)
    plt.xlabel('Month')
    plt.ylabel('Automobile Sales')
    plt.xticks(rotation=45)

    # הצגת התרשים
    plt.tight_layout()
    plt.show()

def plot_recession_sales_side_by_side(df):
    # Filter data for recession period
    rec_data = df[df['Recession'] == 1]

    # Create a figure with two side-by-side subplots
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    # First subplot: Price vs Automobile Sales during Recession
    ax[0].scatter(rec_data['Price'], rec_data['Automobile_Sales'], alpha=0.7)
    z = np.polyfit(rec_data['Price'], rec_data['Automobile_Sales'], 1)
    p = np.poly1d(z)
    ax[0].plot(rec_data['Price'], p(rec_data['Price']), "r--")
    ax[0].set_xlabel('Average Vehicle Price')
    ax[0].set_ylabel('Automobile Sales')
    ax[0].set_title('Vehicle Price vs Automobile Sales (Recession)')
    ax[0].grid(True)

    # Second subplot: Consumer Confidence vs Automobile Sales during Recession
    ax[1].scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'], alpha=0.7)
    z = np.polyfit(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'], 1)
    p = np.poly1d(z)
    ax[1].plot(rec_data['Consumer_Confidence'], p(rec_data['Consumer_Confidence']), "r--")
    ax[1].set_xlabel('Consumer Confidence')
    ax[1].set_ylabel('Automobile Sales')
    ax[1].set_title('Consumer Confidence vs Automobile Sales (Recession)')
    ax[1].grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()

def plot_advertising_expenditure_pie(df):
    # Filter the data into recession and non-recession periods
    Rdata = df[df['Recession'] == 1]
    NRdata = df[df['Recession'] == 0]

    # Calculate the total advertising expenditure for both periods
    RAtotal = Rdata['Advertising_Expenditure'].sum()
    NRAtotal = NRdata['Advertising_Expenditure'].sum()

    # Create a pie chart for the advertising expenditure 
    plt.figure(figsize=(8, 6))

    labels = ['Recession', 'Non-Recession']
    sizes = [RAtotal, NRAtotal]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])

    plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
    plt.show()

def plot_advertisement_expenditure_by_vehicle_type(df):
    # Filter the data for recession period
    Rdata = df[df['Recession'] == 1]

    # Group by Vehicle_Type and calculate the total advertising expenditure for each vehicle type
    VTexpenditure = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

    # Create a pie chart for the share of each vehicle type in total expenditure during recessions
    plt.figure(figsize=(8, 8))

    labels = VTexpenditure.index
    sizes = VTexpenditure.values
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.title('Share of Each Vehicle Type in Total Advertising Expenditure during Recessions')
    plt.show()

# Call the functions to display the plots
plot_sales_over_time(df)
plot_vehicle_type_trends(df)

# Call the function
plot_sales_comparison(df)

# Call the function
plot_gdp_variations(df)
plot_seasonality_bubble_chart(df)

plot_recession_sales_side_by_side(df)

plot_advertising_expenditure_pie(df)

plot_advertisement_expenditure_by_vehicle_type(df)