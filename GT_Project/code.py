import datetime

# Define some events with start and end times
events = [
    {"start_time": datetime.datetime(2024, 3, 15, 10, 0), "end_time": datetime.datetime(2024, 3, 15, 11, 0), "description": "Meeting with client"},
    {"start_time": datetime.datetime(2024, 3, 20, 14, 30), "end_time": datetime.datetime(2024, 3, 20, 16, 0), "description": "Project deadline"},
    {"start_time": datetime.datetime(2024, 3, 25, 12, 0), "end_time": datetime.datetime(2024, 3, 25, 14, 0), "description": "Team outing"}
]

# Function to filter events within the time range
def filter_events(start_time, end_time):
    filtered_events = [event for event in events
                       if event["start_time"] <= end_time and event["end_time"] >= start_time]
    return filtered_events

# Input time range
start_input = input("Enter start time (YYYY-MM-DD HH:MM): ")
end_input = input("Enter end time (YYYY-MM-DD HH:MM): ")

# Convert input strings to datetime objects
start_time = datetime.datetime.strptime(start_input, "%Y-%m-%d %H:%M")
end_time = datetime.datetime.strptime(end_input, "%Y-%m-%d %H:%M")

# Filter events within the specified time range
filtered_events = filter_events(start_time, end_time)

# Print the filtered events
if filtered_events:
    print("Events within the specified time range:")
    for event in filtered_events:
        print(f"Description: {event['description']}, Start Time: {event['start_time']}, End Time: {event['end_time']}")
else:
    print("No events scheduled within the specified time range.")
