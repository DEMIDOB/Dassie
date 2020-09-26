import random

import knowledge.static as knst

def gen_laugh():
    ret = ""
    len = random.randint(2, 5)
    for i in range(len):
        ret += random.choice(knst.laugh_combinations)

    # print(ret[0])

    braces_num = random.randint(0, 3)
    for i in range(0, braces_num):
        ret += ")"

    ret_main = ""
    i = 0
    for r in ret:
        if i == 0:
            ret_main += r.upper()
        else:
            ret_main += r
        i += 1

    return ret_main


if __name__ == '__main__':
    print(gen_laugh())