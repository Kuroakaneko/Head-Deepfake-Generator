@echo off
call _internal\setenv.bat

mkdir "elon\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "elon\data_dst.*" ^
    --output-dir "elon\data_dst" ^
    --fps 0 ^
    --output-ext "png"

pause