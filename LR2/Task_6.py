import requests


def main():
    # Загружаем данные
    url = 'https://www.py4e.com/code3/mbox.txt'
    mbox = requests.get(url).text
    all_lines = mbox.split('\n')

    # Подсчет писем по авторам
    authors = {}
    for line in all_lines:
        if line.startswith("From "):
            parts = line.split()
            if len(parts) > 1:
                email = parts[1]
                authors[email] = authors.get(email, 0) + 1

    if not authors:
        print("Не найдено ни одного адреса.")
        return

    # Находим автора с наибольшим числом писем
    top_author = max(authors.items(), key=lambda x: x[1])

    print()
    print("Список всех авторов и количество писем:")
    for email, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
        print(f"{email}: {count}")

    print(f"\nАвтор, написавший больше всех писем:\n{top_author[0]} — {top_author[1]} писем")


if __name__ == "__main__":
    main()
