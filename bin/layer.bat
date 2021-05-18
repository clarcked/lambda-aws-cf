@echo off
set LAYER_PATH=%cd%\layers\spv\python
@REM **** OJO nunca apuntes el root path de tu maquina ****
set SOURCE_PATH=%cd%\spv

del /S /F /Q %LAYER_PATH%\spv && Xcopy /E /I /Y /Q %SOURCE_PATH% %LAYER_PATH%