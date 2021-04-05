import evolution.run_evolution as evolution


def start_up():
    print("What would you like to run?")
    print("1: Evolution")
    sim = input()
    if sim == "1":
        evolution.run()


if __name__ == "__main__":
    start_up()
