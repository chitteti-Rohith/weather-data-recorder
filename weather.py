import pandas as pd
from datetime import datetime

# Main storage
weather_data = []
dates_seen = set()

def add_entry(date_str, temperature, condition):
    """Add a new entry after validating date and checking uniqueness."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")  # Validate date
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    if date_str in dates_seen:
        print(f"❌ Entry for date {date_str} already exists.")
        return

    entry = {"date": date_str, "temperature": float(temperature), "condition": condition}
    weather_data.append(entry)
    dates_seen.add(date_str)
    print(f"✅ Entry added for {date_str}")

def view_data():
    """Display all stored entries."""
    if not weather_data:
        print("No data available.")
    else:
        for entry in weather_data:
            print(entry)

def export_data(filename="weather_data.csv"):
    """Export the data to a CSV file using Pandas."""
    if not weather_data:
        print("❌ No data to export.")
        return
    df = pd.DataFrame(weather_data)
    df.to_csv(filename, index=False)
    print(f"✅ Data exported to {filename}")

def calculate_average():
    """Calculate average temperature using Pandas."""
    if not weather_data:
        print("❌ No data available.")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["temperature"].mean()
    print(f"🌡️ Average Temperature: {avg_temp:.2f}")

def main():
    """Main menu for the Weather Data Recorder."""
    while True:
        print("\n🌦️ Weather Data Recorder Menu 🌦️")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Export to .csv")
        print("4. Get Average Temperature")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            temp = input("Enter Temperature: ")
            condition = input("Enter Condition (e.g., Sunny/Rainy): ")
            add_entry(date, temp, condition)

        elif choice == "2":
            view_data()

        elif choice == "3":
            export_data()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            print("👋 Exiting the Weather Recorder. Stay weather-aware!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
