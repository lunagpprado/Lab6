def decode(password):
    list = []
    for i in range(0, len(password)):
        list.append(password[i])
    for i in range(0, len(list)):
        list[i] = str(int(list[i]) - 3)
    return "".join(list)
