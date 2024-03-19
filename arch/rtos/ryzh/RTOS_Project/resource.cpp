/*********************************************/
/*  Управление ресурсами - простые семафоры  */
/*********************************************/

#include "rtos_api.h"

// Инициалищация семафоров
void InitPVS(TSemaphore semaphore)
{
  Semaphore.isfree = semaphore.isfree;
  Semaphore.sem_id = semaphore.sem_id;
  Semaphore.task_id = -1;
}

// Захват семафора
void P(TSemaphore semaphore)
{
  int addr = 0;
  SIZE_T sz;
  printf("Trying to obtain semaphore (Task%i)...", RunningTask.task + 1);
  if (!Semaphore.isfree)
  {
    printf(" semaphore is busy\n");

    // Сохраняем контекст задачи и запускаем другую задачу
    TaskQueue[RunningTask.priority][RunningTask.task].semaphorewaiting = true;
    TaskQueue[RunningTask.priority][RunningTask.task].state = -1;

    // Ставим задачу в очередь задач ожидающих семафора
    InsertIntoQueue(SemaphoreWaitingTask);
    TaskQueue[RunningTask.priority][RunningTask.task].context.ContextFlags = CONTEXT_ALL;
    RtlCaptureContext(&(TaskQueue[RunningTask.priority][RunningTask.task].context));
    
    if (TaskQueue[RunningTask.priority][RunningTask.task].semaphorewaiting)
    {
      TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size = (int)SP - (int)&addr;
      TaskQueue[RunningTask.priority][RunningTask.task].Rsp.stack = malloc(TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size);
      if (ReadProcessMemory(GetCurrentProcess(), (LPVOID)(TaskQueue[RunningTask.priority][RunningTask.task].context.Rsp),
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.stack,
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size, &sz))
      {
        printf("Reading memory... Ok %i bytes\n", sz);
      }
      else
      {
        printf("Error: ReadProcessMemory %i\n", GetLastError());
      }

      if (FreeTask[0].priority != -1)
      {
        Dispatch(FreeTask[0].priority, FreeTask[0].task);
      }
      else
      {
        printf("Error: Deadlock in primitive P!\n");
        _getch();
        exit(1);
      }
    }

    if (RestoreStack)
    {
      RestoreStack = false;
      CONTEXT Ctx = TaskQueue[RunningTask.priority][RunningTask.task].context;
      if (WriteProcessMemory(GetCurrentProcess(), (void*)(Ctx.Rsp),
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.stack,
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size, &sz))
      {
        printf("Writing memory... Ok %i bytes\n", sz);
      }
      else
      {
        printf("Error: WriteProcessMemory %i\n", GetLastError());
      }
    }
  }
  printf("Semaphore is obtained (Task%i)\n", RunningTask.task + 1);
  Semaphore.isfree = false;
  Semaphore.task_id = RunningTask.task;
}

// Освобождение семафора
void V(TSemaphore semaphore)
{
  int prt, tsk;
  if (RunningTask.task != -1)
  {
    if (RunningTask.task == Semaphore.task_id)
    {
      printf("Retrieving semaphore (Task%i)...\n", RunningTask.task + 1);
      prt = SemaphoreWaitingTask[0].priority;
      tsk = SemaphoreWaitingTask[0].task;
      SemaphoreWaitingTask[0].priority = -1;
      SemaphoreWaitingTask[0].task = -1;
      Sort(SemaphoreWaitingTask);
      Semaphore.isfree = true;
      Semaphore.task_id = -1;

      if ((prt != -1) & (tsk != -1))
        Schedule(prt, tsk);
    }
    else
    {
      printf("Error: Can not retrieve semaphore, it belongs to another task!");
      _getch(); exit(1);
    }
  }
}
