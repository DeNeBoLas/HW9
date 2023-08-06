ADDRESSBOOK = {}


def input_error(wrap):
    def inner(
        *args,
    ):  # передаемо аргументи в інер -> то буде наш аргумент data в функціях на яких вuсить декоратор
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
        except ValueError:
            return "Give me an information"
        except KeyError:
            return "Give me the name from phonebook"

    return inner


@input_error
def add_handler(data: list):
    print(data)
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with {phone} was saved"


@input_error
def change_handler(data):  # зберігає в пам'яті новий номер телефону існуючого контакту
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with {phone} was changed"


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you?"


@input_error
def phone(data):  # тут після инпуту і парсера зайде список
    name = data[0].title()
    phone = ADDRESSBOOK.get(name)
    if phone != None:
        return f"{name}: number {phone}"
    return "no name"


def show_all(*args):  # виводить всі збереженні контакти з номерами телефонів у консоль
    result = [
        f"Name: {name} -->> number {phone}" for name, phone in ADDRESSBOOK.items()
    ]
    return "\n".join(result)


def error(*args):
    return "Unknown command"


def command_parser(raw_str: str):
    elements = raw_str.split(" ")
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements[1:]
        elif " ".join(elements[:2]).lower() in value:
            return key, elements[2:]
    return error, None


COMMANDS = {
    add_handler: ["add", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    phone: ["phone"],
    show_all: ["show all"],
}


def main():
    while True:
        user_input = input(">>>")
        if not user_input:
            continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        # print(ADDRESSBOOK)


if __name__ == "__main__":
    main()
