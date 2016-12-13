
from ROOT import *
import os
import math
def compressSelection(sel):
  if sel == "N/A": return sel
  splitSel = sel.split(" && ")
  selVars = dict()
  print sel
  for s in splitSel:
    print s
    if s == "": continue
    if ">" in s:
      v = s.split(" > ")[0]
      val = s.split(" > ")[1]
      selVars[v] = [">",val]
    else:
      v = s.split(" < ")[0]
      val = s.split(" < ")[1]
      selVars[v] = ["<",val]
      
  retString = ""
  for v in sorted(selVars.keys()):
    retString += " && %s %s %s"%(v,selVars[v][0],selVars[v][1])

  print retString
  return retString

fileList = open("rejFiles.list")

origSelGlob = "hasGoodVertex && (hasDoubleElTriggers || hasDoubleMuTriggers) && ONZ && NBASICCALOJETS > 0 && PTOSSF > 50"
selStart = "hasGoodVertex > 0.5 && (hasDoubleElTriggers > 0.5 || hasDoubleMuTriggers > 0.5) && ONZ > 0.5 && NBASICCALOJETS > 0" 
origSelObj = " && BETA > 0.9 && MEDIANIPLOG10SIG > 0.868 && MEDIANLOG10TRACKANGLE > -1.8 && TOTALTRACKANGLE > 0.1 && SUMIPSIG > 50.0 && TOTALTRACKPT > 5.0"


processes = []
masses = []
ctaus = []

for line in fileList.readlines():
  process = line.split("HToSSTo")[-1].split("_")[0]
  mass = line.split("_MS")[-1].split("_")[0]
  ctau = line.split("_ctauS")[-1].split("_")[0]
  
  if process not in processes: processes.append(process)
  if mass not in masses: masses.append(mass)
  if ctau not in ctaus: ctaus.append(ctau)

dat = dict()

for p in processes:
  dat[p] = dict()
  for m in masses:
    dat[p][m] = dict()
    for t in ctaus:
      dat[p][m][t] = ["N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A"]

fileList = open("rejFiles.list")

for line in fileList.readlines():
  split = os.popen("tail -n 17 " + line[0:-1]).read().split("\n")
  if len(split) == 1: continue
  #for i in range(len(split)): print str(i)+":\t"+split[i]
  
  selGlob = split[0]
  selObj = split[1]
  BrejTot = split[8].split(" ")[-1]
  SeffTot = split[9].split(" ")[-1]
  BrejOrig = split[14].split(" ")[-1]
  SeffOrig = split[15].split(" ")[-1]
  if BrejTot != "N/A":
    sign = float(SeffTot)/(math.sqrt((1-float(BrejTot))) + 3/2 + 0.2*(1-float(BrejTot))) if float(BrejTot) < 1 else 0
    signOrig = float(SeffOrig)/(math.sqrt((1-float(BrejOrig)))  + 3/2 + 0.2*(1-float(BrejOrig))) if float(BrejOrig) < 1 else 0
  else:
    sign = "N/A"
    signOrig = "N/A"


  process = line.split("HToSSTo")[-1].split("_")[0]
  mass = line.split("_MS")[-1].split("_")[0]
  ctau = line.split("_ctauS")[-1].split("_")[0]

  dat[process][mass][ctau] = [selGlob,selObj,BrejTot,SeffTot,BrejOrig,SeffOrig,sign,signOrig]

outfile1 = open("rejections1.txt",'w')

outfile1.write("ZH signal automatic cut data \norignal region: %s\noriginal selection: %s\n"%(origSelGlob,origSelObj))

for process in sorted(processes):
  outfile1.write(process + '\n')
  for mass in sorted(masses):
    outfile1.write('  mass: ' + mass + '\n')
    for ctau in sorted(ctaus):
      selGlob = dat[process][mass][ctau][0]
      selObj = dat[process][mass][ctau][1]
      if selObj != "N/A": selObj="OBJECT: " + compressSelection(selObj[8:])
      if selGlob != "N/A": selGlob="GLOBAL: " + compressSelection(selGlob[8+len(selStart):])

      print dat[process][mass][ctau]
      
      brej = dat[process][mass][ctau][2]
      seff = dat[process][mass][ctau][3]
      brejOrig = dat[process][mass][ctau][4]
      seffOrig = dat[process][mass][ctau][5]
      sign = dat[process][mass][ctau][6]
      signOrig = dat[process][mass][ctau][7]

      outfile1.write('    ctau: ' + ctau + '\n')
      outfile1.write('      ' + selGlob + '\n')
      outfile1.write('      ' + selObj + '\n')
      outfile1.write('      bkg rejec: ' + str(brej) + "   /   original: " + str(brejOrig) + '\n')
      outfile1.write('      sig effic: ' + str(seff) + "   /   original: " + str(seffOrig) + '\n')
      outfile1.write('      Punzi Sig: ' + str(sign) + "   /   original: " + str(signOrig) + '\n')

    outfile1.write('\n')
  outfile1.write('\n')


outfile2 = open("rejections2.txt",'w')

outfile1.write("ZH signal automatic cut data \norignal region: %s\noriginal selection: %s\n"%(origSelGlob,origSelObj))

for ctau in sorted(ctaus):
  outfile2.write("ctau: " + ctau + '\n')
  for mass in sorted(masses):
    outfile2.write('  mass: ' + mass + '\n')
    for process in sorted(processes):
      selGlob = dat[process][mass][ctau][0]
      selObj = dat[process][mass][ctau][1]
      if selObj != "N/A": selObj="OBJECT: " + compressSelection(selObj[8:])
      if selGlob != "N/A": selGlob="GLOBAL: " + compressSelection(selGlob[8+len(selStart):])

      brej = dat[process][mass][ctau][2]
      seff = dat[process][mass][ctau][3]
      brejOrig = dat[process][mass][ctau][4]
      seffOrig = dat[process][mass][ctau][5]
      sign = dat[process][mass][ctau][6]
      signOrig = dat[process][mass][ctau][7]

      outfile2.write('    process: ' + process + '\n')
      outfile2.write('      ' + selGlob + '\n')
      outfile2.write('      ' + selObj + '\n')
      outfile2.write('      bkg rejec: ' + str(brej) + "   /   original: " + str(brejOrig) + '\n')
      outfile2.write('      sig effic: ' + str(seff) + "   /   original: " + str(seffOrig) + '\n')
      outfile2.write('      Punzi Sig: ' + str(sign) + "   /   original: " + str(signOrig) + '\n')

    outfile2.write('\n')
  outfile2.write('\n')


outfile3 = open("rejections3.txt",'w')
for ctau in sorted(ctaus):
  for mass in sorted(masses):
    for process in sorted(processes):
      selGlob = dat[process][mass][ctau][0]
      selObj = dat[process][mass][ctau][1]
      if selObj != "N/A": 
        selObj=compressSelection(selObj[8:])
        outfile3.write("%s %s %s"%(ctau,mass,process) + '\n')
        outfile3.write(selObj + "\n\n")
      if selGlob != "N/A": 
        selGlob=compressSelection(selGlob[8+len(selStart):])
