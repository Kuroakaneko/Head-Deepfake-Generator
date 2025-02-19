@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" merge ^
    --input-dir "putin\data_dst" ^
    --output-dir "putin\data_dst\merged" ^
    --output-mask-dir "putin\data_dst\merged_mask" ^
    --aligned-dir "putin\data_dst\aligned" ^
    --model-dir "putin\model" ^
    --model SAEHD
    
pause