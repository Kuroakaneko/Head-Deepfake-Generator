@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" merge ^
    --input-dir "elon\data_dst" ^
    --output-dir "elon\data_dst\merged" ^
    --output-mask-dir "elon\data_dst\merged_mask" ^
    --aligned-dir "elon\data_dst\aligned" ^
    --model-dir "elon\model" ^
    --model SAEHD
    
pause