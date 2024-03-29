from sys import argv, exit


def arg_tester():
    args = argv[1:]
    if len(args) != 2:
        print("erreur d'arguments !")
        exit()

    return args


def split_by(string_to_cut, separator):
    
    words = [word for word in string_to_cut if word != separator]
    return words



def main():
    arguments = arg_tester()
    # print(f"arguments: {arguments}")
    string_to_cut = arguments[0].split(" ")
    words = split_by(string_to_cut, arguments[1])

    for word in words:
        print(word)


main()
