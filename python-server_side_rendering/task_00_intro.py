def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input type.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input type.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        current_invitation = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"

            current_invitation = current_invitation.replace(f"{{{placeholder}}}", str(value))
        
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(current_invitation)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
