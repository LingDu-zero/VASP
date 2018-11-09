#!/bin/bash

#please use the following command to submit job
#yhbatch -p TYUT ./job.sh

#partition -p TYUT
#process -n 
#jobname -J

EXE=/THFS/opt/vasp/5.4.4/vasp.5.4.4/bin/vasp_std
name=test

yhrun -n 4 -p TYUT $EXE
