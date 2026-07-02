"""
test_battery.py

Simple test for the battery service.
"""

from services.system_service import get_battery_status


def main():
    battery = get_battery_status()

    if battery is None:
        print("No battery detected.")
        return

    print("Battery Status")
    print("-" * 20)
    print(f"Percentage : {battery['percent']}%")
    print(
        f"Charging   : {'Yes' if battery['charging'] else 'No'}"
    )


if __name__ == "__main__":
    main()