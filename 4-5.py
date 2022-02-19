#5
def str_float(s):
  try:
    return float(s)
  except ValueError:
    print("Invalid input")

print(str_float("6.0"))

print(str_float('Ohtani'))

