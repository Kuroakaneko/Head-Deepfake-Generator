@echo off
call _internal\setenv.bat

mkdir "putin\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "putin\data_dst.*" ^
    --output-dir "putin\data_dst" ^
    --fps 0 ^
    --output-ext "png"

pause