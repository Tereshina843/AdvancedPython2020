import re
import fileinput

'''
Обозначения:

• [абв] - в квадратных скобках <=> один символ из записанных
• \s    - любой пробельный символ (пробел, таб и т.п.)
• *,+   - служебные символы, означают что выражение слева (в нашем случае просто символ) всетречается какое-то число раз
          * значит 0 и более, + значит 1 и более. Например \s* значит, что подряд идет 0 и более пробелов
• \d    - любая цифра (\d+ это 1 и более подряд идущих цифр, т.е. число)
• |     - разделение регулярных выражений. Т.е. Проверяется сначала первоеб до черты. Потом второе, до следующей черты. 
          И т.д.   

Функции:

• re.findall (регулярное_выражение, строка_в_которой_ищем) - возвращает список всех подстрок, подошедших под выражение
• fileinput.input()                                        - список всех введенных в консоли строк. Т.е. - можешь сразу
                                                             вставить весь текст и ввести ctrl+D - обозначение конца 
'''

money_values = []
book_titles = []

print("Enter text ... (end with ctrl+D)")
for line in fileinput.input():
    money_values.extend(re.findall(r'[€$]\s*\d+|\d+\s*₽', line))

    book_titles.extend(re.findall(r'«.*»', line))

print("Money values: ", money_values)
print()
print("Book titles: ", book_titles)