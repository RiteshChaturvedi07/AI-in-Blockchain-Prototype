# test_ai_model.py

from ai_model import model, transaction_data

def test_ai_model():
    # Simulate a test with fraudulent and normal transactions
    test_data = [[100, 2], [10000, 20], [150, 1]]  # Normal, Fraud, Normal transactions
    expected = [1, -1, 1]  # Expected predictions (1: Normal, -1: Fraud)

    predictions = model.predict(test_data)
    assert (predictions == expected).all(), f"Expected {expected}, but got {predictions}"

    print("AI model test passed!")

if __name__ == "__main__":
    test_ai_model()
