import pytest
from src.transaction_manager import Transaction, TransactionManager

def test_add_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    assert manager.get_transaction('1') == transaction

def test_remove_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    manager.remove_transaction('1')
    assert manager.get_transaction('1') is None

def test_get_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    assert manager.get_transaction('1') == transaction

def test_get_all_transactions():
    manager = TransactionManager()
    transaction1 = Transaction('1', 'Test transaction 1', 100.0, '2024-07-24')
    transaction2 = Transaction('2', 'Test transaction 2', 200.0, '2024-07-25')
    manager.add_transaction(transaction1)
    manager.add_transaction(transaction2)
    assert manager.get_all_transactions() == [transaction1, transaction2]

def test_add_duplicate_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    with pytest.raises(ValueError):
        manager.add_transaction(transaction)

def test_remove_non_existent_transaction():
    manager = TransactionManager()
    with pytest.raises(ValueError):
        manager.remove_transaction('1')