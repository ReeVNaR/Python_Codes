import tkinter as tk
from tkinter import ttk, messagebox

# --- CLI Code (commented out) ---
# print("📏 Welcome to the Unit Converter!")
# print("Choose the conversion type:")
# print("1. cm to m")
# print("2. m to cm")
# print("3. km to m")
# print("4. inch to cm")
# print("5. feet to cm")
# print("6. kg to grams")
# print("7. grams to kg")
# print("8. pounds to kg")
# print("9. kg to pounds")
# print("10. Celsius to Fahrenheit")
# print("11. Fahrenheit to Celsius")
# print("0. Exit")

# while True:
#     choice = input("Enter choice (0–11): ")
#     if choice == "0":
#         print("👋 Goodbye!")
#         break

#     if choice in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"}:
#         value = float(input("Enter the value to convert: "))

#         if choice == "1":
#             result = value / 100
#             print(f"{value} cm = {result} m")
#         elif choice == "2":
#             result = value * 100
#             print(f"{value} m = {result} cm")
#         elif choice == "3":
#             result = value * 1000
#             print(f"{value} km = {result} m")
#         elif choice == "4":
#             result = value * 2.54
#             print(f"{value} inch = {result} cm")
#         elif choice == "5":
#             result = value * 30.48
#             print(f"{value} feet = {result} cm")
#         elif choice == "6":
#             result = value * 1000
#             print(f"{value} kg = {result} grams")
#         elif choice == "7":
#             result = value / 1000
#             print(f"{value} grams = {result} kg")
#         elif choice == "8":
#             result = value * 0.45359237
#             print(f"{value} pounds = {result} kg")
#         elif choice == "9":
#             result = value / 0.45359237
#             print(f"{value} kg = {result} pounds")
#         elif choice == "10":
#             result = (value * 9/5) + 32
#             print(f"{value}°C = {result}°F")
#         elif choice == "11":
#             result = (value - 32) * 5/9
#             print(f"{value}°F = {result}°C")
#     else:
#         print("❌ Invalid choice")
#     print()  # Blank line for readability

# --- GUI Implementation ---

CONVERSIONS = [
    ("cm to m", lambda v: v / 100, "cm", "m"),
    ("m to cm", lambda v: v * 100, "m", "cm"),
    ("km to m", lambda v: v * 1000, "km", "m"),
    ("inch to cm", lambda v: v * 2.54, "inch", "cm"),
    ("feet to cm", lambda v: v * 30.48, "feet", "cm"),
    ("kg to grams", lambda v: v * 1000, "kg", "grams"),
    ("grams to kg", lambda v: v / 1000, "grams", "kg"),
    ("pounds to kg", lambda v: v * 0.45359237, "pounds", "kg"),
    ("kg to pounds", lambda v: v / 0.45359237, "kg", "pounds"),
    ("Celsius to Fahrenheit", lambda v: (v * 9/5) + 32, "°C", "°F"),
    ("Fahrenheit to Celsius", lambda v: (v - 32) * 5/9, "°F", "°C"),
]

def convert():
    try:
        value = float(value_entry.get())
        idx = conversion_combo.current()
        if idx == -1:
            messagebox.showerror("Error", "Please select a conversion type.")
            return
        label_from = CONVERSIONS[idx][2]
        label_to = CONVERSIONS[idx][3]
        result = CONVERSIONS[idx][1](value)
        result_label.config(text=f"{value} {label_from} = {result} {label_to}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Unit Converter")

mainframe = ttk.Frame(root, padding="16")
mainframe.grid(row=0, column=0, sticky="NSEW")

ttk.Label(mainframe, text="📏 Unit Converter", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

ttk.Label(mainframe, text="Value:").grid(row=1, column=0, sticky="E")
value_entry = ttk.Entry(mainframe, width=20)
value_entry.grid(row=1, column=1, sticky="W")

ttk.Label(mainframe, text="Conversion:").grid(row=2, column=0, sticky="E")
conversion_combo = ttk.Combobox(mainframe, values=[c[0] for c in CONVERSIONS], state="readonly", width=25)
conversion_combo.grid(row=2, column=1, sticky="W")
conversion_combo.current(0)

convert_btn = ttk.Button(mainframe, text="Convert", command=convert)
convert_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(mainframe, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=(5, 0))

root.mainloop()
