@echo off
echo Press space if you want to delete content in workspace folder
pause
call _internal\setenv.bat
rmdir "elon\data_dst" /s /q 2>nul
mkdir "elon\data_dst" 2>nul
mkdir "elon\data_dst\aligned" 2>nul
echo DONE
pause