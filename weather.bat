@echo off

set /p city="Enter city name: "

curl wttr.in/%city%

pause