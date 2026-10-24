class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма должна быть положительной")
    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств")
    return balance - amount


if __name__ == "__main__":
    for amount in (30, 0, 500):
        try:
            print(f"Новый баланс: {withdraw(100, amount)}")
        except BankError as error:
            print(f"{type(error).__name__}: {error}")
