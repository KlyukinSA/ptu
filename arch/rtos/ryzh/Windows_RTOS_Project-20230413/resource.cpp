/*************************************/
/*             resource.c            */
/*************************************/

#include "sys.h"
#include "rtos_api.h"
#include <stdio.h>

void GetResource(int priority,char* name)
{
	int free_occupy;

	printf("GetResource %s\n",name);

	free_occupy=FreeResource;

	FreeResource=ResourceQueue[FreeResource].priority;

	ResourceQueue[free_occupy].priority=priority;
	ResourceQueue[free_occupy].task=RunningTask;
	ResourceQueue[free_occupy].name=name;

	if(TaskQueue[RunningTask].ceiling_priority < priority)
	{
		TaskQueue[RunningTask].ceiling_priority=priority;
	}

}

void ReleaseResource(int priority,char* name)
{
	int i,ResourceIndex;

	printf("ReleaseResource %s\n",name);

	if(TaskQueue[RunningTask].ceiling_priority == priority)
	{
		int res_priority, task_priority;
		int our_task;

		our_task=RunningTask;
		task_priority=TaskQueue[RunningTask].priority;

		for(i=0;i<MAX_RES;i++)
		{
			if(ResourceQueue[i].task!=RunningTask) continue;

			res_priority=ResourceQueue[i].priority;

			if(res_priority == priority && name == ResourceQueue[i].name)
				ResourceIndex=i;
			else
				if(res_priority>task_priority) task_priority=res_priority;
		}

		TaskQueue[RunningTask].ceiling_priority=task_priority;

		RunningTask=TaskQueue[RunningTask].ref;

		Schedule(our_task,INSERT_TO_HEAD);

		ResourceQueue[ResourceIndex].priority=FreeResource;
		ResourceQueue[ResourceIndex].task=-1;
		FreeResource=ResourceIndex;
		
		if(our_task!=RunningTask)
		{
			Dispatch(our_task);
		}

	}
	else
	{
		ResourceIndex=0;

		while(ResourceQueue[ResourceIndex].task != RunningTask ||
				ResourceQueue[ResourceIndex].priority != priority ||
				ResourceQueue[ResourceIndex].name != name)
		{
			ResourceIndex++;
		}

		ResourceQueue[ResourceIndex].priority=FreeResource;
		ResourceQueue[ResourceIndex].task=-1;
		FreeResource=ResourceIndex;
		
	}
}