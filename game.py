import random
import time

class Game:
    """Основной класс игры 'Угадай число'"""
    
    # Константы для настроек игры
    DIFFICULTY_LEVELS = {
        1: {"code": "easy", "name": "Легкий", "attempts": 10, "hint_chance": 0.5},
        2: {"code": "medium", "name": "Средний", "attempts": 5, "hint_chance": 0.3},
        3: {"code": "hard", "name": "Сложный", "attempts": 3, "hint_chance": 0.1}
    }
    
    def __init__(self):
        """Инициализация игры"""
        self.records = {level["code"]: {"attempts": float('inf'), "time": float('inf')} 
                       for level in self.DIFFICULTY_LEVELS.values()}
        self.secret_number = None
        self.current_level = None
        self.start_time = None

    def run(self):
        """Основной цикл игры"""
        print("Добро пожаловать в игру 'Угадай число'!")
        
        while True:
            self.select_difficulty()
            self.generate_secret_number()
            self.play()
            
            if not self.ask_play_again():
                self.show_records()
                break

    def select_difficulty(self):
        """Выбор уровня сложности"""
        while True:
            print("\nВыберите уровень сложности:")
            for num, level in self.DIFFICULTY_LEVELS.items():
                print(f"{num}. {level['name']} ({level['attempts']} попыток)")
                
            try:
                choice = int(input("Введите номер: "))
                if 1 <= choice <= 3:
                    level_data = self.DIFFICULTY_LEVELS[choice]
                    self.current_level = level_data['code']  # Используем код уровня
                    self.attempts_left = level_data['attempts']
                    break
                print("Пожалуйста, введите число от 1 до 3")
            except ValueError:
                print("Некорректный ввод. Введите число.")

    def generate_secret_number(self):
        """Генерация случайного числа и запуск таймера"""
        self.secret_number = random.randint(1, 100)
        self.start_time = time.time()
        print(f"\nЗагадано число от 1 до 100. У вас {self.attempts_left} попыток!")

    def play(self):
        """Основной игровой процесс"""
        for attempt in range(1, self.attempts_left + 1):
            guess = self.get_user_input(attempt)
            
            if self.check_guess(guess, attempt):
                return
                
        self.game_over()

    def get_user_input(self, attempt):
        """Обработка пользовательского ввода"""
        while True:
            user_input = input(f"Попытка {attempt}: Введите число (или 'подсказка'): ").lower()
            
            if user_input == 'подсказка':
                self.show_hint()
                continue
                
            if user_input.isdigit():
                return int(user_input)
                
            print("Введите число от 1 до 100 или 'подсказка'")

    def check_guess(self, guess, attempt):
        """Проверка угаданного числа"""
        if guess == self.secret_number:
            self.process_win(attempt)
            return True
            
        print("Загаданное число больше" if guess < self.secret_number else "Загаданное число меньше")
        return False

    def process_win(self, attempt):
        """Обработка победы"""
        elapsed_time = round(time.time() - self.start_time, 2)
        print(f"\nПоздравляем! Вы угадали число за {attempt} попыток и {elapsed_time} секунд!")
        
        if self.is_new_record(attempt, elapsed_time):
            self.update_record(attempt, elapsed_time)
            print(f"Новый рекорд для уровня {self.current_level}!")

    def is_new_record(self, attempts, time):
        """Проверка на новый рекорд"""
        current_record = self.records[self.current_level]
        return (attempts < current_record["attempts"] or 
                (attempts == current_record["attempts"] and time < current_record["time"]))

    def update_record(self, attempts, time):
        """Обновление рекорда"""
        self.records[self.current_level] = {"attempts": attempts, "time": time}

    def game_over(self):
        """Завершение игры при исчерпании попыток"""
        elapsed_time = round(time.time() - self.start_time, 2)
        print(f"\nК сожалению, вы проиграли. Загаданное число было {self.secret_number}")
        print(f"Затраченное время: {elapsed_time} секунд")

    def show_hint(self):
        """Генерация и вывод подсказки"""
        if random.random() < self.DIFFICULTY_LEVELS[self.current_level]['hint_chance']:
            hints = [
                f"Число оканчивается на {self.secret_number % 10}",
                f"Сумма цифр: {sum(map(int, str(self.secret_number)))}",
                f"{'Четное' if self.secret_number % 2 == 0 else 'Нечетное'} число",
                f"Ближе к {self.secret_number + random.randint(-10, 10)}"
            ]
            print("\nПодсказка: " + random.choice(hints))
        else:
            print("К сожалению, сейчас подсказка недоступна")

    def ask_play_again(self):
        """Предложение сыграть снова"""
        return input("\nХотите сыграть еще раз? (да/нет): ").lower() == 'да'

    def show_records(self):
        """Вывод рекордов"""
        print("\nВаши лучшие результаты:")
        for level, record in self.records.items():
            print(f"{level.capitalize()}: {record['attempts']} попыток за {record['time']} секунд")

if __name__ == "__main__":
    game = Game()
    game.run()