import http.server
import socketserver
import socket

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Перенаправляем на index.html
        return super().do_GET()

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Привязываемся к любому свободному порту
        return s.getsockname()[1]  # Возвращаем номер порта

# Переменная для включения/выключения функции выбора языка
enable_language_choice = True  # Установите False, чтобы отключить выбор языка

# Функция для выбора языка
def choose_language():
    lang = input("Choose language / Выберите язык (en/ru): ").strip().lower()
    if lang not in ['en', 'ru']:
        print("Invalid choice. Defaulting to English.")
        lang = 'en'
    return lang

# Получаем язык, если функция включена
if enable_language_choice:
    language = choose_language()
else:
    language = 'en'  # По умолчанию английский

# Сообщения в зависимости от языка
if language == 'en':
    start_message = "Server started at http://{}:{}"
else:
    start_message = "Сервер запущен на http://{}:{}"

PORT = find_free_port()  # Генерируем случайный свободный порт
Handler = CustomHTTPRequestHandler

# Получаем IP-адрес машины в локальной сети
HOST = '0.0.0.0'  # Привязываемся ко всем интерфейсам

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(start_message.format(socket.gethostbyname(socket.gethostname()), PORT))
    httpd.serve_forever()
