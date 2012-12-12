:: Create Windows distribution file
:: Copyright (C) 2010-2012 Bastian Kleineidam
@echo off
set PYDIR=c:\python27
rd /s /q build > nul 2>&1
call %~dp0\build.bat
rd /s /q dist > nul 2>&1
%PYDIR%\python.exe setup.py py2exe
pause
