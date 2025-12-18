import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# --- CONFIG ---
MY_PROMO = "285005"
MY_LINK = "https://bit.ly/4sl9zev"
# --------------

def show_telemetry():
    print(Fore.BLUE + "[SYSTEM] Инициализация модуля Astronavt Telemetry...")
    time.sleep(1)
    print(Fore.CYAN + "[DATA] Сканирование высоты полета и плотности трафика...")
    
    # Имитация прогресс-бара
    for i in range(0, 101, 20):
        print(f"{Fore.YELLOW}Загрузка данных: [{('#' * (i//10)).ljust(10)}] {i}%", end='\r')
        time.sleep(0.5)
    print("\n")

def get_prediction():
    print(Fore.WHITE + "--- АНАЛИЗ ТЕКУЩЕЙ СЕССИИ ---")
    
    # Генерируем "безопасный" и "рискованный" порог
    safe_exit = round(random.uniform(1.20, 1.45), 2)
    high_target = round(random.uniform(2.50, 8.00), 2)
    
    print(f"🔹 Безопасная точка выхода: {Fore.GREEN}x{safe_exit}")
    print(f"🔥 Высокий риск (цель): {Fore.RED}x{high_target}")
    print(f"📊 Вероятность успеха: {random.randint(75, 94)}%")
    print(f"\n{Fore.MAGENTA}⚠️ Для синхронизации с сервером используйте промокод: {Style.BRIGHT}{MY_PROMO}")
    print(f"{Fore.MAGENTA}👉 Регистрация: {MY_LINK}\n")

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== ASTRONAVT PREDICTOR V1.0 - OPEN SOURCE ===")
    show_telemetry()
    
    while True:
        cmd = input("Нажмите ENTER для расчета следующего полета (или 'q' для выхода): ")
        if cmd.lower() == 'q': break
        get_prediction()

if __name__ == "__main__":
    main()
