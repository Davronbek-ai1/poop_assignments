class SchoolLocker:
    school_name = "Al-Khwarizmi Academy"
    total_lockers = 0

    def __init__(self, student_name, locker_id, items=None):
        self.student_name = student_name
        self.locker_id = locker_id
        if items is None:
            self.items = []
        else:
            self.items = items
        SchoolLocker.total_lockers += 1

    def store_item(self, item_name):
        if item_name == "":
            print("Invalid item name")
            return
        self.items.append(item_name)
        print(f"Stored: {item_name}")
        return
        
    def retrieve_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"Retrieved: {item_name}")
        else:
            print("Item not found")

    def display_locker(self):
        print(f"Locker {self.locker_id} assigned to {self.student_name} at {SchoolLocker.school_name}")

gulnora = SchoolLocker("Gulnora", "A-12")
ravshan = SchoolLocker("Ravshan", "A-15")
gulnora.display_locker()
gulnora.store_item("Calculator")
gulnora.store_item("Notebook")
gulnora.retrieve_item("Calculator")
ravshan.display_locker()
ravshan.retrieve_item("Backpack")
print(f"Total lockers: {SchoolLocker.total_lockers}")