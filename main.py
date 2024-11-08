import datetime

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
def display_date_as_stars(day, month, year):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", " *** "],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", " *** ", "    *", "    *"],
        '5': [" *** ", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
        '7': [" *** ", "    *", "   * ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " *** ", "    *", " *** "],
        '-': ["     ", " *** ", "     ", " *** ", "     "]
    }
    
    date_str = f"{day:02d}-{month:02d}-{year}"
    
    rows = [""] * 5
    for char in date_str:
        for i in range(5):
            rows[i] += digits[char][i] + "  "
    for row in rows:
        print(row)

def main():
    # Запрос даты рождения у пользователя
    day = int(input("Введите день рождения (дд): "))
    month = int(input("Введите месяц рождения (мм): "))
    year = int(input("Введите год рождения (гггг): "))
    
    # День недели
    day_of_week = get_day_of_week(day, month, year)
    print(f"День недели рождения: {day_of_week}")
    
    # Проверка на високосный год
    if is_leap_year(year):
        print(f"{year} был високосным годом.")
    else:
        print(f"{year} не был високосным годом.")
    
    # Возраст пользователя
    age = calculate_age(day, month, year)
    print(f"Ваш возраст: {age} лет.")
    
    # Отображение даты звездочками
    print("\nДата рождения в формате дд-мм-гггг:")
    display_date_as_stars(day, month, year)

if __name__ == "__main__":
    main()