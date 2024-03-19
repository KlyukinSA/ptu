/****************************************/
/*               sys.h                   /          
/****************************************/

#include "defs.h"

#define INSERT_TO_TAIL 1
#define INSERT_TO_HEAD 0

typedef struct Type_Task
{
	int ref;
	int priority;
	int ceiling_priority;
	void (*entry)(void);
	char* name;

} TTask;

typedef struct Type_resource
{
	int task;
	int priority;
	char* name;

} TResource;

extern TTask TaskQueue[MAX_TASK];

extern TResource ResourceQueue[MAX_RES];

extern int RunningTask;

extern int FreeTask;

extern int FreeResource;

void Schedule(int task,int mode);

void Dispatch(int task);

