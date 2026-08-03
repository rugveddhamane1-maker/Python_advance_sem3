import datetime
import tkinter as tk
from tkinter import messagebox, ttk


# ------------------ Core Data Models ------------------ #

class FlowerSale:
    def __init__(self, sale_id, date_str, quantity_kg, price):
        self.sale_id = sale_id
        self.date_str = date_str
        # Parse datetime object for grouping logic
        self.date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        self.quantity_kg = quantity_kg
        self.price = price


class FlowerSalesTracker:
    def __init__(self):
        self.sales = {}
        self._next_id = 1

    def add_sale(self, date_str, quantity_kg, price):
        sale = FlowerSale(self._next_id, date_str, quantity_kg, price)
        self.sales[self._next_id] = sale
        self._next_id += 1
        return True, "Sale record added successfully!"

    def delete_sale(self, sale_id):
        if sale_id in self.sales:
            del self.sales[sale_id]
            return True, "Record deleted successfully!"
        return False, "Record ID not found."

    def get_all_sales(self):
        return sorted(self.sales.values(), key=lambda x: x.date_obj, reverse=True)

    def get_weekly_totals(self):
        weekly_data = {}
        for sale in self.sales.values():
            year, week, _ = sale.date_obj.isocalendar()
            week_key = f"{year}-W{week:02d}"
            if week_key not in weekly_data:
                weekly_data[week_key] = {"kg": 0.0, "price": 0.0}
            weekly_data[week_key]["kg"] += sale.quantity_kg
            weekly_data[week_key]["price"] += sale.price
        return weekly_data

    def get_monthly_totals(self):
        monthly_data = {}
        for sale in self.sales.values():
            month_key = sale.date_obj.strftime("%Y-%m")
            if month_key not in monthly_data:
                monthly_data[month_key] = {"kg": 0.0, "price": 0.0}
            monthly_data[month_key]["kg"] += sale.quantity_kg
            monthly_data[month_key]["price"] += sale.price
        return monthly_data


# ------------------ GUI Application ------------------ #

class FlowerSalesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flower Sales Tracker & Management")
        self.geometry("950x650")
        self.minsize(850, 550)

        # Initialize Backend Engine
        self.tracker = FlowerSalesTracker()

        # Seed initial sample data
        self._seed_sample_data()

        # Style configuration
        self._setup_styles()

        # Layout Setup
        self._build_header()
        self._build_main_layout()

        # Refresh UI
        self.refresh_all_views()

    def _seed_sample_data(self):
        sample_entries = [
            ("2026-07-20", 12.5, 2500.0),
            ("2026-07-21", 18.0, 3600.0),
            ("2026-07-22", 15.2, 3040.0),
            ("2026-06-15", 25.0, 5000.0),
            ("2026-06-18", 10.0, 2000.0)
        ]
        for date_str, kg, price in sample_entries:
            self.tracker.add_sale(date_str, kg, price)

    def _setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Define color scheme
        self.style.configure("TFrame", background="#F7F9FC")
        self.style.configure("Header.TFrame", background="#2E7D32") # Floral Green
        self.style.configure("Header.TLabel", background="#2E7D32", foreground="white", font=("Helvetica", 18, "bold"))

        self.style.configure("TLabel", background="#F7F9FC", font=("Helvetica", 10))
        self.style.configure("TLabelframe", background="#F7F9FC", font=("Helvetica", 10, "bold"))
        self.style.configure("TLabelframe.Label", background="#F7F9FC", foreground="#2E7D32")

        self.style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
        self.style.configure("Delete.TButton", font=("Helvetica", 10, "bold"), background="#D32F2F", foreground="white")
        self.style.map("Delete.TButton", background=[("active", "#B71C1C")])

        self.style.configure("Treeview", font=("Helvetica", 9), rowheight=25)
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#E8F5E9")

    def _build_header(self):
        header_frame = ttk.Frame(self, style="Header.TFrame", padding=15)
        header_frame.pack(fill=tk.X)
        header_label = ttk.Label(header_frame, text="🌸 Daily Flower Sales Tracker", style="Header.TLabel")
        header_label.pack()

    def _build_main_layout(self):
        main_container = ttk.Frame(self, padding=10)
        main_container.pack(fill=tk.BOTH, expand=True)

        # Left Panel (Input Form & Delete Actions)
        left_panel = ttk.Frame(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self._build_add_sale_form(left_panel)
        self._build_summary_panel(left_panel)

        # Right Panel (Notebook with Tabs: Daily, Weekly, Monthly)
        right_panel = ttk.Frame(main_container)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self._build_daily_tab()
        self._build_weekly_tab()
        self._build_monthly_tab()

    def _build_add_sale_form(self, parent):
        frame = ttk.LabelFrame(parent, text=" Add New Sale Record ", padding=10)
        frame.pack(fill=tk.X, pady=(0, 10))

        # Date Field
        ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.entry_date = ttk.Entry(frame)
        self.entry_date.grid(row=0, column=1, pady=3)
        self.entry_date.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

        # Quantity Field
        ttk.Label(frame, text="Quantity (kg):").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.entry_kg = ttk.Entry(frame)
        self.entry_kg.grid(row=1, column=1, pady=3)

        # Price Field
        ttk.Label(frame, text="Final Price (₹):").grid(row=2, column=0, sticky=tk.W, pady=3)
        self.entry_price = ttk.Entry(frame)
        self.entry_price.grid(row=2, column=1, pady=3)

        # Buttons
        btn_add = ttk.Button(frame, text="Add Sale Entry", command=self.add_sale_action)
        btn_add.grid(row=3, column=0, columnspan=2, pady=(10, 5), sticky=tk.EW)

        btn_delete = ttk.Button(frame, text="Delete Selected Record", style="Delete.TButton", command=self.delete_sale_action)
        btn_delete.grid(row=4, column=0, columnspan=2, pady=(0, 0), sticky=tk.EW)

    def _build_summary_panel(self, parent):
        frame = ttk.LabelFrame(parent, text=" Overall Summary ", padding=10)
        frame.pack(fill=tk.X)

        ttk.Label(frame, text="Total Flowers Sold:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.lbl_total_kg = ttk.Label(frame, text="0.00 kg", font=("Helvetica", 10, "bold"))
        self.lbl_total_kg.grid(row=0, column=1, sticky=tk.E, pady=2)

        ttk.Label(frame, text="Total Revenue:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.lbl_total_price = ttk.Label(frame, text="₹ 0.00", font=("Helvetica", 10, "bold"), foreground="#2E7D32")
        self.lbl_total_price.grid(row=1, column=1, sticky=tk.E, pady=2)

    def _build_daily_tab(self):
        tab = ttk.Frame(self.notebook, padding=5)
        self.notebook.add(tab, text=" All Entries (Daily) ")

        columns = ("id", "date", "kg", "price")
        self.daily_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")

        self.daily_tree.heading("id", text="ID")
        self.daily_tree.heading("date", text="Date")
        self.daily_tree.heading("kg", text="Quantity (kg)")
        self.daily_tree.heading("price", text="Total Price (₹)")

        self.daily_tree.column("id", width=40, anchor=tk.CENTER)
        self.daily_tree.column("date", width=120, anchor=tk.CENTER)
        self.daily_tree.column("kg", width=120, anchor=tk.E)
        self.daily_tree.column("price", width=120, anchor=tk.E)

        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.daily_tree.yview)
        self.daily_tree.configure(yscroll=scrollbar.set)

        self.daily_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _build_weekly_tab(self):
        tab = ttk.Frame(self.notebook, padding=5)
        self.notebook.add(tab, text=" Weekly Totals ")

        columns = ("week", "kg", "price")
        self.weekly_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")

        self.weekly_tree.heading("week", text="Week (Year-W##)")
        self.weekly_tree.heading("kg", text="Total Sold (kg)")
        self.weekly_tree.heading("price", text="Total Revenue (₹)")

        self.weekly_tree.column("week", width=150, anchor=tk.CENTER)
        self.weekly_tree.column("kg", width=150, anchor=tk.E)
        self.weekly_tree.column("price", width=150, anchor=tk.E)

        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.weekly_tree.yview)
        self.weekly_tree.configure(yscroll=scrollbar.set)

        self.weekly_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _build_monthly_tab(self):
        tab = ttk.Frame(self.notebook, padding=5)
        self.notebook.add(tab, text=" Monthly Totals ")

        columns = ("month", "kg", "price")
        self.monthly_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")

        self.monthly_tree.heading("month", text="Month (YYYY-MM)")
        self.monthly_tree.heading("kg", text="Total Sold (kg)")
        self.monthly_tree.heading("price", text="Total Revenue (₹)")

        self.monthly_tree.column("month", width=150, anchor=tk.CENTER)
        self.monthly_tree.column("kg", width=150, anchor=tk.E)
        self.monthly_tree.column("price", width=150, anchor=tk.E)

        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.monthly_tree.yview)
        self.monthly_tree.configure(yscroll=scrollbar.set)

        self.monthly_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ------------------ Action & Update Handlers ------------------ #

    def refresh_all_views(self):
        self._refresh_daily_table()
        self._refresh_weekly_table()
        self._refresh_monthly_table()
        self._refresh_summary_block()

    def _refresh_daily_table(self):
        for row in self.daily_tree.get_children():
            self.daily_tree.delete(row)
        for sale in self.tracker.get_all_sales():
            self.daily_tree.insert("", tk.END, values=(
                sale.sale_id, sale.date_str, f"{sale.quantity_kg:.2f} kg", f"₹ {sale.price:.2f}"
            ))

    def _refresh_weekly_table(self):
        for row in self.weekly_tree.get_children():
            self.weekly_tree.delete(row)
        weekly_data = self.tracker.get_weekly_totals()
        for week, data in sorted(weekly_data.items(), reverse=True):
            self.weekly_tree.insert("", tk.END, values=(
                week, f"{data['kg']:.2f} kg", f"₹ {data['price']:.2f}"
            ))

    def _refresh_monthly_table(self):
        for row in self.monthly_tree.get_children():
            self.monthly_tree.delete(row)
        monthly_data = self.tracker.get_monthly_totals()
        for month, data in sorted(monthly_data.items(), reverse=True):
            self.monthly_tree.insert("", tk.END, values=(
                month, f"{data['kg']:.2f} kg", f"₹ {data['price']:.2f}"
            ))

    def _refresh_summary_block(self):
        total_kg = sum(s.quantity_kg for s in self.tracker.sales.values())
        total_price = sum(s.price for s in self.tracker.sales.values())
        self.lbl_total_kg.config(text=f"{total_kg:.2f} kg")
        self.lbl_total_price.config(text=f"₹ {total_price:.2f}")

    def add_sale_action(self):
        date_str = self.entry_date.get().strip()
        kg_str = self.entry_kg.get().strip()
        price_str = self.entry_price.get().strip()

        try:
            # Validate Date Format
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            kg = float(kg_str)
            price = float(price_str)

            if kg <= 0 or price < 0:
                messagebox.showwarning("Input Error", "Quantity and price must be positive numbers.")
                return

            self.tracker.add_sale(date_str, kg, price)
            self.refresh_all_views()
            self._clear_form()
            messagebox.showinfo("Success", "Flower sale entry added successfully!")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please provide a valid date format (YYYY-MM-DD) and numeric values for Quantity/Price.")

    def delete_sale_action(self):
        selected_item = self.daily_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select an entry from the 'All Entries (Daily)' table to delete.")
            return

        item_values = self.daily_tree.item(selected_item, "values")
        sale_id = int(item_values[0])

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete entry ID {sale_id}?"):
            self.tracker.delete_sale(sale_id)
            self.refresh_all_views()

    def _clear_form(self):
        self.entry_kg.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)


# ------------------ App Entry Point ------------------ #

if __name__ == "__main__":
    app = FlowerSalesApp()
    app.mainloop()