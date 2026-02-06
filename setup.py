#!/usr/bin/env python3
"""
Интерактивный установщик для моих первых программ
"""

import sys
import os
import platform

def check_python():
    """Проверяет установлен ли Python"""
    print("=" * 50)
    print("Проверка системы...")
    print("=" * 50)
    
    print(f"ОС: {platform.system()} {platform.release()}")
    print(f"Версия Python: {sys.version.split()[0]}")
    
    if sys.version_info < (3, 6):
        print("⚠️  Требуется Python 3.6 или выше!")
        return False
    return True

def show_instructions():
    """Показывает инструкции по запуску"""
    print("\n" + "=" * 50)
    print("📚 ИНСТРУКЦИЯ ПО ЗАПУСКУ")
    print("=" * 50)
    
    instructions = {
        "Windows": """
        1. Откройте командную строку (Win + R → cmd)
        2. Перейдите в папку: cd путь\\к\\папке
        3. Запустите: python start.py
        """,
        
        "Darwin": """  # macOS
        1. Откройте Терминал
        2. Перейдите в папку: cd путь/к/папке
        3. Запустите: python3 start.py
        """,
        
        "Linux": """
        1. Откройте терминал
        2. Перейдите в папку: cd путь/к/папке
        3. Запустите: python3 start.py
        """
    }
    
    os_name = platform.system()
    print(f"\nДля {os_name}:")
    print(instructions.get(os_name, "См. README.md"))
    
    print("\n" + "=" * 50)
    print("📁 Файлы в этом проекте:")
    print("=" * 50)
    
    files = [f for f in os.listdir('.') if f.endswith('.py')]
    for file in files:
        print(f"• {file}")
    
    print("\n🎯 Пример запуска:")
    print('python3 start_advanced.py')
    print('>>> Введите имя и возраст для диалога!')

def main():
    """Основная функция"""
    print("👋 Привет! Это установщик моих первых программ на Python")
    
    if not check_python():
        print("\n❌ Установите Python 3.6+ с python.org")
        return
    
    show_instructions()
    
    # Проверяем, есть ли наши файлы
    required_files = ['start.py', 'start_advanced.py']
    missing = [f for f in required_files if not os.path.exists(f)]
    
    if missing:
        print(f"\n⚠️  Отсутствуют файлы: {', '.join(missing)}")
        print("Скачайте полный проект с GitHub")
    else:
        print("\n✅ Все файлы на месте! Можно запускать.")
    
    print("\n" + "=" * 50)
    print("🚀 Удачи в запуске!")
    print("=" * 50)
    
    # Предлагаем запустить программу
    if input("\nЗапустить start_advanced.py сейчас? (y/n): ").lower() == 'y':
        os.system('python3 start_advanced.py')

if __name__ == "__main__":
    main()