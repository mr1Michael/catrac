import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

# Widgets for Tab 1
tab1 = tabview.tab("Tab 1")
ctk.CTkLabel(tab1, text="Content in Tab 1").pack(pady=20)

# Widgets for Tab 2
tab2 = tabview.tab("Tab 2")
ctk.CTkLabel(tab2, text="Content in Tab 2").pack(pady=20)

# Widgets for Tab 3
tab3 = tabview.tab("Tab 3")
ctk.CTkLabel(tab3, text="Content in Tab 3").pack(pady=20)

app.mainloop()
