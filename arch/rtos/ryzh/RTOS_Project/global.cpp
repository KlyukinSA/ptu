/****************************************************/
/*          Описание глобальных переменных          */
/****************************************************/

#include "rtos_api.h"

TTask TaskQueue[MAX_PRIOR][MAX_TASK];

TRunningTask RunningTask;

TRunningTask FreeTask[MAX_TASK];

TRunningTask SemaphoreWaitingTask[MAX_TASK];

TSemaphore Semaphore;

void* SP;

bool RestoreStack;

HANDLE MainProcess;
