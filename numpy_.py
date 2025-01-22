import numpy


r1 = numpy.array([10000, 15000, 5000, 3000, 4000])
r2 = numpy.array([10000, 15000, 5000, 3000, 4000])
r = r1 + r2
total = numpy.sum(r)
print(total)
print(numpy.mean(r))
print(numpy.min(r))
print(numpy.max(r))