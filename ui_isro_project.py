import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Core Data Models ------------------ #

class Project:
    def __init__(self, project_id, name, target_orbit, budget_in_crores):
        self.project_id = project_id
        self.name = name
        self.target_orbit = target_orbit
        self.budget_in_crores = budget_in_crores
        self.status = "In Development"
        self.launch_date = "TBD"


class ISROControlCenter:
    def __init__(self):
        self.projects = {}

    def add_project(self, project):
        if project.project_id in self.projects:
            return False, "Project ID already exists!"
        self.projects[project.project_id] = project
        return True, "Project registered successfully!"

    def get_all_projects(self):
        return list(self.projects.values())

    def search_project(self, project_id):
        return self.projects.get(project_id, None)


# ------------------ GUI Application ------------------ #

class ISROApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ISRO Mission Control System")
        self.geometry("950x600")
        self.minsize(850, 500)

        # Initialize Backend Engine
        self.system = ISROControlCenter()

        # Seed initial sample data
        self._seed_sample_data()

        # Style configuration
        self._setup_styles()

        # Layout Setup
        self._build_header()
        self._build_main_layout()
        
        # Populate Treeview
        self.refresh_project_list()

    def _seed_sample_data(self):
        sample_projects = [
            Project(101, "Chandrayaan-4", "Lunar Surface", 1200.0),
            Project(102, "Gaganyaan-1", "Low Earth Orbit", 9000.0),
            Project(103, "Aditya-L2", "Sun-Earth L2 Point", 400.0)
        ]
        sample_projects[1].status = "Ready for Launch"
        sample_projects[1].launch_date = "15-08-2026"
        for p in sample_projects:
            self.system.add_project(p)

    def _setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Define color scheme
        self.style.configure("TFrame", background="#F4F6F9")
        self.style.configure("Header.TFrame", background="#0B3D91") # ISRO Blue
        self.style.configure("Header.TLabel", background="#0B3D91", foreground="white", font=("Helvetica", 18, "bold"))
        
        self.style.configure("TLabel", background="#F4F6F9", font=("Helvetica", 10))
        self.style.configure("TLabelframe", background="#F4F6F9", font=("Helvetica", 10, "bold"))
        self.style.configure("TLabelframe.Label", background="#F4F6F9", foreground="#0B3D91")

        self.style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
        self.style.configure("Treeview", font=("Helvetica", 9), rowheight=25)
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#E1E6ED")

    def _build_header(self):
        header_frame = ttk.Frame(self, style="Header.TFrame", padding=15)
        header_frame.pack(fill=tk.X)
        header_label = ttk.Label(header_frame, text="🚀 ISRO Project Management Dashboard", style="Header.TLabel")
        header_label.pack()

    def _build_main_layout(self):
        # Main split container
        main_container = ttk.Frame(self, padding=10)
        main_container.pack(fill=tk.BOTH, expand=True)

        # Left Panel (Forms for Input & Update)
        left_panel = ttk.Frame(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self._build_add_project_form(left_panel)
        self._build_update_project_form(left_panel)

        # Right Panel (Data Grid Table)
        right_panel = ttk.Frame(main_container)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self._build_table(right_panel)

    def _build_add_project_form(self, parent):
        frame = ttk.LabelFrame(parent, text=" Register New Mission ", padding=10)
        frame.pack(fill=tk.X, pady=(0, 10))

        # Fields
        ttk.Label(frame, text="Project ID:").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.entry_id = ttk.Entry(frame)
        self.entry_id.grid(row=0, column=1, pady=3)

        ttk.Label(frame, text="Mission Name:").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.entry_name = ttk.Entry(frame)
        self.entry_name.grid(row=1, column=1, pady=3)

        ttk.Label(frame, text="Target Orbit:").grid(row=2, column=0, sticky=tk.W, pady=3)
        self.entry_orbit = ttk.Entry(frame)
        self.entry_orbit.grid(row=2, column=1, pady=3)

        ttk.Label(frame, text="Budget (₹ Cr):").grid(row=3, column=0, sticky=tk.W, pady=3)
        self.entry_budget = ttk.Entry(frame)
        self.entry_budget.grid(row=3, column=1, pady=3)

        # Add Button
        btn_add = ttk.Button(frame, text="Add Project", command=self.add_project_action)
        btn_add.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky=tk.EW)

    def _build_update_project_form(self, parent):
        frame = ttk.LabelFrame(parent, text=" Update Mission Details ", padding=10)
        frame.pack(fill=tk.X)

        ttk.Label(frame, text="Status:").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.combo_status = ttk.Combobox(frame, values=[
            "In Development",
            "Integration & Testing",
            "Ready for Launch",
            "Mission Successful",
            "Mission Failed"
        ], state="readonly")
        self.combo_status.grid(row=0, column=1, pady=3)
        self.combo_status.current(0)

        ttk.Label(frame, text="Launch Date:").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.entry_launch_date = ttk.Entry(frame)
        self.entry_launch_date.grid(row=1, column=1, pady=3)

        # Update Button
        btn_update = ttk.Button(frame, text="Update Selected Project", command=self.update_project_action)
        btn_update.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky=tk.EW)

    def _build_table(self, parent):
        frame = ttk.LabelFrame(parent, text=" Active Projects Directory ", padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        columns = ("id", "name", "orbit", "budget", "status", "launch_date")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", selectmode="browse")

        # Headings
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Mission Name")
        self.tree.heading("orbit", text="Target Orbit")
        self.tree.heading("budget", text="Budget (₹ Cr)")
        self.tree.heading("status", text="Status")
        self.tree.heading("launch_date", text="Launch Date")

        # Column widths
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("name", width=130)
        self.tree.column("orbit", width=120)
        self.tree.column("budget", width=90, anchor=tk.E)
        self.tree.column("status", width=130)
        self.tree.column("launch_date", width=100, anchor=tk.CENTER)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Event binding for row click
        self.tree.bind("<<TreeviewSelect>>", self.on_project_selected)

    # ------------------ Action Handlers ------------------ #

    def refresh_project_list(self):
        # Clear existing items
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Re-populate items
        for p in self.system.get_all_projects():
            self.tree.insert("", tk.END, values=(
                p.project_id, p.name, p.target_orbit, f"{p.budget_in_crores:.2f}", p.status, p.launch_date
            ))

    def add_project_action(self):
        try:
            pid = int(self.entry_id.get().strip())
            name = self.entry_name.get().strip()
            orbit = self.entry_orbit.get().strip()
            budget = float(self.entry_budget.get().strip())

            if not name or not orbit:
                messagebox.showwarning("Input Error", "All fields are required!")
                return

            new_project = Project(pid, name, orbit, budget)
            success, message = self.system.add_project(new_project)

            if success:
                messagebox.showinfo("Success", message)
                self.refresh_project_list()
                self._clear_add_form()
            else:
                messagebox.showerror("Error", message)

        except ValueError:
            messagebox.showerror("Invalid Input", "Project ID and Budget must be numeric values!")

    def update_project_action(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Warning", "Please select a project from the table to update.")
            return

        item_values = self.tree.item(selected_item, "values")
        project_id = int(item_values[0])

        project = self.system.search_project(project_id)
        if project:
            project.status = self.combo_status.get()
            date_input = self.entry_launch_date.get().strip()
            if date_input:
                project.launch_date = date_input

            messagebox.showinfo("Success", "Project updated successfully!")
            self.refresh_project_list()

    def on_project_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            # Prefill update form with current status and launch date
            self.combo_status.set(item_values[4])
            self.entry_launch_date.delete(0, tk.END)
            self.entry_launch_date.insert(0, item_values[5])

    def _clear_add_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_orbit.delete(0, tk.END)
        self.entry_budget.delete(0, tk.END)


# ------------------ App Entry Point ------------------ #

if __name__ == "__main__":
    app = ISROApp()
    app.mainloop()