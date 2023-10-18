from sys import argv, exit


def arg_tester():
    args = argv[1:]
    
    if len(args) != 1:
        print("erreur d'argument")
        exit()
        
    return "".join(args)


def split(array):
    separator = [chr(32), chr(10), chr(9)]
    words = []
    first_caracter_index = 0
    end = len(array)
    
    for i in range(end):
        # print(f"array[{i}] = {array[i]}")
        if array[i] in separator:
            words.append(array[first_caracter_index:i])
            first_caracter_index = i + 1
            
    words.append(array[first_caracter_index:end])
    # print(f"words: {words}")
    
    return words


def main():
    argument = arg_tester()
    # print(argument)
    array = split(argument)
    
    for word in array:
        print(word)


main()