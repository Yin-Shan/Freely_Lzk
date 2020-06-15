@echo off 
cd ..
set project_path="%cd%"
python %project_path%\script\sync.py
pause