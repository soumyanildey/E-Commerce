import pickle

# Load the Item Based recommendations list
with open('ml_model\ItemBase.pkl', 'rb') as file:
    item_based_results = pickle.load(file)

# Load the Matrix Factorization recommendations list
with open('ml_model\MatFac.pkl', 'rb') as file:
    matrix_factorization_results = pickle.load(file)

def load_model_results():
    # Find the intersection of the two lists
    intersection_items = list(set(item_based_results) & set(matrix_factorization_results))
    
    # Print the intersection items to the console
    print("Intersection of Recommended Items:", intersection_items)
    
    return intersection_items

# Call the function and print the result
load_model_results()