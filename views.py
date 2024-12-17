import numpy as np
import matplotlib.pyplot as plt

def print_data_summary(data):

    """
    Print summary statistics of the dataset.
    
    Parameters:
    - data (ndarray): Input data array.
    """
    
    num_rows, num_cols = data.shape
    print("\n===== Data Summary =====")
    print(f"Number of Rows: {num_rows}")
    print(f"Number of Columns: {num_cols}")
    print(f"Size of data: {data.size}")

def perform_statistical_operations(data):

    """
    Perform statistical operations on the dataset.
    
    Parameters:
    - data (ndarray): Input data array.
    
    Returns:
    - statistics (dict): Dictionary containing mean, 
    median, std, min, max for each column.
    """

    data_cleaned = np.nan_to_num(data, nan=0.0)

    statistics = {
        'mean': np.nanmean(data_cleaned, axis=0),
        'median': np.nanmedian(data_cleaned, axis=0),
        'std': np.nanstd(data_cleaned, axis=0),
        'min': np.nanmin(data_cleaned, axis=0),
        'max': np.nanmax(data_cleaned, axis=0)
    }
    
    print("\n===== Statistical Analysis =====")
    
    column_names = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 
                    'total_bedrooms', 'population', 'households', 'median_income', 
                    'median_house_value', 'ocean_proximity']
    
    for num, column_name in enumerate(column_names):
        print(f"{column_name}:")
        print(f"  Mean: {statistics['mean'][num]:.2f}")
        print(f"  Median: {statistics['median'][num]:.2f}")
        print(f"  Standard Deviation: {statistics['std'][num]:.2f}")
        print(f"  Min: {statistics['min'][num]:.2f}")
        print(f"  Max: {statistics['max'][num]:.2f}")
        print()

    return statistics

def plot_histogram(data):

    """
    Plot histogram of selected columns from the dataset.
    
    Parameters:
    - data (ndarray): Input data array.
    """

    plt.hist(data[:, 3], bins=30, alpha=0.5, color='blue', label='Total Rooms')
    plt.hist(data[:, 4], bins=30, alpha=0.5, color='green', label='Total Bedrooms')
    plt.title('Histogram of Total Rooms and Total Bedrooms')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_scatter_total_rooms_median_house_value(data):

    """
    Plot scatter plot between 'total_rooms' and 'median_house_value'.
    
    Parameters:
    - data (ndarray): Input data array.
    """

    plt.scatter(data[:, 3], data[:, 8], alpha=0.5)
    plt.title('Scatter Plot: Total Rooms vs Median House Value')
    plt.xlabel('Total Rooms')
    plt.ylabel('Median House Value')
    plt.show()

def plot_violin_plot(data):

    """
    Plot violin plot for a column.
    
    Parameters:
    - data (ndarray): Input data array for the column.
    """

    plt.violinplot(data, showmeans=False, showmedians=True)
    plt.title('Violin Plot: Housing Median Age')
    plt.ylabel('Housing Median Age')
    plt.show()

def plot_box_plot(data):

    """
    Plot box plot for selected numerical columns.
    
    Parameters:
    - data (ndarray): Input data array.
    """

    numerical_columns = [3, 4, 5, 6]
    numerical_data = data[:, numerical_columns]
    
    plt.boxplot(numerical_data, vert=False, patch_artist=True)
    plt.title('Box Plot: Numerical Columns')
    plt.xlabel('Value')
    plt.yticks(np.arange(1, len(numerical_columns)+1), ['Total Rooms', 'Total Bedrooms', 'Population',
                                                        'Households'])
    plt.show()

def calculate_population_density(data):

    """
    Calculate population density using 'population' and 'total_rooms' columns.
    
    Parameters:
    - data (ndarray): Input data array.
    
    Returns:
    - population_density (ndarray): Calculated population density.
    """

    population_density = data[:, 5] / data[:, 3]  
    print("Population density: ", population_density)


def plot_average_income(data):

    """
    Plot a histogram of the 'median_income' column.
    
    Parameters:
    - data (ndarray): Input data array.
    """

    plt.hist(data[:, 7], bins=30, alpha=0.5, color='yellow')
    plt.title('Distribution of Median Income')
    plt.xlabel('Median Income')
    plt.ylabel('Number of Households')
    plt.grid(True)
    plt.show()
