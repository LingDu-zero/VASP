#!/bin/bash
for i in `seq 300 50 700`
do
cat > INCAR <<!
SYSTEM = Si

ISTART = 0
ICHARG = 2

ISMEAR = 0
SIGMA = 0.05

ENCUT = $i

LWAVE = .FALSE.
LCHARGE = .FALSE.
!

echo "ENCUT=$i eV"
EXE=/THFS/opt/vasp/5.4.4/vasp.5.4.4/bin/vasp_std
yhrun  -n 4 -p TYUT  $EXE

E=`grep "TOTEN" OUTCAR | tail -1 | awk '{printf "%12.6f \n", $5 }'`
echo $i $E>> encut.dat
done
