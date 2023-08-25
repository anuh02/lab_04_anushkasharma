class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id}\t{self.name}\t{self.start_time}\t{self.priority}"

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {"High": 3, "MID": 2, "Low": 1}
        self.processes.sort(key=lambda x: priority_order[x.priority], reverse=True)

    def print_table(self):
        print("P_ID\tProcess\tStart Time\tPriority")
        print("="*40)
        for process in self.processes:
            print(process)

if __name__ == "__main__":
    flight_table = FlightTable()

    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))

    sorting_choice = int(input("Choose sorting parameter:\n1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n"))

    if sorting_choice == 1:
        flight_table.sort_by_p_id()
    elif sorting_choice == 2:
        flight_table.sort_by_start_time()
    elif sorting_choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice!")

    flight_table.print_table()
