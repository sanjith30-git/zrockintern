import pickle
from sklearn.ensemble import RandomForestClassifier

# Function to save the model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Function to load the model
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Sample usage
if __name__ == "__main__":
    # Example: Create and train a random forest model
    model = RandomForestClassifier()
    # Assume you have X_train, y_train
    # model.fit(X_train, y_train)

    # Save the model locally
    save_model(model, 'random_forest_model.pkl')

    # Later, you can load the model
    loaded_model = load_model('random_forest_model.pkl')
