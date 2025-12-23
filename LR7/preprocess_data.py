#!/usr/bin/env python3
"""
Скрипт для предобработки данных База.csv
Преобразует файл в правильный формат для анализа
"""

import pandas as pd
import numpy as np

print("Загрузка исходного файла...")
df = pd.read_csv('База.csv', sep=';', encoding='windows-1251')

print(f"Загружено {len(df)} строк, {len(df.columns)} столбцов")

# Функция для конвертации чисел с запятой
def convert_numeric(x):
    """Преобразует строковые числа с запятой в float"""
    if pd.isna(x):
        return np.nan
    if isinstance(x, str):
        x = x.replace(',', '.').strip()
        try:
            return float(x)
        except:
            return np.nan
    return float(x)

# Преобразуем числовые столбцы
numeric_cols = ['ПродаваемаяПлощадь', 'Этаж', 'СтоимостьНаДатуБрони', 
                'СкидкаНаКвартиру', 'ФактическаяСтоимостьПомещения']

print("\nПреобразование числовых столбцов...")
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].apply(convert_numeric)
        print(f"  ✓ {col}")

# Преобразуем столбец Тип (количество комнат)
# Оставляем как строку, но заменяем запятую на точку
# Парсинг будет в notebook
if 'Тип' in df.columns:
    df['Тип'] = df['Тип'].astype(str).str.replace(',', '.')
    print(f"  ✓ Тип (заменена запятая на точку)")

# Сохраняем
output_file = 'База_clean.csv'
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"\n✓ Файл сохранен: {output_file}")
print(f"  Кодировка: UTF-8")
print(f"  Разделитель: запятая")
print(f"  Размер: {len(df)} строк")
