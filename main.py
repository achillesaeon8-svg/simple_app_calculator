import tkinter as tkinter_library
from calculator_settings import FundamentalOperations
from calculator_modes import CalculatorUI
from additional_features import DailyQuotes
from support_system import ConversionRates

class CalculatorApp:
    def __init__(self):
        self.app = FundamentalOperations()
        self.history_logs = []
        self.modes = ["Basic", "Advanced", "Units", "Currency", "Time"]
        self.idx = 0

        self.app.bind('<Return>', lambda e: self.handle_press("="))
        self.app.bind('<Escape>', lambda e: self.handle_press("C"))

        self.quote = tkinter_library.Label(self.app.button_frame, text=DailyQuotes.get_random_quote(), 
                                         font=("Arial", 16, "italic"), bg="#2c3e50", fg="white")
        self.quote.pack(expand=True)
        self.app.after(1500, lambda: self.app.fade_intro_text(self.quote))
        self.app.after(2500, self.setup_ui)
        self.app.mainloop()

    def handle_press(self, key):
        if "ERROR:" in self.app.main_display.get():
            self.app.main_display.delete(0, 'end')

        if key == "=":
            equation, result = self.app.execute_safe_calculation()
            if equation != "Error": self.history_logs.append(f"{equation} = {result}")
        elif key == "C": 
            self.app.main_display.delete(0, 'end')
        elif key == "History": 
            CalculatorUI.draw_history_view(self.app, self.history_logs, self.handle_press)
        elif key == "Back": 
            CalculatorUI.draw_basic_mode(self.app, self.handle_press)
        elif "→" in key:
            equation, result = ConversionRates.perform_conversion(self.app, key)
            if equation != "Error": self.history_logs.append(f"{equation} -> {result}")
        else:
            self.app.main_display.insert(tkinter_library.END, key)

    def setup_ui(self):
        nav = tkinter_library.Frame(self.app, bg="#2c3e50")
        nav.pack(fill='x', pady=5)
        for t, c in [("MODE", self.rotate), ("FRAC", self.frac), ("DEC", self.dec)]:
            tkinter_library.Button(nav, text=t, font=("Arial", 9, "bold"), command=c).pack(side="left", padx=5)
        CalculatorUI.draw_basic_mode(self.app, self.handle_press)

    def rotate(self):
        self.idx = (self.idx + 1) % len(self.modes)
        m = self.modes[self.idx]
        if m == "Basic": CalculatorUI.draw_basic_mode(self.app, self.handle_press)
        elif m == "Advanced": CalculatorUI.draw_advanced_mode(self.app, self.handle_press)
        elif m == "Units": CalculatorUI.draw_unit_mode(self.app, self.handle_press)
        elif m == "Currency": CalculatorUI.draw_currency_mode(self.app, self.handle_press)
        elif m == "Time": CalculatorUI.draw_time_mode(self.app, self.handle_press)

    def frac(self):
        from fractions import Fraction
        try:
            v = float(self.app.main_display.get())
            self.app.main_display.delete(0, 'end'); self.app.main_display.insert(0, str(Fraction(v).limit_denominator()))
        except: pass

    def dec(self):
        from fractions import Fraction
        try:
            v = self.app.main_display.get()
            self.app.main_display.delete(0, 'end'); self.app.main_display.insert(0, str(float(Fraction(v))))
        except: pass

if __name__ == "__main__":
    CalculatorApp()