/*********************************/
/*      Управление задачами      */
/*********************************/

#include <stdlib.h>
#include "rtos_api.h"

/* Проверка наличия задачи в очереди и её состояния.
   Завершение программы произойдет в следующих случаях:
     - данная задача уже запущена,
     - неправильный приоритет или номер задачи */
void CheckTask(int prt, int tasknumber)
{
  if (prt < MAX_PRIOR)
  {
    if (tasknumber < MAX_TASK)
    {
      if (TaskQueue[prt][tasknumber].state == 1)
      {
        printf("Checking... Error: Task%i is running\n", tasknumber);
        _getch(); exit(1);
      }
    }
    else
    {
      printf("Checking... Error: Trying to activate wrong task - Task%i\n", tasknumber);
      _getch(); exit(1);
    }
    printf("Checking... Ok\n", tasknumber);
  }
  else
  {
    printf("Checking... Error: Trying to activate task with wrong priority %i\n", prt);
    _getch(); exit(1);
  }
}

// Активизация задачи
void ActivateTask(TTask tsk)
{
  printf("Activating %s\n", tsk.name);
  int TaskNumber = atoi(&tsk.name[4]) - 1;
  CheckTask(tsk.priority, TaskNumber);
  
  // Задача вносится в очередь задач
  TaskQueue[tsk.priority][TaskNumber].priority = tsk.priority;
  TaskQueue[tsk.priority][TaskNumber].name = tsk.name;
  TaskQueue[tsk.priority][TaskNumber].entry = tsk.entry;
  TaskQueue[tsk.priority][TaskNumber].eventwaiting = false;
  TaskQueue[tsk.priority][TaskNumber].semaphorewaiting = false;
  Schedule(tsk.priority, TaskNumber); // запускаем планировщик
  printf("Activation of %s completed\n", tsk.name);

  if (RunningTask.priority == -1)
    Dispatch(tsk.priority, TaskNumber); // запускаем диспетчер
}

// Завершение задачи
void TerminateTask(void)
{
  if (RunningTask.task != -1)
  {
    printf("Terminating %s\n", TaskQueue[RunningTask.priority][RunningTask.task].name);
    printf("Termination of %s completed\n", TaskQueue[RunningTask.priority][RunningTask.task].name);
    TaskQueue[RunningTask.priority][RunningTask.task].state = -1;
    RunningTask.priority = -1;
    RunningTask.task = -1;
  }

  // Изменяем состояние задачи. Запускаем следующую в очереди задачу
  if (FreeTask[0].priority != -1)
  {
    Dispatch(FreeTask[0].priority, FreeTask[0].task);
  }
}

// Запуск планировщика
void Schedule(int prt, int task)
{
  int i = 0, j;
  TRunningTask Bufo, Bufn;
  printf("Sheduling %s, priority - %i\n", TaskQueue[prt][task].name, TaskQueue[prt][task].priority);

  // Меняем состояние задачи
  TaskQueue[prt][task].state = 0;

  /* Подготавливаем место в очереди готовых задач.
     Очередь отсортирована по убыванию приоритета, и содержит только указатели на задачи в очереди TaskQueue */
  for (i = 0; i < MAX_TASK; i++)
  {
    if (FreeTask[i].priority < prt)
    {
      if (FreeTask[i].priority != -1)
      {
        j = i + 1;
        Bufo = FreeTask[i];
        while ((FreeTask[j].priority != -1) & (j < MAX_TASK))
        {
          Bufn = FreeTask[j];
          FreeTask[j] = Bufo;
          Bufo = Bufn;
        }
        FreeTask[j] = Bufo;
        break;
      }
      else break;
    }
  }
  // Вставляем задачу в очередь готовых задач
  FreeTask[i].priority = prt;
  FreeTask[i].task = task;
  printf("Scheduling of %s completed\n", TaskQueue[prt][task].name);
}

// Запуск диспетчера
void Dispatch(int prt, int task)
{
  printf("Dispatching...\n");
  // Выбираем первую задачу в очереди готовых задач на исполнение
  RunningTask.priority = FreeTask[0].priority;
  RunningTask.task = FreeTask[0].task;

  // Удаляем выбранную задачу из очереди
  FreeTask[0].priority = -1;
  FreeTask[0].task = -1;
  Sort(FreeTask);
  TaskQueue[prt][task].state = 1;

  // Запускаем задачу. Запускаем приостановленную задачу
  if (TaskQueue[prt][task].eventwaiting | TaskQueue[prt][task].semaphorewaiting)
  {
    TaskQueue[RunningTask.priority][RunningTask.task].context.ContextFlags = CONTEXT_ALL;
    TaskQueue[prt][task].eventwaiting = false;
    TaskQueue[prt][task].semaphorewaiting = false;
    RestoreStack = true;
    RtlRestoreContext(&(TaskQueue[RunningTask.priority][RunningTask.task].context), NULL);
  }
  else
  {
    TaskQueue[prt][task].entry();
  }
  if (RunningTask.task != -1)
    printf("Dispatching of Task%i completed\n", task + 1);
}
