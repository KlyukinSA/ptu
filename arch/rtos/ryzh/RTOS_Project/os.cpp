/*******************************************/
/*              Управление ОС              */
/*******************************************/

#include "rtos_api.h"

// Инициализация очереди задач и очереди указателей на активные задачи
void InitializeTaskQueue()
{
  for (int i = 0; i < MAX_PRIOR; i++)
  {
    for (int j = 0; j < MAX_TASK; j++)
    {
      TaskQueue[i][j].priority = 0;
      TaskQueue[i][j].state = -1;
      TaskQueue[i][j].entry = NULL;
      TaskQueue[i][j].name = NULL;
      TaskQueue[i][j].eventwaiting = false;
      TaskQueue[i][j].semaphorewaiting = false;
      TaskQueue[i][j].Rsp.stack = NULL;
      TaskQueue[i][j].Rsp.size = 0;
      ClearMask(&TaskQueue[i][j]);
    }
  }

  for (int i = 0; i < MAX_TASK; i++)
  {
    FreeTask[i].priority = -1;
    FreeTask[i].task = -1;
    SemaphoreWaitingTask[i].priority = -1;
    SemaphoreWaitingTask[i].task = -1;
  }
}

// Инициализация очереди задач и очереди ресурсов, запуск первой задачи
int StartOS(TTask Task)
{
  int tmp = 0;
  SP = &tmp;
  RunningTask.priority = -1;
  RunningTask.task = -1;
  RestoreStack = false;

  TSemaphore Sem;
  Sem.isfree = true; Sem.sem_id = 1;
  printf("Starting OS...\n");
  InitPVS(Sem);
  InitializeTaskQueue(); // Инициализируем очереди ресурсов и задач
  ActivateTask(Task); // Запуск задачи
  return 0;
}

// Завершение работы ОС
void ShutdownOS()
{
  printf("Shutdown OS...\n");
}
