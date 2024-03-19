/*********************************/
/*            test.cpp           */
/*********************************/

#include <stdlib.h>
#include "rtos_api.h"

DeclareTask(Task1, 0);
DeclareTask(Task2, 1);
DeclareTask(Task3, 2);
DeclareTask(Task4, 3);
DeclareTask(Task5, 4);
DeclareTask(Task6, 5);
DeclareTask(Task7, 6);
DeclareTask(Task8, 7);
DeclareTask(Task9, 8);
DeclareTask(Task10, 9);

DeclareEvent(Event1, 0);
DeclareEvent(Event2, 1);
DeclareEvent(Event3, 2);
DeclareEvent(Event4, 3);
DeclareEvent(Event5, 4);
DeclareEvent(Event6, 5);
DeclareEvent(Event7, 6);
DeclareEvent(Event8, 7);
DeclareEvent(Event9, 8);
DeclareEvent(Event10, 9);

TASK(Task1)
{
  printf("Starting Task1...\n");
  TTask task2, task3;
  TEventMask msk;

  task2.priority = Task2prior;
  task2.state = -1;
  task2.name = const_cast<char *>("Task2");
  task2.entry = Task2;
  task2.eventwaiting = false;
  task2.semaphorewaiting = false;

  ClearMask(&task2);
  ClearMask(&msk);
  msk.mask[Event1] = true;
  msk.mask[Event2] = true;

  task3.priority = Task3prior;
  task3.state = -1;
  task3.name = const_cast<char*>("Task3");;
  task3.entry = Task3;
  task3.eventwaiting = false;
  task3.semaphorewaiting = false;

  ClearMask(&task3);
  ActivateTask(task2);
  ActivateTask(task3);
  P(Semaphore);
  WaitEvent(msk);
  V(Semaphore);
  if (RunningTask.task != -1)
    printf("Executing Task1...\n");
  TerminateTask();
}

TASK(Task2)
{
  printf("Starting Task2...\n");
  TEventMask msk;
  ClearMask(&msk);
  msk.mask[0] = true; msk.mask[1] = true;
  SetEvent(&(TaskQueue[0][0]), msk);
  printf("Executing Task2...\n");
  TerminateTask();
}

TASK(Task3)
{
  printf("Starting Task3...\n");
  TEventMask msk;
  ClearMask(&msk);
  msk.mask[0] = true; msk.mask[1] = true;
  P(Semaphore);
  printf("Executing Task3...\n");
  V(Semaphore);
  TerminateTask();
}

TASK(Task4)
{
  printf("Starting Task4...\n");
  TTask task5, task6;
  TEventMask msk;

  task5.priority = Task5prior;
  task5.state = -1;
  task5.name = const_cast<char*>("Task5");;
  task5.entry = Task5;
  task5.eventwaiting = false;
  task5.semaphorewaiting = false;

  ClearMask(&task5);
  ClearMask(&msk);
  msk.mask[Event3] = true;
  msk.mask[Event4] = true;
  msk.mask[Event5] = true;

  task6.priority = Task6prior;
  task6.state = -1;
  task6.name = const_cast<char*>("Task6");;
  task6.entry = Task6;
  task6.eventwaiting = false;
  task6.semaphorewaiting = false;

  ClearMask(&task6);
  ActivateTask(task5);
  ActivateTask(task6);
  WaitEvent(msk);
  if (RunningTask.task != -1)
    printf("Executing Task4...\n");
  TerminateTask();
}

TASK(Task5)
{
  printf("Starting Task5...\n");
  TEventMask msk;
  ClearMask(&msk);
  msk.mask[Event5] = true;
  SetEvent(&(TaskQueue[3][3]), msk); // Task4 3
  ClearMask(&msk);
  msk.mask[Event10] = true;
  SetEvent(&(TaskQueue[6][6]), msk); // Task7 6
  printf("Executing Task5...\n");
  TerminateTask();
}

TASK(Task6)
{
  printf("Starting Task6...\n");
  TTask task7;
  task7.priority = Task7prior;
  task7.state = -1;
  task7.name = const_cast<char*>("Task7");
  task7.entry = Task7;
  task7.eventwaiting = false;
  task7.semaphorewaiting = false;

  ClearMask(&task7);
  P(Semaphore);
  ActivateTask(task7);
  V(Semaphore);
  printf("Executing Task6...\n");
  TerminateTask();
}

TASK(Task7)
{
  printf("Starting Task7...\n");
  TEventMask msk;
  ClearMask(&msk);
  msk.mask[Event10] = true;
  WaitEvent(msk);
  printf("Executing Task7...\n");
  TerminateTask();
}

void Test(int testNumber)
{
  TTask InitialTask;
  InitialTask.state = -1;
  InitialTask.eventwaiting = false;
  InitialTask.semaphorewaiting = false;
  ClearMask(&InitialTask);

  switch (testNumber)
  {
    case(0):
    {
      InitialTask.priority = Task1prior;
      InitialTask.name = const_cast<char*>("Task1");;
      InitialTask.entry = Task1;
      break;
    }
    case(1):
    {
      InitialTask.priority = Task4prior;
      InitialTask.name = const_cast<char*>("Task4");;
      InitialTask.entry = Task4;
      break;
    }
  }
  StartOS(InitialTask);
  ShutdownOS();
}

int main(void)
{
  HANDLE Temporary = GetCurrentProcess();
  if (DuplicateHandle(GetCurrentProcess(), Temporary, GetCurrentProcess(), &MainProcess, 0, FALSE, DUPLICATE_SAME_ACCESS))
  {
    printf("DupliicateHandle... Ok\n");
  }
  printf("******************************************\n");
  Test(0);
  _getch();
  return 0;
}
