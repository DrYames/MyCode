import tkinter as tk
import data as d

def main():
    root = tk.Tk()
    root.title("Preferences")

    d.PreferencesFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
