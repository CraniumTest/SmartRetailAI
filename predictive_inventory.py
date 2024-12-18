import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load sample sales data
data = pd.read_csv('historical_sales.csv')
X = data[['features']]  # Example: Previous sales, promotion, etc.
y = data['sales']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future sales
predictions = model.predict(X_test)
