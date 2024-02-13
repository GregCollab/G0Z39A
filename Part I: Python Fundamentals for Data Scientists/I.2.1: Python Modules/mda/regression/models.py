"""
This module contains the regression models used in the lecture
"""
import numpy as np


class LinearRegression:
    def __init__(self, X, y):
        """
        Initialize the Linear Regression model.

        Parameters:
        - X (numpy.ndarray): Input features.
        - y (numpy.ndarray): Target values.
        """
        # Add a column of ones to X for the bias term
        self.X = np.column_stack((np.ones(len(X)), X))
        self.y = y.reshape(-1, 1)
        self.theta = None  # Model parameters

    def fit(self):
        """
        Fit the Linear Regression model using the normal equation.
        """
        # Calculate the parameters using the normal equation
        # theta = (X^T * X)^-1 * X^T * y
        X_transpose = np.transpose(self.X)
        self.theta = np.linalg.inv(X_transpose @ self.X) @ X_transpose @ self.y

    def predict(self, X):
        """
        Make predictions using the trained Linear Regression model.

        Parameters:
        - X (numpy.ndarray): Input features for prediction.

        Returns:
        - numpy.ndarray: Predicted values.
        """
        # Add a column of ones to X for the bias term
        X_with_bias = np.column_stack((np.ones(len(X)), X))
        # Make predictions
        predictions = X_with_bias @ self.theta
        return predictions.flatten()
    

if __name__ == '__main__':
    # Useful for testing and debugging! 
    print("This will only run if I run the module directly")