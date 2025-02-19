@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" extract ^
    --input-dir "putin\data_dst" ^
    --output-dir "putin\data_dst\aligned" ^
    --detector s3fd ^
    --max-faces-from-image 3 ^
    --output-debug ^
    --face-type "head" ^
    --image-size 512 ^
    --jpeg-quality 90 ^
    --force-gpu-idxs 0

pause