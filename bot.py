

def add_handler(data):
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return args


def add_handler(*args):
    return 'Goodbye'

def add_handler(*args):
    return 'Hello'

COMMANDS = [
    add_handler: ['add', '+']
    exit_handler: ["good bye", "close", "exit" ]
    hello_handler: ['hello']
]

def command_parser(raw_str: str) -> list:
    items = raw_str.split()
    for key, value in COMMANDS.items()
    if items[0].lower() in value:
        return key, items[1:]


def main():
    while True:
        user_input = input('>>>') # add name 0987009090
        if not user_input:
            continue
        else:

        func, data:list - command_parser(user_input)
        print(func)
        result = func(data)
        print(result)

if __name__ == '__main__':
    main()
