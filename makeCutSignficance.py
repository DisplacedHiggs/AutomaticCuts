from ROOT import *
from array import array
from multiprocessing import Process, Queue
import sys
import math
import os

colors = [kBlue,kRed,kMagenta+1,kGreen+3,kOrange+2,kTeal-7,kAzure-6,kViolet-6,kCyan+3,kRed+3,kGreen-2]
gStyle.SetOptStat(0)

nPoints = 200
product = "BASICCALOJETS1MATCHED"

VarList_obj = []
UpBoundList_obj = []
LowBoundList_obj = []
GoesDownList_obj = []
isGlobalList_obj = []

VarList_obj.append("PT")
LowBoundList_obj.append("0.0")
UpBoundList_obj.append("500.0")
GoesDownList_obj.append(False)
isGlobalList_obj.append(False)

# VarList_obj.append("ALPHAMAX")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(True)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCAPLANARITY")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCIATEDTRACKPT")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("200.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCSPHERICITY")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCTHRUSTMAJOR")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCTHRUSTMINOR")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("AVFASSOCSPHERICITY")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("AVFASSOCTHRUSTMAJOR")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("AVFASSOCTHRUSTMINOR")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("BETA")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("MEDIANIPLOG10SIG")
# LowBoundList_obj.append("-1.0")
# UpBoundList_obj.append("4.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("MEDIANLOG10TRACKANGLE")
# LowBoundList_obj.append("-4.0")
# UpBoundList_obj.append("1.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("MISSINGINNER")
# LowBoundList_obj.append("0")
# UpBoundList_obj.append("10")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("SUMIP")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("750.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("SUMIPSIG")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("750.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)
 
# VarList_obj.append("TOTALTRACKPT")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("200.0")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("TOTALTRACKANGLE")
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("3.142")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCIATEDTRACKPT_%s/TOTALTRACKPT"%(product))
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("100")
# GoesDownList_obj.append(True)
# isGlobalList_obj.append(False)

# VarList_obj.append("ASSOCIATEDTRACKPT_%s/NMATCHEDTRACKS"%(product))
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("100")
# GoesDownList_obj.append(True)
# isGlobalList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("SUMIPSIG_%s/NMATCHEDTRACKS"%(product))
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("100")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

# VarList_obj.append("SUMIP_%s/NMATCHEDTRACKS"%(product))
# LowBoundList_obj.append("0.0")
# UpBoundList_obj.append("100")
# GoesDownList_obj.append(False)
# isGlobalList_obj.append(False)

#-----------------------global variables-------------------------

VarList_glob = []
UpBoundList_glob = []
LowBoundList_glob = []
GoesDownList_glob = []
isGlobalList_glob = []

