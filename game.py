import random
import time

# Словарь для хранения рекордов (минимальное количество попыток для каждого уровня)
records = {
    "easy": {"attempts": float('inf'), "time": float('inf')},
    "medium": {"attempts": float('inf'), "time": float('inf')},
    "hard": {"attempts": float('inf'), "time": float('inf')}
}

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    
    while True:
        # Выбор уровня сложности
        print("\nВыберите уровень сложности:")
        print("1. Легкий (10 попыток)")
        print("2. Средний (5 попыток)")
        print("3. Сложный (3 попытки)")
        
        while True:
            try:
                difficulty = int(input("Введите номер: "))
                if difficulty == 1:
                    attempts = 10
                    level = "easy"
                    break
                elif difficulty == 2:
                    attempts = 5
                    level = "medium"
                    break
                elif difficulty == 3:
                    attempts = 3
                    level = "hard"
                    break
                else:
                    print("Пожалуйста, выберите корректный уровень сложности (1, 2 или 3).")
            except ValueError:
                print("Пожалуйста, введите число.")
        
        print(f"Отлично! Вы выбрали {'легкий' if difficulty == 1 else 'средний' if difficulty == 2 else 'сложный'} уровень сложности.")
        print(f"У вас есть {attempts} попыток.")
        
        # Загадываем число
        secret_number = random.randint(1, 100)
        print("Начинаем игру!")
        
        # Запускаем таймер
        start_time = time.time()
        
        # Основной игровой цикл
        for attempt in range(1, attempts + 1):
            while True:
                try:
                    guess = input("Введите число (или 'подсказка', чтобы получить помощь): ")
                    if guess.lower() == 'подсказка':
                        give_hint(secret_number)
                        continue
                    guess = int(guess)
                    if 1 <= guess <= 100:
                        break
                    else:
                        print("Число должно быть в диапазоне от 1 до 100.")
                except ValueError:
                    print("Пожалуйста, введите целое число или 'подсказка'.")
            
            # Проверка угаданного числа
            if guess == secret_number:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)
                print(f"Поздравляем! Вы угадали число за {attempt} попыток!")
                print(f"Время, затраченное на угадывание: {elapsed_time} секунд.")
                
                # Обновление рекорда
                if attempt < records[level]["attempts"] or (attempt == records[level]["attempts"] and elapsed_time < records[level]["time"]):
                    records[level]["attempts"] = attempt
                    records[level]["time"] = elapsed_time
                    print(f"Новый рекорд для этого уровня: {attempt} попыток за {elapsed_time} секунд!")
                break
            elif guess < secret_number:
                print("Неверно! Загаданное число больше.")
            else:
                print("Неверно! Загаданное число меньше.")
            
            # Вывод оставшихся попыток
            remaining_attempts = attempts - attempt
            if remaining_attempts > 0:
                print(f"Осталось попыток: {remaining_attempts}")
            else:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)
                print(f"К сожалению, вы исчерпали все попытки. Загаданное число было: {secret_number}.")
                print(f"Время, затраченное на угадывание: {elapsed_time} секунд.")
        
        # Предложение сыграть ещё раз
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != 'да':
            print("\nСпасибо за игру! Вот ваши рекорды:")
            for lvl, record in records.items():
                print(f"- {lvl.capitalize()}: {record['attempts']} попыток за {record['time']} секунд")
            break

def give_hint(secret_number):
    """Функция для предоставления подсказки."""
    hints = [
        f"Загаданное число ближе к {secret_number - random.randint(1, 10)}.",
        f"Загаданное число делится на {random.choice([x for x in range(1, 11) if secret_number % x == 0])}.",
        f"Загаданное число {'чётное' if secret_number % 2 == 0 else 'нечётное'}."
    ]
    print(random.choice(hints))

if __name__ == "__main__":
    main()