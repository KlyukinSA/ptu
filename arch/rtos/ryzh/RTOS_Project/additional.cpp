/**********************************/
/*         additional.cpp         */
/**********************************/

#include "rtos_api.h"

// —ортировка задач по приоритету
void Sort(TRunningTask* Task)
{
  TRunningTask Buf;
  for (int i = 0; i < MAX_TASK - 1; i++)
  {
    if (Task[i + 1].priority == -1) break;
    Buf = Task[i];
    Task[i] = Task[i + 1];
    Task[i + 1] = Buf;
  }
}

// ѕостановка задачи в очередь согласно приоритету
void InsertIntoQueue(TRunningTask* Task)
{
  int i = 0, j;
  TRunningTask Bufo, Bufn;
  for (i = 0; i < MAX_TASK; i++)
  {
    if (Task[i].priority < RunningTask.priority)
    {
      if (Task[i].priority != -1)
      {
        j = i + 1;
        Bufo = Task[i];
        while ((Task[j].priority != -1) & (j < MAX_TASK))
        {
          Bufn = Task[j];
          Task[j] = Bufo;
          Bufo = Bufn;
        }
        Task[j] = Bufo;
        break;
      }
      else break;
    }
  }
  Task[i] = RunningTask;
}
