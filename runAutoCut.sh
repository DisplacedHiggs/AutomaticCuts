#!/bin/bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export COIN_FULL_INDIRECT_RENDERING=1
echo $VO_CMS_SW_DIR
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /users/h2/sritata/CMS_ENVIRONMENTS/CMSSW_8_0_7_patch1/src
export SCRAM_ARCH=slc6_amd64_gcc530
eval `scramv1 runtime -sh`
cd /cms/data24/sritata
python makeROCPlots_objectVar.py $1

