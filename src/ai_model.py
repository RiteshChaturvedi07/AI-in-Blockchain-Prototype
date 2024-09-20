# ai_model.py

import numpy as np
from sklearn.ensemble import IsolationForest

# Simulated transaction data (features could include transaction amount, frequency, etc.)
transaction_data = np.array([[100, 2], [200, 3], [150, 1], [10000, 20], [50, 0.5]])

# Train Isolation Forest to detect anomalies
model = IsolationForest(contamination=0.2)
model.fit(transaction_data)

# Predict anomalies (fraud)
predictions = model.predict(transaction_data)
print("Anomalies: ", predictions)  # -1 indicates fraud, 1 indicates normal transactions
