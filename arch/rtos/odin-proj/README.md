1. https://github.com/odin-lang/Odin/releases/download/dev-2024-03/odin-ubuntu-amd64-dev-2024-03.zip
2. `sudo ln -s `pwd`/odin /usr/local/bin/odin`
3. `sudo apt install clang`

4. `git clone git@github.com:0riginaln0/rtos.git`
5. `cd rtos`
6. `odin build rtos`
7. `./rtos.bin`

-->
```
OS: Start
Activate task Task1
Schedule task Task1
End of Schedule Task1
Dispatch started
Task1: Start
Activate task Task2
Schedule task Task2
End of Schedule Task2
End of Activate task Task2
Task1: Working
Task1: Completed
Terminate task Task1
End of terminating task Task1
Task2: Start
Activate task Task3
Schedule task Task3
End of Schedule Task3
Dispatch started
Task3: Start
Task3: Working
Task3: Completed
Terminate task Task3
End of terminating task Task3
End of dispatch
End of Activate task Task3
Task2: Working
Task2: Completed
Terminate task Task2
End of terminating task Task2
End of dispatch
End of Activate task Task1
OS: Shutdown
```

