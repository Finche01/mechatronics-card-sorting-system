@echo off
REM Automated Card Sorter - Repository Setup Script (Windows)
REM Run this after cloning your new GitHub repository

echo ==========================================
echo Automated Card Sorter - Repository Setup
echo ==========================================
echo.

REM Check if we're in a git repository
if not exist ".git" (
    echo ERROR: Not in a git repository!
    echo Please run this script from your cloned repository directory.
    pause
    exit /b 1
)

echo Git repository detected
echo.

REM Extract the archive (requires tar on Windows 10+, or use 7-Zip)
echo Extracting repository files...
if exist "automated-card-sorter-repo.tar.gz" (
    tar -xzf automated-card-sorter-repo.tar.gz
    echo Files extracted successfully
) else (
    echo ERROR: automated-card-sorter-repo.tar.gz not found!
    echo Please download it from Claude and place it in this directory.
    pause
    exit /b 1
)

REM Create necessary directories
echo.
echo Creating directory structure...
mkdir software\vision\templates\ranks 2>nul
mkdir software\vision\templates\suits 2>nul
mkdir software\vision\logs 2>nul
mkdir software\node-red 2>nul
mkdir software\plc\click-program 2>nul
mkdir hardware\mechanical\nx-models 2>nul
mkdir hardware\electrical\eplan-diagrams 2>nul
mkdir tests 2>nul
mkdir docs\images 2>nul

echo Directory structure created
echo.

echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Add your actual Python vision code to software/vision/
echo 2. Add your Node-RED flows to software/node-red/
echo 3. Add your PLC programs to software/plc/
echo 4. Add your CAD files to hardware/mechanical/
echo 5. Add system photos to docs/images/
echo 6. Update the BOM Excel file in hardware/
echo.
echo Then commit and push:
echo   git add .
echo   git commit -m "Initial commit with complete project structure"
echo   git push origin main
echo.
echo Your repository is ready to go!
echo.
pause
