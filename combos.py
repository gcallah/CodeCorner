import random

choices = [1, 2, 3]
num_choices = len(choices)

def gen_combo():
    # Let's fill our 4 slots:
    # Place all 3 choices:
    result = [0]*(num_choices+1)
    taken = [False]*(num_choices+1)

    for i in range(num_choices):
       slot = random.randint(0, num_choices)
       while taken[slot]:
           slot = random.randint(0, num_choices)
       taken[slot] = True
       result[slot] = choices[i]
    not_taken = result.index(False)
    result[not_taken] = random.choice(choices)
    # result[rand
    print(result)


def main():
    for i in range(1000):
        gen_combo()


if __name__ == "__main__":
    main()
