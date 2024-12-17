from enum import Enum, auto

class MenuOption(Enum):
    
    """
    Enumeration for the different menu options available in the application.

    Attributes:
        PRINT_DATA_SUMMARY: Option to print a summary of the data.
        PERFORM_STATISTICAL_OPERATIONS: Option to perform statistical operations on the data.
        PLOT_HISTOGRAM: Option to generate a histogram plot of the data.
        PLOT_SCATTER_PLOT: Option to generate a scatter plot of the data.
        PLOT_VIOLIN_PLOT: Option to generate a violin plot of the data.
        PLOT_BOX_PLOT: Option to generate a box plot of the data.
        CALCULATE_POPULATION_DENSITY: Option to calculate and display population density.
        PLOT_AVERAGE_INCOME: Option to plot the average income from the data.
        EXIT: Option to exit the application.
    """
    
    PRINT_DATA_SUMMARY = auto()
    PERFORM_STATISTICAL_OPERATIONS = auto()
    PLOT_HISTOGRAM = auto()
    PLOT_SCATTER_PLOT = auto()
    PLOT_VIOLIN_PLOT = auto()
    PLOT_BOX_PLOT = auto()
    CALCULATE_POPULATION_DENSITY = auto()
    PLOT_AVERAGE_INCOME = auto()
    EXIT = auto()
