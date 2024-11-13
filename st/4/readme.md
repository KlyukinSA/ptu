polynoms.doc
->
data.txt
->
data2matlab
->
auto_crclabmod.m
->
result.csv

перед запуском auto_crclabmod.m надо включить ускорение симуляции в crclabmod2.slx. rapid acceleration у меня не получилось так как ему не нравится мой компилятор: 

### Building the rapid accelerator target for model: crclabmod2
"C:\MinGW\bin/gcc" -c -fwrapv -m64 -O0 -mcmodel=medium -msse2 -DCLASSIC_INTERFACE=1 -DALLOCATIONFCN=0 -DONESTEPFCN=0 -DTERMFCN=1 -DMULTI_INSTANCE_CODE=0 -DINTEGER_CODE=0 -DEXT_MODE -DIS_RAPID_ACCEL -DTGTCONN -DIS_SIM_TARGET -DNRT -DRSIM_PARAMETER_LOADING -DRSIM_WITH_SL_SOLVER -DENABLE_SLEXEC_SSBRIDGE=1 -DMODEL_HAS_DYNAMICALLY_LOADED_SFCNS=0 -DON_TARGET_WAIT_FOR_START=0 -DTID01EQ=0 -DMODEL=crclabmod2 -DNUMST=1 -DNCSTATES=0 -DHAVESTDIO  @crclabmod2_comp.rsp -o "crclabmod2.obj" "C:/Users/user/Documents/MATLAB/crclab/slprj/raccel/crclabmod2/crclabmod2.c"
C:/Users/user/Documents/MATLAB/crclab/slprj/raccel/crclabmod2/crclabmod2.c:1:0: error: code model 'medium' not supported in the 32 bit mode
 #include "crclabmod2.h"

далее надо выбрать blocksToStop и errorsToStop. 1000000 и 100 это совсем мало.
