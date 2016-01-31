@ECHO off
SETLOCAL enabledelayedexpansion
SET /A num=0
FOR %%i in (*.cmd) do ( 
SET /A num+=1
ECHO !num! : %%i
)
