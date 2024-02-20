"""
This is the script where you do the main work
"""
import numpy as np

from mda import LinearRegression


X_train = np.array([1, 2, 3, 4, 5])
y_train = np.array([2, 4, 5, 4, 5])

# Create and fit the model
model = LinearRegression(X_train, y_train)
model.fit()

# Make predictions
X_test = np.array([6, 7, 8])
predictions = model.predict(X_test)

# Print the predictions
print("Predictions:", predictions)