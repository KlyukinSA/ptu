/****************************************/
/*           rtos_api.h                 */
/****************************************/

#define DeclareTask(TaskID,priority)\
	TASK(TaskID);					\
enum {TaskID##prior=priority}

#define DeclareResource(ResID,priority)\
enum {ResID=priority}

#define TASK(TaskID) void TaskID(void)

typedef void TTaskCall(void);

void ActivateTask(TTaskCall entry,int priority,char* name);
void TerminateTask(void);

int StartOS(TTaskCall entry,int priority,char* name);
void ShutdownOS();

void GetResource(int priority, char* name);
void ReleaseResource(int priority, char* name);