@echo off
call _internal\setenv.bat

mkdir "macron\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "macron\data_dst.*" ^
    --output-dir "macron\data_dst" ^
    --fps 0 ^
    --output-ext "png"
pause