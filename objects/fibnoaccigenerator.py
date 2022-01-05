def generate_fibonacci_sequence():
    num_1 = 0
    num_2 = 1

    while True:
        # temporary return value every time the function gets called unlike for return that terminates the function
        yield num_1

        num_1 = num_2
        num_2 = num_1 + num_2


if __name__ == "__main__":
    seq = generate_fibonacci_sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))

