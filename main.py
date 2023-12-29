import warnings
from tabulate import tabulate
from colorama import Fore, Style

import universal
import t

warnings.filterwarnings("ignore")

board = [[0 for _ in range(10)] for _ in range(10)]
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
invis_board = [[str(0) for _ in range(10)] for _ in range(10)]


def game():
    score = 0
    step = 0
    t.place_ships(board, ships)
    formatted_table = tabulate(board, tablefmt="fancy_grid") # для разраба отображает расстановку фигур
    print(formatted_table) # для разраба отображает расстановку фигур
    while sum(row.count(0) for row in board) < 100:
        formatted_table_inv = tabulate(invis_board, tablefmt="fancy_grid")
        formatted_table_inv = formatted_table_inv.replace("Х", f"{Fore.RED}X{Style.RESET_ALL}")
        print(formatted_table_inv)
        ch_row = int(input("Введите номер строки: "))
        choose_it = int(input("Введите номер элемента строки: "))
        if board[ch_row][choose_it] != 0:
            score += board[ch_row][choose_it]
            step += 1
            if 1 < board[ch_row][choose_it] <= 4:
                value_to_check = board[ch_row][choose_it]
                board[ch_row][choose_it] = 0
                invis_board[ch_row][choose_it] = "Х"  # Изменяем значение на "X"
                count_of_value = sum(row.count(value_to_check) for row in board)
                if count_of_value == 0 and value_to_check == 4:
                    print("Корабль уничтожен")
                elif (count_of_value % 3 == 0 or count_of_value == 0) and value_to_check == 3:
                    print("Корабль уничтожен")
                elif (count_of_value % 2 == 0 or count_of_value == 0) and value_to_check == 2:
                    print("Корабль уничтожен")
                else:
                    print("Есть пробитие")
            else:
                board[ch_row][choose_it] = 0
                invis_board[ch_row][choose_it] = "Х"
                print("Корабль уничтожен")
        else:
            print("Мимо!")
    print("Игра закончена !")
    print("Шагов сделано: ", step)
    return step


def main():
    run = True
    commands = """==========================================================================
1. Вывести доску.
2. Начать новую игру.
6. Завершить сеанс"""
    while run:
        run = universal.uni(commands, game)
    return


if __name__ == '__main__':
    main()
