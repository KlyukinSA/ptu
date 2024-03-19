/****************************************/
/*        global.c                      */
/****************************************/

#include "sys.h"

TTask TaskQueue[MAX_TASK];

TResource ResourceQueue[MAX_RES];

int RunningTask;

int FreeTask;

int FreeResource;
