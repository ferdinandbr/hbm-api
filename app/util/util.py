import math

def calculateValue(time, accurary):
  PI = math.pi
  result = -0.06366 + 0.12613 * math.cos(PI * time / 500) + 0.12258 * math.cos(PI * time / 250) + 0.01593 * math.sin(PI * time / 500) + 0.03147 * math.sin(PI * time / 250)
  if accurary is not None:
      return round(result, accurary)

  return result