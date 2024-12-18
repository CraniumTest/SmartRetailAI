from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Load customer product interaction data
customer_data = pd.read_csv('customer_interaction.csv')

# Train a k-nearest neighbor model
model = NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
model.fit(customer_data)

# Make recommendations for a customer
customer_index = 0  # Example customer index
distances, indices = model.kneighbors([customer_data.iloc[customer_index]])
recommended_products = customer_data.iloc[indices.flatten()]