VarList_glob.append("HT")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("1000.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

# VarList_glob.append("LRM")
# LowBoundList_glob.append("0.0")
# UpBoundList_glob.append("1.0")
# GoesDownList_glob.append(True)
# isGlobalList_glob.append(True)

# VarList_glob.append("LSPH")
# LowBoundList_glob.append("0.0")
# UpBoundList_glob.append("1.0")
# GoesDownList_glob.append(False)
# isGlobalList_glob.append(True)

VarList_glob.append("Max_LEPTON_DPHI")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("3.142")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("Max_MEDIANIPLOG10SIG_BASICCALOJETS1MATCHED")
LowBoundList_glob.append("-1.0")
UpBoundList_glob.append("4.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("Max_SUMIPSIG_BASICCALOJETS1MATCHED")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("750.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("Max_TOTALTRACKANGLE_BASICCALOJETS1MATCHED")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("3.142")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("MET")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("300.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("Min_LEPTON_DPHI")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("3.142")
GoesDownList_glob.append(True)
isGlobalList_glob.append(True)

# VarList_glob.append("Min_LEPTON_DPHI")
# LowBoundList_glob.append("0.0")
# UpBoundList_glob.append("3.142")
# GoesDownList_glob.append(True)
# isGlobalList_glob.append(True)

VarList_glob.append("Alt_MT")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("500.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

VarList_glob.append("PTOSSF")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("400.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

# VarList_glob.append("SSPH")
# LowBoundList_glob.append("0.0")
# UpBoundList_glob.append("1.0")
# GoesDownList_glob.append(False)
# isGlobalList_glob.append(True)

VarList_glob.append("Alt_WPT")
LowBoundList_glob.append("0.0")
UpBoundList_glob.append("1000.0")
GoesDownList_glob.append(False)
isGlobalList_glob.append(True)

fileDir = "/cms/data23/sritata/VHdisplaced/histograms/VH_addedHistos_chunks"
filesBkg = []

mode = 0 
#0 for all bkg
#1 for W
#2 for Z

filesBkg.append("allHistos_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_*.root")
if mode in [0,1]:
  filesBkg.append("allHistos_WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8_*.root")
  filesBkg.append("allHistos_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_*.root")
  filesBkg.append("allHistos_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_*.root")
  filesBkg.append("allHistos_ST_tW_antitop_5f_DS_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_*.root")
  filesBkg.append("allHistos_ST_tW_top_5f_DS_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_*.root")
  filesBkg.append("allHistos_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_*.root")
if mode in [0,2]:
  filesBkg.append("allHistos_ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_*.root")
  filesBkg.append("allHistos_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_*.root")
  filesBkg.append("allHistos_DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_*.root")
  filesBkg.append("allHistos_ZHToTauTau_M125_13TeV_powheg_pythia8_*.root")
  filesBkg.append("allHistos_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_*.root")
  filesBkg.append("allHistos_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_*.root")
  filesBkg.append("allHistos_ZZTo4L_13TeV_powheg_pythia8_*.root")
  filesBkg.append("allHistos_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_*.root")
  filesBkg.append("allHistos_WWTo2L2Nu_13TeV-powheg_*.root")

filesSignal = [
  sys.argv[1]
]

signalSample = sys.argv[1].split("_0.root")[0].split("allHistos_")[-1]


xsecs = []
xsecs.append(831.76)
if mode in [0,1]: 
  xsecs.append(1.369 * 0.577 *0.324)
  xsecs.append(26.23)
  xsecs.append(44.09)
  xsecs.append(35.6)
  xsecs.append(35.6)
  xsecs.append(61526.7)
if mode in [0,2]:
  xsecs.append(0.8696 * 0.577 * 0.102)
  xsecs.append(6025.2)
  xsecs.append(7160)
  xsecs.append(0.8696 * 0.0622)
  xsecs.append(5.52)
  xsecs.append(4.43)
  xsecs.append(1.26)
  xsecs.append(3.38)
  xsecs.append(12.46)

def makeHisto(selectionRegion,i,j,doGlobal,queue):
  if doGlobal:
    VarList = VarList_glob
    UpBoundList = UpBoundList_glob
    LowBoundList = LowBoundList_glob
    GoesDownList = GoesDownList_glob
    isGlobalList = isGlobalList_glob  
  else:
    VarList = VarList_obj
    UpBoundList = UpBoundList_obj
    LowBoundList = LowBoundList_obj
    GoesDownList = GoesDownList_obj
    isGlobalList = isGlobalList_obj

  print "start: " + filesBkg[j]

  fileList = os.popen("ls %s/%s"%(fileDir,filesBkg[j])).read().split("\n")[:-1]
  
  for f in range(0,len(fileList)):
    inF = fileList[f].split('/')[-1]
    ff = TFile(fileDir + '/' + inF)
    # print inF
    tree = ff.Get("tree_" + product)
    tree.SetWeight(1.0)
    nocutCount = ff.Get("noCutSignature_COUNT")
    if f == 0:
      nEvents = nocutCount.GetEntries()
    else:
      nEvents += nocutCount.GetEntries()
    
    hname = "%s_%s"%(VarList[i],product) if not isGlobalList[i] else VarList[i]
    varexp = hname + ">>h%i%i(%s,%s,%s)"%(i,j,nPoints,LowBoundList[i],UpBoundList[i])
    
    
    
    tree.Draw(varexp,selectionRegion,"goff")
    h = TH1F(gDirectory.Get("h%i%i"%(i,j)))
    h.SetDirectory(0)
    
    if f == 0:
      hTot = h
    else:
      hTot.Add(h)
    
  if nEvents != 0: hTot.Scale(xsecs[j]/nEvents)
  
  queue.put(hTot)
  print "done: " + filesBkg[j]
  
def makeROC(gen,selectionRegion,doGlobal,previousVar): 
  outfilename = "pdfHistos/ROC_%s_%i_%s.pdf"%(signalSample,gen,"global" if doGlobal else "object")
  data = dict()
  histos = dict()

  if doGlobal:
    VarList = VarList_glob
    UpBoundList = UpBoundList_glob
    LowBoundList = LowBoundList_glob
    GoesDownList = GoesDownList_glob
    isGlobalList = isGlobalList_glob  
  else:
    VarList = VarList_obj
    UpBoundList = UpBoundList_obj
    LowBoundList = LowBoundList_obj
    GoesDownList = GoesDownList_obj
    isGlobalList = isGlobalList_obj
    
    
  for i in range(0,len(VarList)):
    var = VarList[i]
    data[var] = []
    data[var].append([])
    
    histos[var] = []

    #background
    print "\nBACKGROUND \n"
    data[var].append([])
    
    hBkg = TH1F()
    
    processes = []
    queues = []
    for j in range(0,len(filesBkg)):
      queues.append(Queue())
      processes.append(Process(target=makeHisto, args=(selectionRegion,i,j,doGlobal,queues[j])))
      
    hname = "%s_%s"%(VarList[i],product) if not isGlobalList[i] else VarList[i]
    varexp = hname + ">>h(%s,%s,%s)"%(nPoints,LowBoundList[i],UpBoundList[i])
    
    print hname
    print varexp
    
    for p in processes:
      p.start()
      
    for p in processes:
      p.join()
      
    for j in range(0,len(filesBkg)):
      h = queues[j].get()
      if j == 0: hBkg = h
      else: hBkg.Add(h)
    
    hBkg.SetDirectory(0)
    histos[var].append(hBkg)
    
    data[var][1].append(hBkg.Integral(-1,nPoints+1))
    if GoesDownList[i]:
      data[var][0].append(float(UpBoundList[i]))
      for k in range(0, nPoints):
        data[var][0].append(float(UpBoundList[i]) - 1.0*k/nPoints*(float(UpBoundList[i]) - float(LowBoundList[i])))
        data[var][1].append(1 - 1.0*hBkg.Integral(-1,nPoints - k)/data[var][1][0])
      data[var][0].append(float(LowBoundList[i]))
    else:
      data[var][0].append(float(LowBoundList[i]))
      for k in range(0, nPoints):
        data[var][0].append(float(LowBoundList[i]) + 1.0*k/nPoints*(float(UpBoundList[i]) - float(LowBoundList[i])))
        data[var][1].append(1 - 1.0*hBkg.Integral(k,nPoints+1)/data[var][1][0])
      data[var][0].append(float(UpBoundList[i]))
    data[var][1].append(1)
    # print data[var][1]

    
    #signal
    print "\nSIGNAL \n"
    for j in range(0,len(filesSignal)):
      data[var].append([])
      ff = TFile(fileDir + '/' + filesSignal[j].split("/")[-1])
      tree = ff.Get("tree_"+product)
      tree.SetWeight(1.0)
      
      hname = "%s_%s"%(VarList[i],product) if not isGlobalList[i] else VarList[i]
      varexp = hname + ">>h(%s,%s,%s)"%(nPoints,LowBoundList[i],UpBoundList[i])
      print hname
      print varexp
      tree.Draw(varexp,selectionRegion,"goff")
      print gDirectory.Get("h")
      h = TH1F(gDirectory.Get("h"))
      h.SetDirectory(0)
      histos[var].append(h)
      
      data[var][j+2].append(h.Integral(-1,nPoints+1))
      if GoesDownList[i]:
        for k in range(0, nPoints):
          data[var][j+2].append(1.0*h.Integral(-1,nPoints - k)/data[var][j+2][0])
      else:
        for k in range(0, nPoints):
          data[var][j+2].append(1.0*h.Integral(k,nPoints+1)/data[var][j+2][0])
      data[var][j+2].append(0)
      
  npage = 1
  canvas = TCanvas("c1","",1400,1400)
  canvas.Divide(2,2)
      
  latex = TLatex()
  latex.SetNDC()
  latex.SetTextFont(62)
  latex.SetTextSize(0.035)
  
  attempt = 0
  retval = [False,False,False,0,0,0,0]
  retval[3] = data[VarList[0]][1][0]
  retval[4] = data[VarList[0]][2][0]
  candValMax = 0
  for s in range(0,len(VarList)):        
    var = VarList[s]
    if var == previousVar: continue
    refGraph = TGraph()
    refGraph.SetMarkerColor(kBlack)
    refGraph.SetLineColor(kBlack)
    refGraph.SetMarkerStyle(1)
    refGraph.SetMarkerSize(0)
    
    for i in range(0, 201):
      refGraph.SetPoint(refGraph.GetN(),0.005*i,1-(0.005*i)*(0.005*i))
    
    legend = TLegend(0.82,0.78,0.98,0.98)
    legend.Clear()
    legend.SetFillColor(kWhite)
    legend.AddEntry(refGraph,"y=1-x^2","l")
    
    mg1 = TMultiGraph()
    mg1.Add(refGraph)
    mg2 = TMultiGraph()
    
    sigOrig = 0
    bkgOrig = 0
    
    for i in range(1,len(data[var])):
      if i == 1:
        bkgOrig=data[var][i][0]
        data[var][i][0]=0
      else:
        sigOrig=data[var][i][0]
        data[var][i][0]=1
    
    for i in range(2,len(data[var])):
      rocGraph  = TGraph()
      sSqrtB = TGraph()
      print "%s\n sig: %f\n bkg: %f\n"%(var,sigOrig,bkgOrig)
      print 
      for j in range(0,len(data[var][i])):
        cut = data[var][0][j]
        Brej = data[var][1][j]
        Seff = data[var][i][j]
        rocGraph.SetPoint(rocGraph.GetN(),Seff,Brej)
        if Brej != 1:
          sSqrtB.SetPoint(sSqrtB.GetN(),cut,Seff*(1-math.sqrt(1-math.pow(Seff,4)))/math.sqrt(1-Brej))
          if attempt == 0:
            candVal = Seff/(math.sqrt(1-Brej) + 3/2 + 0.2*(1-Brej))
          elif attempt == 1:
            candVal = Seff/(math.sqrt(1-Brej) + 3/2)
          elif attempt == 2:
            candVal = Seff/(math.sqrt(1-Brej) + 0.2*(1-Brej))
          elif attempt == 3:
            candVal = Seff/(math.sqrt(1-Brej))
            
          if candVal > candValMax and Brej > 1 - Seff*Seff and Brej > 0.15 and Seff > 0.6:
            candValMax = candVal
            retval[0] = var
            retval[1] = GoesDownList[s]
            retval[2] = cut
            retval[5] = Brej
            retval[6] = Seff
        
      rocGraph.SetLineColor(colors[i])
      rocGraph.SetMarkerColor(colors[i])
      sSqrtB.SetLineColor(colors[i])
      sSqrtB.SetMarkerColor(colors[i])
      
      legend.AddEntry(rocGraph,"signal%i"%(i-1),"l")
      mg1.Add(rocGraph)
      mg2.Add(sSqrtB)
      
    pad=canvas.cd(1)
    pad.SetGrid()
    
    mg1.Draw("al*")
    mg1.GetXaxis().SetTitle("signal efficiency")
    mg1.GetYaxis().SetTitle("background rejection (= 1 - bkgEff)")
    legend.Draw("e")
    
    hname = "%s_%s"%(VarList[s],product) if not isGlobalList[s] else VarList[s]
    latex.DrawLatex(0.02,0.95,hname + ": ROC curves - " + ("N < cut" if GoesDownList[s] else "N > cut"))
    latex.DrawLatex(0.16,0.85, "Step Size: " + str(math.fabs(data[var][0][0] - data[var][0][1])))
    
    pad = canvas.cd(2)
    mg2.Draw("al*")
    mg2.SetTitle(selectionRegion)
    mg2.GetXaxis().SetTitle("cut value")
    mg2.GetYaxis().SetTitle("candVal")
    if attempt == 0:
      # latex.DrawLatex(0.35,0.85,"S*#sqrt{#frac{1-S^{4}}{B}}")
      latex.DrawLatex(0.35,0.85,"PUNZI")
    elif attempt == 1:
      latex.DrawLatex(0.35,0.85,"PUNZI ALT 1")
    elif attempt == 2:
      latex.DrawLatex(0.35,0.85,"PUNZI ALT 2")
    elif attempt == 3:
      latex.DrawLatex(0.35,0.85,"#frac{S}{#sqrt{B}}")
    
    pad = canvas.cd(3)
    pad.SetLogy()
    legend2 = TLegend(0.82,0.78,0.98,0.98)
    legend2.Clear()
    legend2.SetFillColor(kWhite)
      
    for i in range(0,len(histos[var])):
      h = histos[var][i]
      if h.Integral()!=0: h.Scale(1./h.Integral())
      h.SetLineColor(colors[i])
      h.SetTitle(var)
      if i == 0:
        h.Draw()
        legend2.AddEntry(h,"background","l")
      else:
        h.Draw("same")
        legend2.AddEntry(h,"signal %i"%(i),"l")
        
    legend2.Draw()
    
    pad = canvas.cd(4)
    
    legend3 = TLegend(0.82,0.78,0.98,0.98)
    legend3.Clear()
    legend3.SetFillColor(kWhite)
    
    hEffis = []
    for i in range(0,len(histos[var])):
      h = histos[var][i]
      hE = h.Clone()
      hE.SetName("eff %s %i"%(var,i))
      hE.SetTitle("SigEff and BkgRej")
      for j in range(0,len(data[var][i+1])):
        hE.SetBinContent(j,data[var][i+1][j])
      hE.SetDirectory(0)
      hEffis.append(hE)
    
    for i in range(0,len(hEffis)):
      hE = hEffis[i]
      if i == 0:
        hE.Draw()
        legend3.AddEntry(hE,"bkg rej","l")
      else:
        hE.Draw("same")
        legend3.AddEntry(hE,"signal %i"%(i),"l")
        
    legend3.Draw()
    
    if npage == 1:
      canvas.Print(outfilename+"(","pdf")
    else:
      canvas.Print(outfilename,"pdf")
    canvas.Clear()
    canvas.Divide(2,2)
    npage += 1
  canvas.Print(outfilename+")","pdf")
  retval.append(attempt)
  return retval
  
def main():
  txtFile = open("pdfHistos/cutSetSignificance_%s.txt"%(signalSample),'w')
  txtFile.write("%s\n\n"%(signalSample))
  
  bkgOrig = 0
  sigOrig = 0
  
  selectionRegionOriginal = "hasGoodVertex > 0.5 && (hasDoubleElTriggers > 0.5 || hasDoubleMuTriggers > 0.5) && ONZ > 0.5 && NBASICCALOJETS > 0 && PTOSSF > 50"
  objSelectionOriginal = " && BETA_BASICCALOJETS1 > 0.9 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.868 && MEDIANLOG10TRACKANGLE_BASICCALOJETS1 > -1.8 && TOTALTRACKANGLE_BASICCALOJETS1 > 0.1 && SUMIPSIG_BASICCALOJETS1 > 50.0 && TOTALTRACKPT_BASICCALOJETS1 > 5.0".replace("BASICCALOJETS1",product)  
  
  selectionRegionStart = "hasGoodVertex > 0.5 && (hasDoubleElTriggers > 0.5 || hasDoubleMuTriggers > 0.5) && ONZ > 0.5 && NBASICCALOJETS > 0"
  objSelection = ""
  
  objectSelections = [
  " && ALPHAMAX_BASICCALOJETS1 < 0.25 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && PT_BASICCALOJETS1 > 20 && TOTALTRACKPT_BASICCALOJETS1 > 13 && SUMIPSIG_BASICCALOJETS1 > 35".replace("BASICCALOJETS1",product),
  " && ALPHAMAX_BASICCALOJETS1 < 0.25 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && PT_BASICCALOJETS1 > 20 && TOTALTRACKPT_BASICCALOJETS1 > 13".replace("BASICCALOJETS1",product),
  " && ALPHAMAX_BASICCALOJETS1 < 0.25 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && PT_BASICCALOJETS1 > 20".replace("BASICCALOJETS1",product),
  " && ALPHAMAX_BASICCALOJETS1 < 0.25 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && PT_BASICCALOJETS1 > 20 && MEDIANLOG10TRACKANGLE_BASICCALOJETS1 > -1.7".replace("BASICCALOJETS1",product),
  " && ALPHAMAX_BASICCALOJETS1 < 0.1 && BETA_BASICCALOJETS1 > 0.65 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && MEDIANLOG10TRACKANGLE_BASICCALOJETS1 > -1.7 && PT_BASICCALOJETS1 > 20 && SUMIPSIG_BASICCALOJETS1 > 170".replace("BASICCALOJETS1",product),
  " && ALPHAMAX_BASICCALOJETS1 < 0.1 && MEDIANIPLOG10SIG_BASICCALOJETS1 > 0.5 && MEDIANLOG10TRACKANGLE_BASICCALOJETS1 > -1.7 && PT_BASICCALOJETS1 > 20 && SUMIPSIG_BASICCALOJETS1 > 170".replace("BASICCALOJETS1",product),
  ]
  
  cutSetNames = [
  "Cut Set 1",
  "Cut Set 1b",
  "Cut Set 1c",
  "Cut Set 1d",
  "Cut Set 2",
  "Cut Set 2b"
  ]
  
  previousVar = "N/A"
  
  for idx in range(0,len(objectSelections)+3):    
    if idx == 0:
      print selectionRegionStart
      retval = makeROC(idx,selectionRegionStart,False,"N/A")
      bkgOrig = retval[3]
      sigOrig = retval[4]
    elif idx < len(objectSelections)+1:
      print selectionRegionStart + objectSelections[idx-1]
      retval = makeROC(idx,selectionRegionStart + objectSelections[idx-1],False,"N/A")
      
      print retval[3]
      print retval[4]
      print sigOrig
      print bkgOrig
      print math.sqrt(retval[3]/bkgOrig) + 1.5 + 0.2*retval[3]/bkgOrig
      
      punzi = (retval[4]/sigOrig) / (math.sqrt(retval[3]/bkgOrig) + 1.5 + 0.2*retval[3]/bkgOrig)
      
      txtFile.write(cutSetNames[idx-1] + ":\t%s\tSig Eff:\t%s\tBkg Rej:\t%s\n"%(punzi,retval[4]/sigOrig,retval[3]/bkgOrig))
    elif idx == len(objectSelections)+1:
      print selectionRegionOriginal + objSelectionOriginal
      retval = makeROC(idx,selectionRegionOriginal + objSelectionOriginal,False,"N/A")
      
      print retval[3]
      print retval[4]
      print sigOrig
      print bkgOrig
      print math.sqrt(retval[3]/bkgOrig) + 1.5 + 0.2*retval[3]/bkgOrig
      
      punzi = (retval[4]/sigOrig) / (math.sqrt(retval[3]/bkgOrig) + 1.5 + 0.2*retval[3]/bkgOrig)
      
      txtFile.write("Original:\t%s\tSig Eff:\t%s\tBkg Rej:\t%s\n"%(punzi,retval[4]/sigOrig,retval[3]/bkgOrig))
    else:
      autoCutFile = open("pdfHistos/cut_%s.txt"%(signalSample))
      lines = autoCutFile.readlines()
      selectionRegionAuto = lines[0][:-1]
      objSelectionAuto = lines[1][:-1]
      print selectionRegionAuto + objSelectionAuto
      
      retval = makeROC(idx,selectionRegionAuto + objSelectionAuto,False,"N/A")
      
      punzi = (retval[4]/sigOrig) / (math.sqrt(retval[3]/bkgOrig) + 1.5 + 0.2*retval[3]/bkgOrig)
      
      txtFile.write("Automatic:\t%s\tSig Eff:\t%s\tBkg Rej:\t%s\n"%(punzi,retval[4]/sigOrig,retval[3]/bkgOrig))
      
    previousVar = retval[0]
    
if __name__ == '__main__':main()
