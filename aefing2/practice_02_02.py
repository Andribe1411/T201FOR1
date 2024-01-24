# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>
vindstig = ["Logn","Andvari","Kul","Gola","Stinningsgola","Kaldi",
            "Stinningskaldi","Allhvass vindur","Hvassvidri","Stormur",
            "Rok","Ofsavedur","Farvidri"]
windSpeed = float(input("Wind speed: "))
windSpeed = round(windSpeed,1)
if windSpeed >200 or windSpeed<0:
    print("Illegal wind speed")
elif windSpeed >= 0 and windSpeed <= 0.2:
    print(vindstig[1])
elif windSpeed >= 0.3 and windSpeed <= 1.5:
    print(vindstig[2])
elif windSpeed >= 1.6 and windSpeed <= 3.3:
    print(vindstig[3])
elif windSpeed >= 3.4 and windSpeed <= 5.4:
    print(vindstig[4])
elif windSpeed >= 5.5 and windSpeed <= 7.9:
    print(vindstig[5])
elif windSpeed >= 8 and windSpeed <= 10.7:
    print(vindstig[6])
elif windSpeed >= 10.8 and windSpeed <= 13.8:
    print(vindstig[7])
elif windSpeed >= 13.9 and windSpeed <= 17.1:
    print(vindstig[8])
elif windSpeed >= 17.2 and windSpeed <= 20.7:
    print(vindstig[9])
elif windSpeed >= 20.8 and windSpeed <= 24.4:
    print(vindstig[10])
elif windSpeed >= 24.5 and windSpeed <= 28.4:
    print(vindstig[11])
elif windSpeed >= 28.5 and windSpeed <= 32.6:
    print(vindstig[12])
elif windSpeed >= 32.7:
    print(vindstig[13])