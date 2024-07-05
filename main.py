import tkinter as tk
import random
from datetime import date

class DailyMotivationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Motivation App")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.quotes = [
            "Believe in yourself!",
            "You can do it!",
            "Keep pushing forward!",
            "Never give up!",
            "Stay positive, work hard, make it happen!",
            "Your only limit is you.",
            "Dream it. Wish it. Do it.",
            "Success is not for the lazy.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
            "Don't watch the clock; do what it does. Keep going."
        ]

        self.daily_quote = tk.StringVar()
        self.set_daily_quote()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Daily Motivation", font=("Helvetica", 20, "bold")).pack(pady=10)

        self.quote_label = tk.Label(self.root, textvariable=self.daily_quote, wraplength=400, justify="center", font=("Helvetica", 16))
        self.quote_label.pack(pady=20)

        tk.Button(self.root, text="New Quote", command=self.get_new_quote, font=("Helvetica", 14)).pack(pady=10)

    def set_daily_quote(self):
        # This function would ideally set the quote based on the current date.
        # For simplicity, we'll just set a random quote on startup.
        self.daily_quote.set(random.choice(self.quotes))

    def get_new_quote(self):
        self.daily_quote.set(random.choice(self.quotes))

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyMotivationApp(root)
    root.mainloop()
