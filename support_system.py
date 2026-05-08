class ConversionRates:
  @staticmethod
  def perform_conversion(app, key):
    try:
      value_string = app.main_display.get()
      value = float(value_string)

      rates = {
        '$→₱': 58.45, '₱→$': 0.017, 
        'KRW→₱': 0.042, '₱→KRW': 23.81, 
        '¥→₱': 0.37, '₱→¥': 2.70,
        '€→₱': 63.12, '₱→€': 0.015,

        
      }