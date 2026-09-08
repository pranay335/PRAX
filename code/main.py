from agent import PraxAgent


def main():

    prax = PraxAgent()

    print("=" * 40)
    print("          PRAX AI AGENT")
    print("=" * 40)
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("PRAX: Goodbye!")
            break

        try:
            response = prax.chat(user_input)
            print(f"\nPRAX: {response}\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()