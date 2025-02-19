@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "putin\data_dst\merged" ^
    --output-file "putin\result.mp4" ^
    --reference-file "putin\data_dst.*" ^
    --bitrate 16 ^
    --include-audio

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "putin\data_dst\merged_mask" ^
    --output-file "putin\result_mask.mp4" ^
    --reference-file "putin\data_dst.*" ^
    --lossless

pause