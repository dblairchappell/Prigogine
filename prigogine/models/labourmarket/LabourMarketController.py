import time
from prigogine.Prigogine import *
start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm", "LabourMarketRunscript.prs")

end = time.clock()
print "time elapsed: " + str(end - start) + "s"







