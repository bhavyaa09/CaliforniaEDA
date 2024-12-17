import numpy as np

def load_data(file_path):
    
    """
    Load data from a CSV file.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    
    Returns:
    - data (ndarray or None): Loaded data as numpy array or None if file not found.
    """
    
    try:
        data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
        return data
    except IOError:
        print(f"Error: File '{file_path}' not found.")
        return None
