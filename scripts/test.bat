:: Run test suite
:: Copyright (C) 2010-2012 Bastian Kleineidam
@echo off
set PYDIR=C:\Python27
%PYDIR%\python.exe -m pytest tests
pause
