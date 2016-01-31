@echo off
:confirm
SET /P "Continue [y/n]>" %confirm%
FINDSTR /I "^(y|n|yes|no)$" /C:%confirm% || GOTO: confirm