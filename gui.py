import customtkinter as ctk
from tkinter import ttk, filedialog

import csv

from engine import Apex_Codes, ApexEngine


class App:

    def __init__(self):

        self.window = ctk.CTk()

        self.window.title("Apex Inventory Engine")
        self.window.geometry("1000x600")


        # Title
        self.label = ctk.CTkLabel(
            self.window,
            text="Apex Code Categorisation System",
            font=("Arial", 20)
        )

        self.label.pack(pady=20)


        # Table frame
        self.table_frame = ctk.CTkFrame(self.window)
        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        # Table
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
            self.table.heading(
                col,
                text=col
            )

            self.table.column(
                col,
                width=150
            )

        self.table.pack(
            fill="both",
            expand=True
        )

        self.export_button = ctk.CTkButton(
            self.window,
            text="Export CSV",
            command=self.export_csv
        )

        self.export_button.pack(pady=10)
        self.refresh_button = ctk.CTkButton(
            self.window,
            text="Refresh",
            command=self.refresh_table
        )

        self.refresh_button.pack(pady=10)

        # Test data
        self.load_test_data()


        self.window.mainloop()


    def load_test_data(self):

        data = [
            (
                "AP19368",
                "Energade - Blueberry 24x500ml",
                "Energade"
            ),

            (
                "AP20001",
                "Fresh Garlic 500g",
                "Unknown"
            ),

            (
                "AP30001",
                "Random Product",
                "ABC"
            )
        ]


        for item in data:
            code, description, brand = item

            product = Apex_Codes(
                code,
                description,
                brand
            )

            category = product.get_category()

            tag = ()

            if category[0] == "Unknown":
                tag = ("unknown",)

            self.table.insert(
                "",
                "end",
                values=(
                    code,
                    description,
                    brand,
                    category[0],
                    category[1],
                    category[2]
                ),
                tags=tag
            )
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
    def refresh_table(self):
        pass #
