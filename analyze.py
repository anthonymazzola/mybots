import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
#frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
sinArr = numpy.load('data/arrayValues.npy')
#print(backLegSensorValues)
#print(frontLegSensorValues)

sinArray = matplotlib.pyplot.plot(sinArr)


#back = matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg",linewidth=4)
#front = matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()