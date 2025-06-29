import random

class Card:
    def __init__(self):
        self.rows = self._generate_card()
        self.marked = set()

    def _generate_card(self):
        numbers = random.sample(range(1, 91), 15)
        numbers.sort()
        card = []
        for i in range(3):
            row_nums = sorted(numbers[i*5:(i+1)*5])
            row = [''] * 9
            positions = random.sample(range(9), 5)
            for pos, num in zip(sorted(positions), row_nums):
                row[pos] = num
            card.append(row)
        return card

    def has_number(self, number):
        for row in self.rows:
            if number in row:
                return True
        return False

    def mark_number(self, number):
        for row in self.rows:
            for i in range(9):
                if row[i] == number:
                    row[i] = '-'
                    self.marked.add(number)

    def is_complete(self):
        return len(self.marked) == 15

    def __str__(self):
        s = '-'*26 + '\n'
        for row in self.rows:
            s += ' '.join(f'{str(x):>2}' if x != '' else '  ' for x in row) + '\n'
        s += '-'*26
        return s

class Barrel:
    def __init__(self):
        self.barrels = list(range(1, 91))
        random.shuffle(self.barrels)

    def draw(self):
        if self.barrels:
            return self.barrels.pop()
        return None

    def remaining(self):
        return len(self.barrels)

class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card()

    def has_won(self):
        return self.card.is_complete()

class Game:
    def __init__(self):
        self.user = Player('Вы')
        self.comp = Player('Компьютер')
        self.barrel = Barrel()

    def play(self):
        while True:
            number = self.barrel.draw()
            if number is None:
                print('Бочонки закончились! Ничья!')
                break
            print(f'Новый бочонок: {number} (осталось {self.barrel.remaining()})')
            print('------ Ваша карточка -----')
            print(self.user.card)
            print('-- Карточка компьютера ---')
            print(self.comp.card)
            answer = input('Зачеркнуть цифру? (y/n) ')
            if answer.lower() == 'y':
                if self.user.card.has_number(number):
                    self.user.card.mark_number(number)
                else:
                    print('Числа нет на вашей карточке. Вы проиграли!')
                    break
            else:
                if self.user.card.has_number(number):
                    print('Число было на вашей карточке. Вы проиграли!')
                    break
            if self.comp.card.has_number(number):
                self.comp.card.mark_number(number)
            if self.user.has_won():
                print('Вы выиграли!')
                break
            if self.comp.has_won():
                print('Компьютер выиграл!')
                break


Game().play()
