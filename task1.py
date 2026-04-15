# tasks/task1.py

def solve():
# Ниже пишите решение задачи
   # Ввод общего количества журавликов
    S = int(input())
    # Решение:
    # Пусть Петя = x, Сережа = x, тогда Катя = 2*(x + x) = 4x
    # Всего: x + x + 4x = 6x = S
    # Отсюда x = S // 6
    
    petya = S // 6
    serezha = petya
    katya = 4 * petya
    
    # Вывод результата (Петя, Катя, Сережа)
    print(petya, katya, serezha)  
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()