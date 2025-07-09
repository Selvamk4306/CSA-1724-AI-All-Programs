def vacuum_cleaner(agent_location, room_status):
    steps = []
    print(f"Initial Location: {agent_location}")
    print(f"Initial Room Status: {room_status}")

    while room_status["A"] == "dirty" or room_status["B"] == "dirty":
        if agent_location == "A":
            if room_status["A"] == "dirty":
                print("Room A is dirty. Sucking...")
                room_status["A"] = "clean"
                steps.append("Suck in A")
            if room_status["B"] == "dirty":
                print("Moving to Room B")
                agent_location = "B"
                steps.append("Move Right")
        elif agent_location == "B":
            if room_status["B"] == "dirty":
                print("Room B is dirty. Sucking...")
                room_status["B"] = "clean"
                steps.append("Suck in B")
            if room_status["A"] == "dirty":
                print("Moving to Room A")
                agent_location = "A"
                steps.append("Move Left")

    print("\nAll rooms are clean now!")
    print("Actions taken:")
    for action in steps:
        print(f" - {action}")

# Example usage:
room_status = {
    "A": "clean",
    "B": "dirty"
}
vacuum_cleaner("A", room_status)