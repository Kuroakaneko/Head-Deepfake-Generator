@echo off
call _internal\setenv.bat

if exist "macron\result.mp4" del "macron\result.mp4"
if exist "macron\result_mask.mp4" del "macron\result_mask.mp4"

rmdir "macron\data_dst\merged" /s /q 2>nul
rmdir "macron\data_dst\merged_mask" /s /q 2>nul

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" merge ^
    --input-dir "macron\data_dst" ^
    --output-dir "macron\data_dst\merged" ^
    --output-mask-dir "macron\data_dst\merged_mask" ^
    --aligned-dir "macron\data_dst\aligned" ^
    --model-dir "macron\model" ^
    --model SAEHD
    
pause