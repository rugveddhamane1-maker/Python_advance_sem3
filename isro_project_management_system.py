class Project:
    def __init__(self, project_id, name, target_orbit, budget_in_crores):
        self.project_id = project_id
        self.name = name
        self.target_orbit = target_orbit  # e.g., LEO, GEO, Lunar, Martian
        self.budget_in_crores = budget_in_crores
        self.status = "In Development"  # Default status
        self.launch_date = "TBD"

    def update_status(self, new_status):
        self.status = new_status

    def schedule_launch(self, launch_date):
        self.launch_date = launch_date

    def display_project(self):
        print(f"Project ID    : {self.project_id}")
        print(f"Mission Name  : {self.name}")
        print(f"Target Orbit  : {self.target_orbit}")
        print(f"Budget (₹)    : {self.budget_in_crores} Crores")
        print(f"Status        : {self.status}")
        print(f"Launch Date   : {self.launch_date}")
        print("-" * 35)


class ISROControlCenter:
    def __init__(self):
        self.projects = []

    # Register a new project
    def add_project(self, project):
        self.projects.append(project)
        print("Project registered successfully!")

    # Display all registered projects
    def display_all_projects(self):
        if not self.projects:
            print("No active projects found in the system.")
        else:
            print("\n------ Active ISRO Projects ------")
            for project in self.projects:
                project.display_project()

    # Search project by ID
    def search_project(self, project_id):
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None

    # Update project status
    def update_project_status(self, project_id, status):
        project = self.search_project(project_id)
        if project:
            project.update_status(status)
            print("Project status updated successfully.")
        else:
            print("Project ID not found.")

    # Schedule or update launch date
    def schedule_project_launch(self, project_id, launch_date):
        project = self.search_project(project_id)
        if project:
            project.schedule_launch(launch_date)
            print("Launch date scheduled successfully.")
        else:
            print("Project ID not found.")


# ---------------- Main Program ---------------- #

isro = ISROControlCenter()

while True:
    print("\n====== ISRO Project Management System ======")
    print("1. Register New Project")
    print("2. Display All Projects")
    print("3. Search Project")
    print("4. Update Project Status")
    print("5. Schedule Launch Date")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        project_id = int(input("Enter Project ID: "))
        name = input("Enter Mission Name (e.g., Gaganyaan, Chandrayaan-4): ")
        target_orbit = input("Enter Target Orbit/Destination: ")
        budget = float(input("Enter Budget (in Crores INR): "))

        project = Project(project_id, name, target_orbit, budget)
        isro.add_project(project)

    elif choice == "2":
        isro.display_all_projects()

    elif choice == "3":
        project_id = int(input("Enter Project ID to search: "))
        project = isro.search_project(project_id)

        if project:
            print("\n--- Project Found ---")
            project.display_project()
        else:
            print("Project not found.")

    elif choice == "4":
        project_id = int(input("Enter Project ID: "))
        print("\nSelect New Status:")
        print("1. In Development")
        print("2. Integration & Testing")
        print("3. Ready for Launch")
        print("4. Mission Successful")
        print("5. Mission Failed")
        status_choice = input("Choice: ")

        status_map = {
            "1": "In Development",
            "2": "Integration & Testing",
            "3": "Ready for Launch",
            "4": "Mission Successful",
            "5": "Mission Failed"
        }

        new_status = status_map.get(status_choice, "In Development")
        isro.update_project_status(project_id, new_status)

    elif choice == "5":
        project_id = int(input("Enter Project ID: "))
        launch_date = input("Enter Launch Date (e.g., DD-MM-YYYY): ")
        isro.schedule_project_launch(project_id, launch_date)

    elif choice == "6":
        print("Exiting ISRO Management System. Jai Hind!")
        break

    else:
        print("Invalid choice! Please try again.")