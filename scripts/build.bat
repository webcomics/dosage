:: Build script
:: Copyright (C) 2012 Bastian Kleineidam
@echo off
:: Python version
set PYDIR=C:\Python27
set PYVER=2.7
%PYDIR%\python.exe setup.py build
