@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "elon\data_dst\merged" ^
    --output-file "elon\result.mp4" ^
    --reference-file "elon\data_dst.*" ^
    --bitrate 16 ^
    --include-audio

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" videoed video-from-sequence ^
    --input-dir "elon\data_dst\merged_mask" ^
    --output-file "elon\result_mask.mp4" ^
    --reference-file "elon\data_dst.*" ^
    --lossless

pause