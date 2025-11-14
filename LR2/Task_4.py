def main():
    participants = input().split()
    n = int(input())
    expenses = {name: 0 for name in participants}

    for _ in range(n):
        name, amount = input().split()
        expenses[name] += int(amount)

    total = sum(expenses.values())
    average = total / len(participants)

    balances = {name: round(exp - average, 2) for name, exp in expenses.items()}
    debtors = sorted([(n, -b) for n, b in balances.items() if b < 0], key=lambda x: x[1])
    creditors = sorted([(n, b) for n, b in balances.items() if b > 0], key=lambda x: x[1], reverse=True)

    transfers = []

    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]
        amount = round(min(debt, credit), 2)

        transfers.append((debtor, creditor, amount))

        debtors[i] = (debtor, round(debt - amount, 2))
        creditors[j] = (creditor, round(credit - amount, 2))

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    print()
    print(len(transfers))
    for d, c, a in transfers:
        print(f"{d} {c} {a:.2f}")


if __name__ == "__main__":
    main()
