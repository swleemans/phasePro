import tkinter as tk

def main():
    root = tk.Tk()
    root.title("super cool app")
    root.geometry("400x400")
    

    # --------------------------
    # Slider (Scale) Widget
    # --------------------------
    slider_label = tk.Label(root, text="Adjust the slider:")
    slider_label.pack(pady=5)
    
    # Create a horizontal slider ranging from 0 to 100
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    slider.pack(pady=5)

    # --------------------------
    # Dropdown (OptionMenu) Widget
    # --------------------------
    dropdown_label = tk.Label(root, text="Choose an option:")
    dropdown_label.pack(pady=5)
    
    # Create a StringVar to hold the selected option
    option_var = tk.StringVar(root)
    option_var.set("Option 1")  # Set a default value
    
    # Define the options for the drop-down menu
    options = ["Option 1", "Option 2", "Option 3"]
    dropdown = tk.OptionMenu(root, option_var, *options)
    dropdown.pack(pady=5)

    # --------------------------
    # Button to demonstrate retrieving values
    # --------------------------
    def print_values():
        # Print the current slider value and the selected dropdown option
        print("Slider value:", slider.get())
        print("Dropdown selection:", option_var.get())

    button = tk.Button(root, text="Print Values", command=print_values)
    button.pack(pady=10)
    root.mainloop()

if __name__ =='__main__':
    main()

