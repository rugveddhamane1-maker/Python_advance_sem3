# Decorator for formatting project details
def project_decorator(function):
    def wrapper(self):
        print("=" * 40)
        function(self)
        print("=" * 40)
    return wrapper


class Project:

    # Class variable
    project_count = 0

    # Constructor
    def __init__(self, project_id, name, target_orbit, budget_in_crores):
        self.project_id = project_id
        self.name = name
        self.target_orbit = target_orbit
        self.budget_in_crores = budget_in_crores
        self.status = "In Development"
        self.launch_date = "TBD"

        Project.project_count += 1

    # Magic Method
    def __str__(self):
        return f"Project ID: {self.project_id} | Mission: {self.name}"

    # Class Method
    @classmethod
    def total_projects(cls):
        print("Total Projects Registered:", cls.project_count)

    # Decorator applied
    @project_decorator
    def display_project(self):
        print("ISRO PROJECT DETAILS")
        print("Project ID   :", self.project_id)
        print("Mission Name :", self.name)
        print("Target Orbit :", self.target_orbit)
        print("Budget       :", self.budget_in_crores, "Crores")
        print("Status       :", self.status)
        print("Launch Date  :", self.launch_date)


# ---------------- Main Program ----------------

# User Input
project_id = int(input("Enter Project ID: "))
name = input("Enter Mission Name: ")
target_orbit = input("Enter Target Orbit: ")
budget = float(input("Enter Budget (in Crores): "))

# Create Object
p1 = Project(project_id, name, target_orbit, budget)

# Display Project Details
p1.display_project()

# Using Magic Method
print(p1)

# Display Total Projects
Project.total_projects()
