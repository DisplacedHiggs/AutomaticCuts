# AutomaticCuts

createAutoCut.sh
  create scripts for condor submission (will need to be modified for use on LPC) 

findRejPattern.py  
  organize output of AutoCut into readable data
  
makeAutoCut_global.py
  script for automatically generating global cuts (will need to be modified to match new trees)

makeAutoCut_object.py 
  script to generate object-level cuts (will need to be modified to match new trees)
  
makeCutSignficance.py  
  script to generate significances for different cutsets (will need to be modified to match new trees)
  
makeSignificanceTable.py  
  organize output of makeSignificanceCut into readable data

runAutoCut.sh
  run script for condor (will need to be modified for use on LPC)
  
signalfiles.list
  list of signal files, need this for createAutoCut
