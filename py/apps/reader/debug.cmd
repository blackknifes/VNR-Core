:: run.cmd
:: 11/1/2012 jichi
setlocal
set PYTHON=..\..\..\..\Python\python.exe
set FLAGS=-B
%PYTHON% %FLAGS% debug.py  --debug %*
