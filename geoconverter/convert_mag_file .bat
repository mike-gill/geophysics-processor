cls
@ECHO OFF 
REM ***********************************************
REM * Run this Windows batch file to convert a raw
REM * Magnetometer data file.  It runs Python code
REM * which will open up a file dialogue to choose
REM * the file.
REM *
REM * Author:		Mike Gill
REM * Copyright:	Mike Gill
REM ***********************************************

C:\Python26\python.exe src\geoconverter\GeophysConverter.py M
pause