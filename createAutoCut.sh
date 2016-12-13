#!/bin/bash

MAINDIR=`pwd`
SCRIPTDIR=`pwd`/scripts
LOGDIR=$MAINDIR/logs
CMSDIR=$CMSSW_BASE/src


condorFile=$SCRIPTDIR/submitAutoCut.condor

if [ -e $condorFile ]
then
    rm -rf $condorFile
fi
touch $condorFile

runScript=$MAINDIR/runAutoCut.sh
if [ -e $runScript ]
then
    rm -rf $runScript
fi
touch $runScript
chmod a+x $runScript

echo "universe = vanilla" >> $condorFile
echo '+AccountingGroup = "group_rutgers.'$USER'"' >> $condorFile
echo 'Requirements = (Arch == "X86_64")' >> $condorFile
echo "Executable = $runScript" >> $condorFile
echo "should_transfer_files = NO" >> $condorFile
echo "Notification=never" >> $condorFile
echo "" >> $condorFile
echo "" >> $condorFile


echo "#!/bin/bash" >> $runScript
echo "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch" >> $runScript
echo "export COIN_FULL_INDIRECT_RENDERING=1" >> $runScript
echo 'echo $VO_CMS_SW_DIR' >> $runScript
echo 'source $VO_CMS_SW_DIR/cmsset_default.sh' >> $runScript
#echo "cd ~/Software" >> $runScript
#echo "source setup700.sh" >> $runScript
echo "cd $CMSDIR" >> $runScript
echo "export SCRAM_ARCH=$SCRAM_ARCH" >> $runScript
echo 'eval `scramv1 runtime -sh`' >> $runScript
#echo "cd $SCRIPTDIR/Datacards/coNLSP" >> $runScript
echo "cd $MAINDIR" >> $runScript
echo 'python makeROCPlots_objectVar.py $1' >> $runScript
echo "" >> $runScript

#tmplist=tmp.tmp
#ls -l submitEfficiency_WH_HToSS*.condor | grep condor > $tmplist
#ls -l submitEff*WH_HToSSTo4Tau*.condor | grep condor > $tmplist

filelist=signalfiles.list

while read line
do
  #echo $line
  base=`echo $line | awk '{split($1,array,"allHistos_"); split(array[2],array2,".root"); print array2[1]}'`
  echo $base
  infile=`echo $line | awk '{n=split($1,array,"/");print array[n]}'`
  echo $infile
  echo
  echo "output = $LOGDIR/\$(Cluster)_autoCut_${base}.out" >> $condorFile
  echo "error = $LOGDIR/\$(Cluster)_autoCut_${base}.err" >> $condorFile
  echo "log = $LOGDIR/\$(Cluster)_autoCut_${base}.log" >> $condorFile
  echo "arguments = $infile" >> $condorFile
  echo "queue" >> $condorFile
  echo "" >> $condorFile
done < $filelist