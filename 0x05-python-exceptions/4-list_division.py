#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = 0;
    l = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            l.append(res)
        except ZeroDivisionError:
            print("division by 0")
            l.append(0)
        except TypeError:
            print("wrong type")
            l.append(0)
        except IndexError:
            print("out of range")
            l.append(0)
            break
        finally:
            continue
    return l
