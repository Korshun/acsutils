:: Build ACSUtils and compile it with all supported compilers
:: Example .bat file to call this from:


::set ACC_DIR=C:\path\to\acc\
::set BCC_DIR=C:\path\to\bcc\
::set GDCC_DIR=C:\path\to\gdcc\
::
:: call compile.bat


del acs\*.o

rmdir dist /S /Q
mkdir dist

copy misc\cvarinfo.acsutils dist\
copy misc\decorate.acsutils dist\

py tools\preprocess.py
@if ERRORLEVEL 1 (
	echo PREPROCESS.PY FAILED
	PAUSE
	EXIT
)

py tools\changeflaggen.py
@if ERRORLEVEL 1 (
	echo CHANGEFLAGGEN FAILED
	PAUSE
	EXIT
)

%ACC_DIR%\acc.exe -i dist\ misc\empty_project.acs acs\acc.o
@if ERRORLEVEL 1 (
	echo ACC FAILED
	PAUSE
	EXIT
)

%BCC_DIR%\bcc.exe -i %ACC_DIR% -i dist\ -acc-stats misc\empty_project.acs acs\bcc.o
@if ERRORLEVEL 1 (
	echo BCC FAILED
	PAUSE
	EXIT
)

%GDCC_DIR%\gdcc-acc.exe -i dist\ misc\empty_project.acs acs\gdcc.o --no-warn-forward-reference
@if ERRORLEVEL 1 (
	echo GDCC FAILED
	PAUSE
	EXIT
)

%BCC_DIR%\\bcc.exe -i dist\ -acc-stats misc\empty_project.bcs acs\bcsutils.o
@if ERRORLEVEL 1 (
	echo BCC BCSUTILS FAILED
	PAUSE
	EXIT
)


@echo SUCCESS

@PAUSE
