'''
Lab 6
Authors: Luna Prado and Laura Garcia
Class: COP3502C
Section: 22282
Description: GitHub Version Control, encoding and decoding program
'''


def encoder(str_input):
    str_list = []
    for i in range(0, len(str_input)):
        str_list.append(str_input[i])
        str_list[i] = str(int(str_list[i]) + 3)
    final_list = "".join(str_list)
    return final_list


def main():
    loop_var = True
    while loop_var:
        print()
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        print()
        input_var = int(input("Please enter an option: "))
        print()
        if input_var == 1:
            str_user = input("Please enter your password to encode: ")
            encoded_var = encoder(str_user)
            print(f"Your password has been encoded and stored!")
        if input_var == 2:
            print(f"The encoded password is {encoded_var}, and the original password is {str_user}.")
        if input_var == 3:
            loop_var = False
            break


if __name__ == '__main__':
    main()
