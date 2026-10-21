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
        raise InvalidAmountError(f"Сумма должна быть положительной: {amount}")
    if amount > balance:
        raise InsufficientFundsError(f"Недостаточно средств: баланс {balance}, запрошено {amount}")
    return balance - amount


def main():
    balance = 1000
    while True:
        raw = input(f"Баланс: {balance}. Сумма для снятия (или 'q'): ").strip()
        if raw.lower() == 'q':
            break
        try:
            amount = float(raw)
        except ValueError:
            print("Это не число")
            continue
        try:
            balance = withdraw(balance, amount)
        except InvalidAmountError as e:
            print(f"Некорректная сумма: {e}")
        except InsufficientFundsError as e:
            print(f"Отказ: {e}")
        except BankError as e:
            print(f"Ошибка банка: {e}")
        else:
            print(f"Снято {amount}, новый баланс: {balance}")


if __name__ == "__main__":
    main()
