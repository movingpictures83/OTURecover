import sys
import numpy
from scipy import stats

class OTURecoverPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
       line = self.infile.readline()
       contents = line.strip().split(',')
       n = len(contents)-1

       a = []
       for line in self.infile:
          contents = line.strip().split(',')
          nonzero = 0
          for i in range(1, len(contents)):
              if (float(contents[i]) != 0):
                 nonzero += 1
          a.append(nonzero)

       outfile = open(filename, 'w')
       outfile.write("Mean OTUs Recovered: "+str(numpy.mean(a))+"\n")
       outfile.write("Standard Deviation: "+str(stats.sem(a))+"\n")
