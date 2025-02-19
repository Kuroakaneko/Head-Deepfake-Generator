@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "trump\data_dst\merged" ^
    --output-file "trump\result.mp4" ^
    --reference-file "trump\data_dst.*" ^
    --bitrate 16 ^
    --include-audio

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "trump\data_dst\merged_mask" ^
    --output-file "trump\result_mask.mp4" ^
    --reference-file "trump\data_dst.*" ^
    --lossless

pause