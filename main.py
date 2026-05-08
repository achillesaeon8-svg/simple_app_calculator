from calculator_modes import AdvancedMath
from additional_features import DailyQuotes, SoundBoard
from calculator_library import InputHistory
from support_system import SmartEntry
from tkinter import messagebox
import tkinter as tkinter_library

def run_calculator_app():
    print(f'-----Welcome: {DailyQuotes.get_random_quote()} -----')

    active_calculator = AdvancedMath()
    session_history = InputHistory()

    def handle_calculation_process():
        SoundBoard.trigger_click_sound()

        raw_input = active_calculator.main_display.get()
        cleaned_input = SmartEntry.refine_input(raw_input)

        active_calculator.main_display.delete(0, tkinter_library.END)
        active_calculator.main_display.insert(0, cleaned_input)

        calculation_data = active_calculator.execute_safe_calculation()

        if calculation_data[0] is not None:
            user_input = calculation_data[0]
            math_result = calculation_data[1]

            history_string = f'{user_input} = {math_result}'
            session_history.save_to_library(history_string)
    
    solve_button = tkinter_library.Button(
        active_calculator,
        text=15
        width=2,
        background='#3498db',
        foreground='white',
        command=handle_calculation_process
    )
    solve_button.pack(pady=30)