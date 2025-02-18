import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # Load the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars94_miss.csv')

    # Drop rows where the price is missing
    df.dropna(subset=['Price'], inplace=True)

    # Split the dataset into features and target
    X = df.drop(['Price', 'Name'], axis=1)
    y = df['Price']

    # Return the preprocessed data
    return X, y

def split_data(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Return the splitted data
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)