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
        print("""STRING ENCODER/DECODER
1. ENCODER
2. DECODER
3. EXIT""")
        print()
        input_var = int(input("INPUT MENU OPTION: "))
        print()
        if input_var == 1:
            str_user = input("ENTER STRING TO BE ENCODED: ")
            encoded_var = encoder(str_user)
            print(f"ENCODED STRING: {encoded_var}")
        if input_var == 2:
            print("None")
        if input_var == 3:
            print("GOODBYE!")
            loop_var = False
            break


if __name__ == '__main__':
    main()
