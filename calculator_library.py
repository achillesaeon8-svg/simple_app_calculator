class InputHistory:
  def __init__(self):
    self.calculation_logs = []
  
  def save_to_library(self, math_entry):
    self.calculation_logs.append(math_entry)
    with open ('calculation_history.txt', 'a') as history_file:
      history_file.write(math_entry + '\n')
