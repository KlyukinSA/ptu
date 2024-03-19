/******************************/
/*          os.c              */
/******************************/

#include <stdio.h>
#include "sys.h"
#include "rtos_api.h"

int StartOS(TTaskCall entry,int priority,char* name)
{
	int i;

	RunningTask=-1;

	FreeTask=0;

	FreeResource=0;

	printf("StartOS!\n");

	for(i=0;i<MAX_TASK;i++)
	{
		TaskQueue[i].ref=i+1;
	}

	TaskQueue[MAX_TASK-1].ref=-1;

	for(i=0;i<MAX_RES;i++)
	{
		ResourceQueue[i].priority=i+1;
		ResourceQueue[i].task=-1;
	}

	ResourceQueue[MAX_RES-1].priority=-1;


	ActivateTask(entry,priority,name);

	return 0;
}

void ShutdownOS()
{
	printf("ShutdownOS!\n");
}