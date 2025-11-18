class EmergencyWorkflow:

    def __init__(self):
        pass

    def run_workflow(self, risk, location, emergency_level, user_message, user_id):
        print("------ WORKFLOW STARTED ------")
        print(f"Risk Score: {risk}")
        print(f"Location: {location}")
        print(f"Emergency Level: {emergency_level}")
        print(f"User Message: {user_message}")
        print(f"User ID: {user_id}")

        response = {
            "risk": risk,
            "location": location,
            "emergency_level": emergency_level,
            "message": user_message,
            "user_id": user_id,
            "status": "Workflow Completed Successfully"
        }
        return response
