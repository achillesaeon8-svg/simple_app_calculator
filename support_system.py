class SmartEntry:
  @staticmethod
  def refine_input(user_text):
    return user_text.replace('++', '+').replace('--', '-').replace('xx', '*')

class FactionModification:
  pass
class DecimalModification:
  pass
