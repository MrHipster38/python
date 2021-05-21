import random

class LotoCard:
    def __init__(self, player_type):
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())
        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stoke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBER_IN_CARD:
                        raise Exception(f'{self.player_type} победил!')
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LEN = 3
        header = f'\n{self.player_type}:\n'
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LEN)
            body += '\n'
        return header + body

class Game:
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        self._MAX_NUMBER = 90
        self.bag = random.sample(range(1, self._MAX_NUMBER+1), self._MAX_NUMBER)
    def start(self):
        for number in self.bag:
            print(f'Новый бочонок {number}')
            print(self.human.__str__())
            print(self.computer.__str__())
            self.answer = input(f'Зачеркнуть цифру?  Y/N ')
            LotoCard.try_stoke_number(self.computer, number)
            if self.answer == 'Y':
                if not LotoCard.try_stoke_number(self.human, number):
                    raise Exception('ВЫ ПРОИГРАЛИ')
                else: pass
            else:
                if LotoCard.try_stoke_number(self.human, number):
                    raise Exception('ВЫ ПРОИГРАЛИ')
                else: pass
            print('\n' * 5)

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = Game(human_player, computer_player)
game.start()
