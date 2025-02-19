@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "macron\data_dst\merged" ^
    --output-file "macron\result.mp4" ^
    --reference-file "macron\data_dst.*" ^
    --bitrate 16 ^
    --include-audio

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "macron\data_dst\merged_mask" ^
    --output-file "macron\result_mask.mp4" ^
    --reference-file "macron\data_dst.*" ^
    --lossless

pause