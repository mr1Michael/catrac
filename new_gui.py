import csv

import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox


class App:
    def __init__(self):
        self.main_window = ctk.CTk()
        self.main_window.geometry("1000x600")

        self.tabs = ctk.CTkTabview(self.main_window)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabs.add("information")
        self.tabs.add("inputs")

        # Build tabs
        self._build_information_tab()
        self._build_inputs_tab()

        self.main_window.mainloop()

    def _build_information_tab(self):
        tab = self.tabs.tab("information")
        # Title
        self.label = ctk.CTkLabel(
            tab,
            text="Apex Code Categorisation System",
            font=("Arial", 20)
        )
        self.label.pack(pady=20)

        # Table frame
        self.table_frame = ctk.CTkFrame(tab)
        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Table (ttk.Treeview)
        columns = (
            "StockCode",
            "Description",
            "Brand",
            "Category",
            "Department",
            "Group"
        )

        self.table = ttk.Treeview(
            self.table_frame,
            columns=columns,
            show="headings"
        )

        self.table.tag_configure(
            "unknown",
            background="orange"
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=150)

        self.table.pack(
            fill="both",
            expand=True
        )

        self.export_button = ctk.CTkButton(
            tab,
            text="Export CSV",
            command=self.export_csv
        )
        self.export_button.pack(pady=10)

        self.refresh_button = ctk.CTkButton(
            tab,
            text="Refresh",
            command=self.refresh_table
        )
        self.refresh_button.pack(pady=10)

        # Test data
        self.load_data()

    def _build_inputs_tab(self):
        tab = self.tabs.tab("inputs")

        ctk.CTkLabel(tab, text="Add entry").pack(pady=(10, 5))

        form = ctk.CTkFrame(tab)
        form.pack(pady=10, padx=20, fill="x")

        entry_vars = {
            "StockCode": ctk.StringVar(),
            "Description": ctk.StringVar(),
            "Brand": ctk.StringVar(),
            "Category": ctk.StringVar(),
            "Department": ctk.StringVar(),
            "Group": ctk.StringVar(),
        }

        fields = ["StockCode", "Description", "Brand", "Category", "Department", "Group"]

        for i, field in enumerate(fields):
            ctk.CTkLabel(form, text=field).grid(row=i, column=0, sticky="w", padx=10, pady=6)
            ctk.CTkEntry(form, textvariable=entry_vars[field], width=260).grid(
                row=i, column=1, sticky="ew", padx=10, pady=6
            )

        form.grid_columnconfigure(1, weight=1)

        # ctk.CTkButton(tab, text="Add Entry", command=self.add_entry, width=200).pack(pady=10)
        ctk.CTkButton(tab, text="Add Entry",
            command=lambda: self.load_data(data=
                [(entry_vars["StockCode"].get(),
                entry_vars["Description"].get(),
                entry_vars["Brand"].get(),
                entry_vars["Category"].get(),
                entry_vars["Department"].get(),
                entry_vars["Group"].get())]
            ), width=200).pack(pady=10)
        ctk.CTkButton(tab, text="Import CSV", command=self.import_csv, width=200).pack(pady=10)

        ctk.CTkButton(tab, text="Import Matrix Data", command=self.import_matrix_data, width=200).pack(pady=10)


    def export_csv(self):

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV files", "*.csv")
            ]
        )


        if filename:

            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(
                    file,
                    delimiter=";"
                )


                writer.writerow(
                    [
                        "StockCode",
                        "Description",
                        "Brand",
                        "Category",
                        "Department",
                        "Group"
                    ]
                )


                for row in self.table.get_children():

                    writer.writerow(
                        self.table.item(row)["values"]
                    )

    def import_csv(self):
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )
        if not filename:
            return

        expected_header = [
            "StockCode", "Description", "Brand",
            "Category", "Department", "Group"
        ]

        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=";")
                rows = list(reader)

            if not rows:
                return

            # skip header if it matches
            start_idx = 1 if rows[0] == expected_header else 0
            data_rows = rows[start_idx:]

            if not data_rows:
                return

            # Build a map: StockCode -> item_id
            stockcode_to_itemid = {}
            for item_id in self.table.get_children():
                values = self.table.item(item_id).get("values", [])
                if values:
                    stockcode = values[0]  # StockCode is column 0
                    if stockcode != "":
                        stockcode_to_itemid[str(stockcode)] = item_id

            for r in data_rows:
                r = (r + [""] * 6)[:6]  # ensure 6 columns
                stockcode = str(r[0]).strip()
                if not stockcode:
                    continue  # skip rows without StockCode

                # If exists, replace values; else insert
                if stockcode in stockcode_to_itemid:
                    item_id = stockcode_to_itemid[stockcode]
                    self.table.item(item_id, values=r)
                else:
                    # Insert new row
                    new_item_id = self.table.insert("", "end", values=r)
                    stockcode_to_itemid[stockcode] = new_item_id

            # This moves you back to the information tab when you are finished loading the data
            self.tabs.set("information")
        except Exception as e:
            messagebox.showerror("Import failed", str(e))

    def import_matrix_data(self):
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )
        if not filename:
            return

        # adjust expected header/order to match master CSV
        expected_header = ["StockCode", "Category", "Department", "Group"]

        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=";")
                rows = list(reader)

            if not rows:
                return

            # If header exists, skip it
            header = rows[0]
            start_idx = 1 if header == expected_header else 0
            data_rows = rows[start_idx:]
            if not data_rows:
                return
            for r in data_rows:
                r = (r + [""] * 4)[:4]

                key = str(r[0]).strip()  # e.g. "ENERGADE"
                if not key:
                    continue

                category = str(r[1]).strip()
                department = str(r[2]).strip()
                group = str(r[3]).strip()

                ApexEngine.BrandRules[key] = (category, department, group)

            messagebox.showinfo("Import complete", f"Loaded {len(ApexEngine.BrandRules)} BrandRules rows.")
            self.tabs.set("information")
        except Exception as e:
            messagebox.showerror("Import failed", str(e))

    def refresh_table(self):
        pass

    def load_data(self, data=None):
        if data == None:
            return
        for item in data:
            code, description, brand = item[:3]
            product = Apex_Codes(code, description, brand)

            category = product.get_category()
            if item[3:] == category:
                tag = ()
            else:
                tag = ("unknown",)
            self.table.insert("","end",
                # values=(code, description, brand, category[0], category[1], category[2]),
                values=(code, description, brand, item[3], item[4], item[5]), # this is user added data not master data
                tags=tag
            )
        # This moves you back to the information tab when you are finished loading the data
        self.tabs.set("information")


if __name__ == "__main__":
    from engine import Apex_Codes, ApexEngine
    App()
