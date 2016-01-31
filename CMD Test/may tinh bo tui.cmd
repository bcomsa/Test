@echo off
@title:May tinh bo tui
setlocal EnableDelayedExpansion
:calc
cls
echo.
echo  May tinh bo tui
echo.
echo  + Cong
echo  - Tru
echo  * Nhan
echo  / Chia
echo.
set /p Pheptinh=Nhap phep tinh vao day: 
set /a ketqua=%Pheptinh%
echo.
echo.
echo Ket qua: %Pheptinh%=!ketqua!
pause>nul
goto calc