import argparse
import os
from data.database_tables import create_database
from handlers.contact_handler import contact_functions
from handlers.website_handler import website_functions, view_down_history
from website_monitor import run_monitor
from handlers.integration_handler import setup_integrations

def main():
    parser = argparse.ArgumentParser(description="Website Monitor")
    parser.add_argument('--run-background', action='store_true', help='Run the monitor in the background')
    args = parser.parse_args()

    create_database()

    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW('Website Monitor')

    if args.run_background:
        run_monitor()
        return

    while True:
        print("\n1: Run Monitor")
        print("2: Setup and Integrations")
        print("3: Website Functions")
        print("4: Contact Functions")
        print("5: View website down history")
        print("0: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            run_monitor()
        elif choice == '2':
            setup_integrations()
        elif choice == '3':
            website_functions()
        elif choice == '4':
            contact_functions()
        elif choice == '5':
            view_down_history()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
