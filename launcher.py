import subprocess
import time

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна: ')
    if action == 'q':
        break
    elif action == 's':
        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        # Запускаем сервер!
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        time.sleep(5)   # задержка из-за длинного вывода используемых методов и атрибутов в метаклассе ServerMaker
        # Запускаем клиентов:
        for i in range(clients_count):
            process.append(subprocess.Popen(f'python client.py -n test{i + 1}',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        while process:
            process.pop().kill()
