from agents.supervisor import SupervisorAgent

def main():
    supervisor = SupervisorAgent()

    while True:
        user_text = input("\nYou: ")

        if user_text.lower() == "exit":
            print("Exiting SHE-GUARD...")
            break

        response = supervisor.process_input(user_text)
        print("\nSYSTEM OUTPUT:", response)


if __name__ == "__main__":
    main()
