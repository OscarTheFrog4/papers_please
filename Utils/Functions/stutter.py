import random

from wait import wait

def stutter():
    if random.randint(1, 10) == 1:
        wait(1.5, 2)
        print("<< 'Oops, hold on I've got one more.'")
        wait(2, 2)
    elif random.randint(1, 9) == 1:
        wait(1.5, 2)
        print("<< 'Hang on.'")
        wait(2, 2)
    elif random.randint(1, 8) == 1:
        wait(1.5, 2)
        print("<< 'One second please.'")
        wait(2, 2)
    elif random.randint(1, 7) == 1:
        wait(1.5, 2)
        print("<< 'Lemme just find it here...'")
        wait(2, 2)
    else:
        wait(1, 4)