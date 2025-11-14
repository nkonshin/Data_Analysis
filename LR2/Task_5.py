def main():
    n = int(input("Введите количество заказов: "))
    orders = []

    for _ in range(n):
        date, pizza, price = input("Введите дату, пиццу и цену через пробел: ").split()
        orders.append((date, pizza, float(price)))

    # a) частота заказов по пиццам
    pizza_count = {}
    for _, pizza, _ in orders:
        pizza_count[pizza] = pizza_count.get(pizza, 0) + 1

    sorted_pizzas = sorted(pizza_count.items(), key=lambda x: x[1], reverse=True)

    # б) суммарная выручка по датам
    date_sum = {}
    for date, _, price in orders:
        date_sum[date] = date_sum.get(date, 0) + price

    sorted_dates = sorted(date_sum.items(), key=lambda x: x[0])

    # в) самый дорогой заказ
    most_expensive = max(orders, key=lambda x: x[2])

    # г) средняя стоимость заказа
    avg_price = sum(price for _, _, price in orders) / len(orders)

    print()
    print("а) Популярность пицц:")
    for pizza, count in sorted_pizzas:
        print(f"{pizza}: {count}")

    print("\nб) Суммарная выручка по датам:")
    for date, total in sorted_dates:
        print(f"{date}: {total:.2f}")

    print("\nв) Самый дорогой заказ:")
    print(f"Дата: {most_expensive[0]}, Пицца: {most_expensive[1]}, Цена: {most_expensive[2]:.2f}")

    print("\nг) Средняя стоимость заказа:")
    print(f"{avg_price:.2f}")


if __name__ == "__main__":
    main()
