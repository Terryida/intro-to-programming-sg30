from selekta.student_pick import choose



def clear_screen():
    print("\033[2J\033[H", end="")


if __name__ == "__main__":
    students = []
    lower = int(input("Enter a students lower number: ").strip())
    clear_screen()
    upper = int(input("Enter a students upper number: ").strip())
    clear_screen()
    while True:
        user_input = input("\nEnter (Q/q) to quit: ").strip()
        if user_input.lower() == "q":
            clear_screen()
            print("\nThanks for your collaboration!")
            break
        if not students:
            students = choose(lower, upper+1)
        clear_screen()
        print(f"\nStudent: {students.pop()} it's your turn")
