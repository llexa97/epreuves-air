from sys import argv, exit


def arg_tester():
    args = argv[1:]

    if len(args) < 3:
        print("erreur d'arguments !")
        exit()

    return args


def intruder_finder(array):
    length = len(array)
    doublon = False

    for i in range(0, length):
        doublon = False
        for j in range(i + 1, length):
            # print("array[i] = " + array[i] + " array[j] = " + array[j])
            if array[i] == array[j]:
                # print("doublon")
                doublon = True
                break
        if not doublon:
            return array[i]


def main():
    args = arg_tester()
    intruder = intruder_finder(args)
    print(intruder)


main()