/****************************************/
/*              rtos_api.h              */
/****************************************/
#pragma once

//#include <curses.h>
#include <stdio.h>
//#include <winnt.h>

#define MAX_TASK 32  // Макс. кол-во задач
#define MAX_RES 16   // Макс. кол-во ресурсов
#define MAX_PRIOR 16 // Макс. кол-во приоритетов
#define MAX_EVENT 16 // Макс. кол-во событий

typedef struct Type_Mask
{
  bool mask[MAX_EVENT]; // маска событий
} TEventMask;

typedef struct Type_stack
{
  void* stack; // стек
  int size;    // рамер стека
} _stack;

typedef struct Type_Task
{
  int priority;          // приоритет
  int state;             // состояние задачи
  void (*entry)(void);   // точка входа
  char* name;            // имя задачи
  TEventMask mask_w;     // маска ожидаемых событий
  TEventMask mask_h;     // маска произошедших событий
  bool eventwaiting;     // флаг ожидания события
  bool semaphorewaiting; // флаг ожидагия семафора
  CONTEXT context;       // контекст задачи
  _stack Rsp;            // стек вызовов
} TTask;

typedef struct Type_runningtask
{
  int priority; // приоритет
  int task;     // номер задачи в очереди
} TRunningTask;

typedef struct Type_semaphore
{
  int sem_id;  // идентификатор
  int task_id; // идентификатор задачи
  bool isfree; // состояние
} TSemaphore;

// Регистрация задачи
#define DeclareTask(TaskID, priority)\
  TASK(TaskID);\
  enum { TaskID##prior = priority };

// Регистрация ресурса
#define DeclareResource(ResID, priority)\
  enum { ResID = priority };

// Регистрация события
#define DeclareEvent(Event_ID, EventID)\
  enum { Event_ID = EventID };

#define TASK(TaskID)\
  void TaskID(void)

typedef void TTaskCall(void);

extern TTask TaskQueue[MAX_PRIOR][MAX_TASK]; // Очередь задач для POSIX планировщика, отдельная очередь на каждый приоритет

extern TRunningTask RunningTask; // Запущенная задача

extern TRunningTask FreeTask[MAX_TASK]; // Очередь свободных задач отсортированных по убыванию приоритетов

extern TRunningTask SemaphoreWaitingTask[MAX_TASK]; // Очередь задач, ожидающих освобождение семафора

extern TSemaphore Semaphore; // Семафор

extern void* SP; // Начало стека

extern bool RestoreStack; // Флаг, характеризующий необходимость восстанавления стека

extern HANDLE MainProcess; // Дескриптор процесса

void CheckTask(int prt, int tasknumber); // Проверка наличия задачи в очереди и её состояния

void ActivateTask(TTask tsk); // Изменение состояния задачи из suspebded в ready

void TerminateTask(void); // Завершение текущей задачи

void Schedule(int prt, int task); // Запуск планировщика

void Dispatch(int prt, int task); // Запуск диспетчера

void InitializeTaskQueue(); // Инициализация очереди задач

int StartOS(TTask Task); // Запуск ОС

void ShutdownOS(); // Завершение работы ОС

void InitPVS(TSemaphore semaphore); // Инициализация семафора

void P(TSemaphore semaphore); // Захват семафора

void V(TSemaphore semaphore); // Освобождение семафора

void SetEvent(TTask* Task, TEventMask Mask); // Установки для заданных задач маски собятия

void GetEvent(TTask Task, TEventMask* Mask); // Получение состояния маски для заданной задачи

void WaitEvent(TEventMask Mask); // Ожидание события

void ClearEvent(TEventMask Mask); // Очистка признаков событий по маске

void ClearMask(TTask* Task); // Очистка маски по задаче

void ClearMask(TEventMask* Mask); // Очистка заданной маски

void Sort(TRunningTask* Task); // Сортировка задач по приоритету

void InsertIntoQueue(TRunningTask* Task); // Постановка задачи в очередь согласно приоритету
