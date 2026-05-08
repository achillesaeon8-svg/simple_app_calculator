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

        'kg→g': 1000, 'g→kg': 0.001, 
        'm→cm': 100, 'cm→m': 0.01,
        'km→m': 1000, 'm→km': 0.001,
        'lb→kg': 0.4535, 'kg→lb': 2.2046,

        'hr→min': 60, 'min→hr': 1/60,
        'min→sec': 60, 'sec→min': 1/60,
        'day→hr': 24, 'hr→day': 1/24
      }