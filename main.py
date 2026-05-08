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
        cleaned_input = Smart