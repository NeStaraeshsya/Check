import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Генератор паролей")
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): "))
        if length <= 0:
            print("Длина должна быть положительным числом.")
            return
    except ValueError:
        length = 12
    password = generate_password(length)
    print(f"Сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()