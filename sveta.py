# ADDRESSBOOK = {}


# def input_error(wrap):
#     def inner(
#         *args,
#     ):  # передаемо аргументи в інер -> то буде наш аргумент data в функціях на яких весить декоратор
#         try:
#             return wrap(*args)
#         except IndexError:
#             return "Give me name and phone please"
#         except ValueError:
#             return "Give me an information"
#         except KeyError:
#             return "Give me the name from phonebook"

#     return inner


# @input_error
# def add_handler(data: list):
#     print(data)
#     name = data[0].title()
#     phone = data[1]
#     ADDRESSBOOK[name] = phone
#     return f"Contact {name} with {phone} was saved"


# @input_error
# def change_handler(data):
#     name = data[0].title()
#     phone = data[1]
#     ADDRESSBOOK[name] = phone
#     return f"Contact {name} with {phone} was saved"


# def exit_handler(*args):
#     return "Goodbye"


# def hello_handler(*args):
#     return "How can I help you?"


# def command_parser(raw_str: str):
#     elements = raw_str.split()
#     for key, value in COMMANDS.items():
#         if elements[0].lower() in value:
#             return key, elements[1:]
#         # тут потрібна перевірка на подвійні команди типу "good bye" зі своїм ретерном
#     # тут ще один return коли такої команди не існуе..продумати то щоб цикл не впав а сказав невідома команда


# COMMANDS = {
#     add_handler: ["add", "+"],
#     exit_handler: ["good bye", "close", "exit"],
#     hello_handler: ["hello"],
#     change_handler: ["change"],
# }


# def main():
#     while True:
#         user_input = input(">>>")  # add name 0987009090
#         if not user_input:
#             continue
#         func, data = command_parser(user_input)
#         result = func(data)
#         print(result)
#         if func == exit_handler:
#             break
#         print(ADDRESSBOOK)


# if __name__ == "__main__":
#     main()
