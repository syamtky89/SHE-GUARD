from agents.supervisor import SupervisorAgent

def main():
    supervisor = SupervisorAgent()

    print("=== WELCOME TO SHE-GUARD ===")
    user_message = input("Enter your message: ")
    user_id = "USER-01"

    result = supervisor.process_input(user_message, user_id)

    print("\n--- FINAL OUTPUT ---")
    print(result)


if __name__ == "__main__":
    main()
