#!/bin/bash
for i in `seq 3 9`
do
cat > KPOINTS <<!
auto
0
Gamma
$i $i $i
0.0 0.0 0.0
!

echo 'k=`$i`'
EXE=/THFS/opt/vasp/5.4.4/vasp.5.4.4/bin/vasp_std
yhrun  -n 4 -p TYUT  $EXE

E=`grep "TOTEN" OUTCAR | tail -1 | awk '{printf "%12.6f \n", $5 }'`
K=`grep "irred" OUTCAR | tail -1 | awk '{printf "%4i\n", $2 }'`
echo $i $E>> kpoints.dat
done
