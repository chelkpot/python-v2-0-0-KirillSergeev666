# Задание 1. Журавлики

def solve():
    # Ввод данных
    S = int(input())
    
    # Вычисление количества журавликов
    petya = S // 6
    serezha = petya
    katya = 4 * petya
    
    # Вывод результата
    print(petya, katya, serezha)

if __name__ == "__main__":
    solve()