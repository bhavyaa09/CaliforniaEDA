import views
import services
from enum_1 import MenuOption

def print_menu():

    """
    Print the menu of operations.
    """

    print("\n===== Operations =====")
    print("1. Print data summary")
    print("2. Perform statistical operations")
    print("3. Plot histogram of total rooms and total bedrooms")
    print("4. Plot scatter plot between total rooms and median house value")
    print("5. Plot violin plot for housing median age")
    print("6. Plot box plot for numerical columns")
    print("7. Print population density")
    print("8. Plot Average Income of Median Income")
    print("9. Exit")

def get_menu_choice(user_input):

    """
    Convert user input to MenuOption enum.
    """
    
    try:
        choice = int(user_input)
        return MenuOption(choice)
    except (ValueError, KeyError):
        return None

def main():
    
    print("\nCalifornia Housing Exploratory Data Analysis")
    print("*" * 45)
    file_path = 'data/housing.csv' 

    data = services.load_data(file_path)
    
    if data is None:
        print("Exiting program.")
        return
    
    print("Data loaded successfully.")
    print("Missing values Handled sucessfully.")
    print("You can go further with your analysis")
    print("*" * 45)
    
    while True:
        print_menu()
        user_input = input("Enter the number of that operation you want to perform: ")
        
        choice = get_menu_choice(user_input)
        
        match choice:
            case MenuOption.PRINT_DATA_SUMMARY:
                print("\nPrinting data summary...")
                views.print_data_summary(data)
            
            case MenuOption.PERFORM_STATISTICAL_OPERATIONS:
                print("\nPerforming statistical operations...")
                views.perform_statistical_operations(data)
            
            case MenuOption.PLOT_HISTOGRAM:
                print("\nPlotting histogram of total rooms and total bedrooms...")
                views.plot_histogram(data)
            
            case MenuOption.PLOT_SCATTER_PLOT:
                print("\nPlotting scatter plot between total rooms and median house value...")
                views.plot_scatter_total_rooms_median_house_value(data)
            
            case MenuOption.PLOT_VIOLIN_PLOT:
                print("\nPlotting violin plot for housing median age...")
                views.plot_violin_plot(data[:, 2])
            
            case MenuOption.PLOT_BOX_PLOT:
                print("\nPlotting box plot for numerical columns...")
                views.plot_box_plot(data)
            
            case MenuOption.CALCULATE_POPULATION_DENSITY:
                views.calculate_population_density(data)
                
            case MenuOption.PLOT_AVERAGE_INCOME:
                views.plot_average_income(data)

            case MenuOption.EXIT:
                print("Exiting.....")
                break
            
            case _:
                print("Invalid choice. Please enter a valid option number.")

if __name__ == "__main__":
    main()
