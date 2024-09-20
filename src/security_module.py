# security_module.py

from blockchain import Blockchain
from ai_model import model, transaction_data

blockchain = Blockchain()

def validate_transaction(transaction):
    prediction = model.predict([transaction])
    if prediction == -1:
        print("Transaction flagged as fraud!")
    else:
        blockchain.new_transaction(transaction[0], transaction[1], transaction[2])
        print("Transaction added to blockchain.")

# Test transaction
test_transaction = [150, 1]
validate_transaction(test_transaction)
