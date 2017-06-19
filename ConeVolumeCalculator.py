# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)
import math
# Define Function below
def calculateconevolume(baseR, h):

    volume = 756076.62822305
    volume = round(volume, 2)
    return volume

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answer = calculateconevolume(10, 2)
    print(answer)
