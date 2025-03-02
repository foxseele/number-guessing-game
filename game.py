import random
import time

def get_hint(secret_number):
    """Функция для предоставления подсказки."""
    hints = [
        f"Загаданное число ближе к {secret_number - random.randint(1, 10)}.",
        f"Загаданное число делится на {random.choice([x for x in range(1, 11) if secret_number % x == 0])}.",
        f"Загаданное число {'чётное' if secret_number % 2 == 0 else 'нечётное'}."
    ]
    print(random.choice(hints))

def select_level():
    """Выбор уровня сложности."""
    levels = {
        1: {"name": "Лёгкий", "attempts": 10, "key": "easy"},
        2: {"name": "Средний", "attempts": 5, "key": "medium"},
        3: {"name": "Сложный", "attempts": 3, "key": "hard"}
    }
    
    while True:
        print("Выберите уровень сложности:")
        for num, lvl in levels.items():
            print(f"{num}. {lvl['name']} ({lvl['attempts']} попыток)")
        
        try:
            choice = int(input("Введите номер: "))
            if choice in levels:
                return levels[choice]
            else:
                print("Некорректный ввод. Выберите 1, 2 или 3.")
        except ValueError:
            print("Ошибка ввода! Введите число от 1 до 3.")

def play_game(level, records):
    """Основной игровой процесс."""
    secret_number = random.randint(1, 100)
    attempts = level["attempts"]
    level_key = level["key"]
    
    print(f"Отлично! Вы выбрали {level['name']} уровень. У вас есть {attempts} попыток.")
    start_time = time.time()
    
    for attempt in range(1, attempts + 1):
        while True:
            guess = input("Введите число (или 'подсказка' для помощи): ").strip()
            if guess.lower() == 'подсказка':
                get_hint(secret_number)
                continue
            try:
                guess = int(guess)
                if 1 <= guess <= 100:
                    break
                else:
                    print("Число должно быть в диапазоне от 1 до 100.")
            except ValueError:
                print("Ошибка! Введите число или 'подсказка'.")
        
        if guess == secret_number:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Поздравляем! Вы угадали число за {attempt} попыток за {elapsed_time} секунд.")
            
            if attempt < records[level_key]["attempts"] or (
                attempt == records[level_key]["attempts"] and elapsed_time < records[level_key]["time"]):
                records[level_key]["attempts"] = attempt
                records[level_key]["time"] = elapsed_time
                print("Новый рекорд!")
            return
        elif guess < secret_number:
            print("Неверно! Загаданное число больше.")
        else:
            print("Неверно! Загаданное число меньше.")
        
        if attempt < attempts:
            print(f"Осталось попыток: {attempts - attempt}")
        else:
            print(f"Вы проиграли! Загаданное число: {secret_number}.")

def main():
    """Главная функция."""
    print("Добро пожаловать в игру 'Угадай число'!")
    records = {
        "easy": {"attempts": float('inf'), "time": float('inf')},
        "medium": {"attempts": float('inf'), "time": float('inf')},
        "hard": {"attempts": float('inf'), "time": float('inf')}
    }
    
    while True:
        level = select_level()
        play_game(level, records)
        
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            print("Спасибо за игру! Вот ваши рекорды:")
            for lvl, record in records.items():
                if record['attempts'] < float('inf'):
                    print(f"- {lvl.capitalize()}: {record['attempts']} попыток за {record['time']} секунд")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВыход из игры. Пока!")
