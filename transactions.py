#transactions.py
class Transaction():

    def __init__(self, transaction_id, transaction_amount, transaction_type) -> None:
        
        self.transaction_id=transaction_id
        self.transaction_amount=transaction_amount
        self.transaction_type=transaction_type

    def create_transaction(self, amount: float, type: str):
        transaction = {(self.transaction_id): [self.transaction_amount, self.transaction_type]}
        return (transaction)