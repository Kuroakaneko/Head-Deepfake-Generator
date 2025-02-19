@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" merge ^
    --input-dir "trump\data_dst" ^
    --output-dir "trump\data_dst\merged" ^
    --output-mask-dir "trump\data_dst\merged_mask" ^
    --aligned-dir "trump\data_dst\aligned" ^
    --model-dir "trump\model" ^
    --model SAEHD

pause