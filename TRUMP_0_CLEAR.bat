@echo off
echo Press space if you want to delete content in workspace folder
pause
call _internal\setenv.bat
rmdir "trump\data_dst" /s /q 2>nul
mkdir "trump\data_dst" 2>nul
mkdir "trump\data_dst\aligned" 2>nul
echo DONE
pause