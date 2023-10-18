from sys import argv, exit


def arg_tester():
    args = argv[1:]

    if len(args) < 3:
        print("erreur d'argument")
        exit()

    return args


def concat_by(array, separator):
    words = [word + separator for word in array]
    # print(words)

    return words


def main():
    argument = arg_tester()
    separator = argument[-1]
    array_to_concat = argument[:-1]

    sentence = "".join(concat_by(array_to_concat, separator))

    print(sentence)


main()
    
