/*********************************/
/*      ���������� ��������      */
/*********************************/

#include <stdlib.h>
#include "rtos_api.h"

/* �������� ������� ������ � ������� � � ���������.
   ���������� ��������� ���������� � ��������� �������:
     - ������ ������ ��� ��������,
     - ������������ ��������� ��� ����� ������ */
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

// ����������� ������
void ActivateTask(TTask tsk)
{
  printf("Activating %s\n", tsk.name);
  int TaskNumber = atoi(&tsk.name[4]) - 1;
  CheckTask(tsk.priority, TaskNumber);
  
  // ������ �������� � ������� �����
  TaskQueue[tsk.priority][TaskNumber].priority = tsk.priority;
  TaskQueue[tsk.priority][TaskNumber].name = tsk.name;
  TaskQueue[tsk.priority][TaskNumber].entry = tsk.entry;
  TaskQueue[tsk.priority][TaskNumber].eventwaiting = false;
  TaskQueue[tsk.priority][TaskNumber].semaphorewaiting = false;
  Schedule(tsk.priority, TaskNumber); // ��������� �����������
  printf("Activation of %s completed\n", tsk.name);

  if (RunningTask.priority == -1)
    Dispatch(tsk.priority, TaskNumber); // ��������� ���������
}

// ���������� ������
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

  // �������� ��������� ������. ��������� ��������� � ������� ������
  if (FreeTask[0].priority != -1)
  {
    Dispatch(FreeTask[0].priority, FreeTask[0].task);
  }
}

// ������ ������������
void Schedule(int prt, int task)
{
  int i = 0, j;
  TRunningTask Bufo, Bufn;
  printf("Sheduling %s, priority - %i\n", TaskQueue[prt][task].name, TaskQueue[prt][task].priority);

  // ������ ��������� ������
  TaskQueue[prt][task].state = 0;

  /* �������������� ����� � ������� ������� �����.
     ������� ������������� �� �������� ����������, � �������� ������ ��������� �� ������ � ������� TaskQueue */
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
  // ��������� ������ � ������� ������� �����
  FreeTask[i].priority = prt;
  FreeTask[i].task = task;
  printf("Scheduling of %s completed\n", TaskQueue[prt][task].name);
}

// ������ ����������
void Dispatch(int prt, int task)
{
  printf("Dispatching...\n");
  // �������� ������ ������ � ������� ������� ����� �� ����������
  RunningTask.priority = FreeTask[0].priority;
  RunningTask.task = FreeTask[0].task;

  // ������� ��������� ������ �� �������
  FreeTask[0].priority = -1;
  FreeTask[0].task = -1;
  Sort(FreeTask);
  TaskQueue[prt][task].state = 1;

  // ��������� ������. ��������� ���������������� ������
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
