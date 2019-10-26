def solution(num_as_string):
    number = 5
    num_as_string = list(str(num_as_string))

    if "-" in num_as_string:
        num_as_string.remove('-')
        str_int = int(num_as_string[0])
        if number < str_int:
            num_as_string.insert(0, str(number))
        else:
            leng = len(num_as_string) - 1
            while leng > -1:
                if number < int(num_as_string[leng]):
                    leng = leng - 1
                    continue
                elif number == int(num_as_string[leng]):
                    leng = leng - 1
                    continue
                else:
                    if leng == 0:
                        num_as_string.insert(0, str(number))
                        break
                    else:
                        num_as_string.insert(leng + 1, str(number))
                        break
        num_as_string.insert(0, "-")
        a = ''.join(num_as_string)
        return int(a)
    else:
        str_int = int(num_as_string[0])
        if number > str_int:
            num_as_string.insert(0, str(number))
        else:
            leng = len(num_as_string) - 1
            while leng > -1:
                if number > int(num_as_string[leng]):
                    leng = leng - 1
                    continue
                elif number == int(num_as_string[leng]):
                    leng = leng - 1
                    continue
                else:
                    if leng == 0:
                        num_as_string.insert(0, str(number))
                        break
                    else:
                        num_as_string.insert(leng+1, str(number))
                        break

    a = ''.join(num_as_string)
    return int(a)


if __name__ == "__main__":
    print(solution(9))