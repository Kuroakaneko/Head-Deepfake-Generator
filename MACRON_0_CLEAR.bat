@echo off
echo Press space if you want to delete content in workspace folder
pause
call _internal\setenv.bat
mkdir "macron" 2>nul
rmdir "macron\data_dst" /s /q 2>nul
mkdir "macron\data_dst" 2>nul
mkdir "macron\data_dst\aligned" 2>nul
echo DONE
pause