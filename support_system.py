class SmartEntry:
  @staticmethod
  def refine_input(user_text):
    return user_text.replace('++', '+').replace('--', '-').replace('xx', '*')

class FactionModification:
  @staticmethod
  def to_fraction_format (nnumeric_value):
    from fractions import Fraction
    return str(Fraction(nnumeric_value).limit_denominator())
  
class DecimalModification:
  pass
