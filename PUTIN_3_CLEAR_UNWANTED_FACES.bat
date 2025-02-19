@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "face_deleter_by_index.py" "putin"

pause