# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

windSpeed = float(input("Wind speed: "))
windSpeed = round(windSpeed,1)
if windSpeed >200 or windSpeed<0:
    print("Illegal wind speed")
elif windSpeed >= 0 and windSpeed <= 0.2:
    print("Logn")
elif windSpeed >= 0.3 and windSpeed <= 1.5:
    print("Andvari")
elif windSpeed >= 1.6 and windSpeed <= 3.3:
    print("Kul")
elif windSpeed >= 3.4 and windSpeed <= 5.4:
    print("Gola")
elif windSpeed >= 5.5 and windSpeed <= 7.9:
    print("Stinningsgola")
elif windSpeed >= 8 and windSpeed <= 10.7:
    print("Kaldi")
elif windSpeed >= 10.8 and windSpeed <= 13.8:
    print("Stinningskaldi")
elif windSpeed >= 13.9 and windSpeed <= 17.1:
    print("Allhvass vindur")
elif windSpeed >= 17.2 and windSpeed <= 20.7:
    print("Hvassvidri")
elif windSpeed >= 20.8 and windSpeed <= 24.4:
    print("Stormur")
elif windSpeed >= 24.5 and windSpeed <= 28.4:
    print("Rok")
elif windSpeed >= 28.5 and windSpeed <= 32.6:
    print("Ofsavedur")
elif windSpeed >= 32.7:
    print("Farvidri")