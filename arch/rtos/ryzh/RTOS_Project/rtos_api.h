/****************************************/
/*              rtos_api.h              */
/****************************************/
#pragma once

//#include <curses.h>
#include <stdio.h>
//#include <winnt.h>

#define MAX_TASK 32  // ����. ���-�� �����
#define MAX_RES 16   // ����. ���-�� ��������
#define MAX_PRIOR 16 // ����. ���-�� �����������
#define MAX_EVENT 16 // ����. ���-�� �������

typedef struct Type_Mask
{
  bool mask[MAX_EVENT]; // ����� �������
} TEventMask;

typedef struct Type_stack
{
  void* stack; // ����
  int size;    // ����� �����
} _stack;

typedef struct Type_Task
{
  int priority;          // ���������
  int state;             // ��������� ������
  void (*entry)(void);   // ����� �����
  char* name;            // ��� ������
  TEventMask mask_w;     // ����� ��������� �������
  TEventMask mask_h;     // ����� ������������ �������
  bool eventwaiting;     // ���� �������� �������
  bool semaphorewaiting; // ���� �������� ��������
  CONTEXT context;       // �������� ������
  _stack Rsp;            // ���� �������
} TTask;

typedef struct Type_runningtask
{
  int priority; // ���������
  int task;     // ����� ������ � �������
} TRunningTask;

typedef struct Type_semaphore
{
  int sem_id;  // �������������
  int task_id; // ������������� ������
  bool isfree; // ���������
} TSemaphore;

// ����������� ������
#define DeclareTask(TaskID, priority)\
  TASK(TaskID);\
  enum { TaskID##prior = priority };

// ����������� �������
#define DeclareResource(ResID, priority)\
  enum { ResID = priority };

// ����������� �������
#define DeclareEvent(Event_ID, EventID)\
  enum { Event_ID = EventID };

#define TASK(TaskID)\
  void TaskID(void)

typedef void TTaskCall(void);

extern TTask TaskQueue[MAX_PRIOR][MAX_TASK]; // ������� ����� ��� POSIX ������������, ��������� ������� �� ������ ���������

extern TRunningTask RunningTask; // ���������� ������

extern TRunningTask FreeTask[MAX_TASK]; // ������� ��������� ����� ��������������� �� �������� �����������

extern TRunningTask SemaphoreWaitingTask[MAX_TASK]; // ������� �����, ��������� ������������ ��������

extern TSemaphore Semaphore; // �������

extern void* SP; // ������ �����

extern bool RestoreStack; // ����, ��������������� ������������� �������������� �����

extern HANDLE MainProcess; // ���������� ��������

void CheckTask(int prt, int tasknumber); // �������� ������� ������ � ������� � � ���������

void ActivateTask(TTask tsk); // ��������� ��������� ������ �� suspebded � ready

void TerminateTask(void); // ���������� ������� ������

void Schedule(int prt, int task); // ������ ������������

void Dispatch(int prt, int task); // ������ ����������

void InitializeTaskQueue(); // ������������� ������� �����

int StartOS(TTask Task); // ������ ��

void ShutdownOS(); // ���������� ������ ��

void InitPVS(TSemaphore semaphore); // ������������� ��������

void P(TSemaphore semaphore); // ������ ��������

void V(TSemaphore semaphore); // ������������ ��������

void SetEvent(TTask* Task, TEventMask Mask); // ��������� ��� �������� ����� ����� �������

void GetEvent(TTask Task, TEventMask* Mask); // ��������� ��������� ����� ��� �������� ������

void WaitEvent(TEventMask Mask); // �������� �������

void ClearEvent(TEventMask Mask); // ������� ��������� ������� �� �����

void ClearMask(TTask* Task); // ������� ����� �� ������

void ClearMask(TEventMask* Mask); // ������� �������� �����

void Sort(TRunningTask* Task); // ���������� ����� �� ����������

void InsertIntoQueue(TRunningTask* Task); // ���������� ������ � ������� �������� ����������
