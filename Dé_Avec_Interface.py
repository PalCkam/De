import random
import tkinter as tk
from tkinter import messagebox

def roll_dice():
    try:
        faces = int(entry_faces.get())
        number_of_dice = int(entry_dice.get())
        
        if faces <= 0 or number_of_dice <= 0:
            raise ValueError("Les nombres doivent être supérieurs à zéro.")
        
        results = [random.randint(1, faces) for _ in range(number_of_dice)]
        total = sum(results)
        
        result_text = "\n".join([f"Dé {i + 1} : {result}" for i, result in enumerate(results)])
        result_label.config(text=f"{result_text}\n\nRésultat total : {total}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides pour les faces et les dés.")

def reset_fields():
    entry_faces.delete(0, tk.END)
    entry_dice.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Simulateur de lancer de dés")

tk.Label(root, text="Nombre de faces par dé :").grid(row=0, column=0, padx=10, pady=5)
entry_faces = tk.Entry(root)
entry_faces.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nombre de dés à lancer :").grid(row=1, column=0, padx=10, pady=5)
entry_dice = tk.Entry(root)
entry_dice.grid(row=1, column=1, padx=10, pady=5)

roll_button = tk.Button(root, text="Lancer les dés", command=roll_dice)
roll_button.grid(row=2, column=0, columnspan=2, pady=10)

reset_button = tk.Button(root, text="Réinitialiser", command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
