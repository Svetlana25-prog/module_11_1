import matplotlib.pyplot as plt
import numpy
days = [1,2,3,4,5,6,7]
r = numpy.array([100, 102, 99, 98, 90, 120, 88])

plt.plot(days, r, color='blue')
plt.title('$')
plt.xlabel('Дни')
plt.ylabel('Курс')

plt.show()