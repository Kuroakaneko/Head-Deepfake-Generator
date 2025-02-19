@echo off
call _internal\setenv.bat

mkdir "trump\data_dst" 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed extract-video ^
    --input-file "trump\data_dst.*" ^
    --output-dir "trump\data_dst" ^
    --fps 0 ^
    --output-ext "png"

pause