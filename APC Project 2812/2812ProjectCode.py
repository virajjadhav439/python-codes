import datetime
import os

# Name of the text file where data will be stored
DATA_FILE = 'gym_members_db.txt'

class GymManagementSystem:
    def __init__(self):
        self.members = {}
        self.load_data()

    def load_data(self):
        """Loads data from the TXT file when the script starts."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as file:
                    for line in file:
                        line = line.strip() # Remove extra spaces/newlines
                        if line: # Skip empty lines
                            # Split the line by the pipe symbol '|'
                            phone, name, join_date, duration, fee_paid = line.split('|')
                            
                            self.members[phone] = {
                                "name": name,
                                "join_date": join_date,
                                "duration_months": int(duration),
                                "fee_paid": fee_paid == 'True' # Convert back to boolean
                            }
                print(f"📂 System Ready: Loaded {len(self.members)} members from text file.")
            except Exception as e:
                print(f"⚠️ Warning: Could not read the file properly. Starting fresh. ({e})")
                self.members = {}
        else:
            print("📂 No existing text database found. A new one will be created.")

    def save_data(self):
        """Saves the current dictionary to the TXT file automatically."""
        with open(DATA_FILE, 'w') as file:
            for phone, info in self.members.items():
                # Create a string separated by '|'
                line = f"{phone}|{info['name']}|{info['join_date']}|{info['duration_months']}|{info['fee_paid']}\n"
                file.write(line)

    def calculate_expiry(self, join_date_str, duration_months):
        """Accurately calculates the expiry date based on months."""
        join_date = datetime.date.fromisoformat(join_date_str)
        month = join_date.month - 1 + duration_months
        year = join_date.year + month // 12
        month = month % 12 + 1
        day = min(join_date.day, [31,
            29 if year % 4 == 0 and not year % 400 == 0 else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime.date(year, month, day)

    def add_member(self):
        print("\n--- 🏋️‍♂️ Add New Gym Member ---")
        phone = input("Enter Phone Number (Unique ID): ")
        if phone in self.members:
            print(f"❌ A member with phone {phone} already exists!")
            return

        name = input("Enter Member Name: ")
        
        try:
            duration = int(input("Enter Membership Duration (in months): "))
        except ValueError:
            print("❌ Invalid input! Duration must be a number.")
            return

        fee_input = input("Has the fee been paid? (yes/no): ").strip().lower()
        fee_paid = True if fee_input == 'yes' else False

        self.members[phone] = {
            "name": name,
            "join_date": str(datetime.date.today()),
            "duration_months": duration,
            "fee_paid": fee_paid
        }
        
        self.save_data()  # 💾 SAVE TO TXT FILE
        print(f"✅ Gym Bro '{name}' added successfully! Saved to text file.")

    def check_fee_status(self):
        print("\n--- 💰 Monthly Fee Status ---")
        if not self.members:
            print("No members in the system yet.")
            return

        for phone, info in self.members.items():
            status = "✅ Paid" if info['fee_paid'] else "❌ Pending"
            print(f"👤 {info['name']} | 📞 {phone} | Status: {status}")

    def update_fee_status(self):
        print("\n--- 💳 Update Fee Status ---")
        phone = input("Enter Phone Number to update fee status: ")
        if phone in self.members:
            self.members[phone]['fee_paid'] = True
            self.save_data()  # 💾 SAVE TO TXT FILE
            print(f"✅ Fee marked as PAID for {self.members[phone]['name']}. Text file updated.")
        else:
            print("❌ Member not found!")

    def expired_alert(self):
        print("\n--- 🚨 Expired Memberships Alert ---")
        if not self.members:
            print("No members to check.")
            return

        today = datetime.date.today()
        found_expired = False
        
        for phone, info in self.members.items():
            expiry_date = self.calculate_expiry(info['join_date'], info['duration_months'])
            
            if today > expiry_date:
                days_overdue = (today - expiry_date).days
                print(f"⚠️ {info['name']} (📞 {phone})")
                print(f"   Expired On: {expiry_date} ({days_overdue} days overdue!)")
                found_expired = True
        
        if not found_expired:
            print("All good! No expired memberships right now. Everyone is active! 💪")

def main():
    gym = GymManagementSystem()
    
    while True:
        print("\n" + "="*35)
        print("   IRON FORGE GYM MANAGER")
        print("="*35)
        print("1. Add New Member")
        print("2. View Fee Status")
        print("3. Update Fee to Paid")
        print("4. Check Expired Memberships (Alert)")
        print("5. Exit")
        print("="*35)
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            gym.add_member()
        elif choice == '2':
            gym.check_fee_status()
        elif choice == '3':
            gym.update_fee_status()
        elif choice == '4':
            gym.expired_alert()
        elif choice == '5':
            print("Exiting system. Have a great workout! 🏋️‍♂️👋")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()