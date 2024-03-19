/*******************************************************/
/*  Управление событиями - события принадлежат задаче  */
/*******************************************************/

#include <stdlib.h>
#include "rtos_api.h"

// Установки для заданных задач маски собятия
void SetEvent(TTask* Task, TEventMask Mask)
{
  int i = 0;
  bool flag = false, comma = true;
  printf("Setting for %s ", (*Task).name);

  // Устанавливаем маску произошедших событий
  for (int i = 0; i < MAX_EVENT; i++)
  {
    if (Mask.mask[i])
    {
      if (comma) { printf("Event_%i", i + 1); comma = false; }
      else printf(", Event_%i", i + 1);
      (*Task).mask_h.mask[i] = Mask.mask[i];
    }
    if (((*Task).mask_w.mask[i]) & ((*Task).mask_h.mask[i]))
    {
      flag = true;
      (*Task).mask_h.mask[i] = false;
      (*Task).mask_w.mask[i] = false;
    }
  }
  printf("\n");
  if (flag)
  {
    int TaskNumber = atoi(&(*Task).name[4]) - 1;
    Schedule((*Task).priority, TaskNumber);
  }
  printf("Setting events for %s completed\n", (*Task).name);
}

// Получение состояния маски для заданной задачи
void GetEvent(TTask Task, TEventMask* Mask)
{
  (*Mask) = Task.mask_h;
}

// Для вызвавшей задачи устанавливается маска ожидаемых событий, задаваемая Mask
void WaitEvent(TEventMask Mask)
{
  bool flag = false, temp = false, comma = true;
  int count = 0, i = 0, addr = 0;
  SIZE_T sz;
  printf("Waiting (Task%i) ", RunningTask.task + 1);
  
  // Устанавливаем маску ожидаемых событий
  for (i = 0; i < MAX_EVENT; i++)
  {
    if (Mask.mask[i])
    {
      if (comma) { printf("Event_%i", i + 1); comma = false; }
      else printf(", Event_%i", i + 1);
      count++;
      TaskQueue[RunningTask.priority][RunningTask.task].mask_w.mask[i] = Mask.mask[i];
    }
  }
  printf("\n"); comma = true;

  // Проверка установленной маски
  for (i = 0; i < MAX_EVENT; i++)
  {
    // Если ожидаемые события уже произошли сбрасываем маску
    if ((TaskQueue[RunningTask.priority][RunningTask.task].mask_w.mask[i]) & (TaskQueue[RunningTask.priority][RunningTask.task].mask_h.mask[i]))
    {
      TaskQueue[RunningTask.priority][RunningTask.task].mask_w.mask[i] = false;
      TaskQueue[RunningTask.priority][RunningTask.task].mask_h.mask[i] = false;
      if (!flag) printf("Events which have already happened: ");
      flag = true;
      count--;
      temp = true;
      if (comma) { printf("Event_%i", i + 1); comma = false; }
      else printf(", Event_%i", i + 1);
    }
  }

  // Если все события произошли, то ничего не делаем, в противном случае задача переходит в состояние waiting и запускаем другую задачу
  if (temp) printf("\n");

  // Есть события, появление которых нужно ожидать
  // Приостанавливаем запущенную задачу и устанавливаем флаг, сигнализирующий о том, что есть события, появления которых нужно ожидать
  if (count != 0)
  {
    TaskQueue[RunningTask.priority][RunningTask.task].state = -1;
    TaskQueue[RunningTask.priority][RunningTask.task].eventwaiting = true;

    // Сохраняем контекст задачи и запускаем другую задачу
    TaskQueue[RunningTask.priority][RunningTask.task].context.ContextFlags = CONTEXT_ALL;
    RtlCaptureContext(&(TaskQueue[RunningTask.priority][RunningTask.task].context));
    if (TaskQueue[RunningTask.priority][RunningTask.task].eventwaiting)
    {
      TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size = (int)SP - (int)&addr;
      TaskQueue[RunningTask.priority][RunningTask.task].Rsp.stack = malloc(TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size);
      if (ReadProcessMemory(MainProcess, (LPVOID)(TaskQueue[RunningTask.priority][RunningTask.task].context.Rsp),
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.stack,
        TaskQueue[RunningTask.priority][RunningTask.task].Rsp.size, &sz))
      {
        printf("Reading memory... Ok %i bytes\n", sz);
      }
      else { printf("Error: ReadProcessMemory %i\n", GetLastError()); }
      
      if (FreeTask[0].priority != -1)
      {
        Dispatch(FreeTask[0].priority, FreeTask[0].task);
      }
      else
      {
        printf("Error: Deadlock in WaitEvent routine!\n");
        _getch();
        exit(1);
      }
    }
    if (RestoreStack) // Восстанавливаем стек при необходимости
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
  else
  {
    printf("All events have already happened!\n");
  }

  if (RunningTask.task != -1) printf("Waiting events (Task%i) completed\n", RunningTask.task + 1);
}

// Очистка признаков событий по маске
void ClearEvent(TEventMask Mask)
{
  TaskQueue[RunningTask.priority][RunningTask.task].mask_h = Mask;
}

// Очистка маски по задаче
void ClearMask(TTask* Task)
{
  for (int i = 0; i < MAX_EVENT; i++)
  {
    (*Task).mask_w.mask[i] = false;
    (*Task).mask_h.mask[i] = false;
  }
}

// Очистка заданной маски
void ClearMask(TEventMask* Mask)
{
  for (int i = 0; i < MAX_EVENT; i++)
  {
    (*Mask).mask[i] = false;
    (*Mask).mask[i] = false;
  }
}
