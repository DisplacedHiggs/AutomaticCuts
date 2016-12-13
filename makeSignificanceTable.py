from prettytable import PrettyTable
from pprint import pprint
import math

infile = open("cutSetSignficance.txt")

cutSetNames = [
"Cut Set 1",
"Cut Set 1b",
"Cut Set 1c",
"Cut Set 1d",
"Cut Set 2",
"Cut Set 2b",
"Original",
"Automatic"
]

data = dict()
punzis = dict()
sigEffs = dict()
bkgEffs = dict()
for cut in cutSetNames:
  data[cut] = []
  punzis[cut] = 0.
  bkgEffs[cut] = 0.
  sigEffs[cut] = 0.

nSamples = 0
mass = 0
ctau = 0
process = "N/A"

for line_ in infile.readlines():
  line = line_[:-1]
  print line
  if "13TeV" in line:
    if nSamples != 0:
      for cut in cutSetNames:
        sigEff = sigEffs[cut]
        bkgEff = bkgEffs[cut]
        punzi = punzis[cut]
        #data[cut].append([mass,ctau,process,score1,score1b,score1c,score1d,score2,score2b,original,automatic])
        data[cut].append([mass,ctau,process,sigEff,1-bkgEff,punzi,sigEff/math.sqrt(bkgEff)])

    process = line.split("HToSSTo")[-1].split("_")[0]
    mass = line.split("_MS")[-1].split("_")[0]
    ctau = line.split("_ctauS")[-1].split("_")[0]
    continue

  if len(line) == 0: continue
 
  for cut in cutSetNames:
    if cut + ":" in line:
      punzis[cut] = float(line.split('\t')[1])
      bkgEffs[cut] = float(line.split('\t')[5])
      sigEffs[cut] = float(line.split('\t')[3])
      break
  
  nSamples += 1
    
for cut in data.keys():
  outfile = open("punzi_cutsets_%s.txt"%(cut.replace(" ","_")),'w')
  t = PrettyTable(["Mass","Ctau (mm)","process","sig eff","bkg rej","punzi","s/sqrt(b)"])
  #t = PrettyTable(["Mass","Ctau (mm)","process","set 1","set 1b","set 1c","set 1d","set 2","set 2b","original","automatic"])
  for x in data[cut]:
    t.add_row(x)
  outfile.write(str(t))
