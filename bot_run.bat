@echo off

call %~dp0telegram_bot\venv\Scripts\activate
cd %~dp0telegam_bot

set TOKEN=5636728056:AAEujHHf2xu0ITfqB1zxYgpktUAWHCw2QKw

python telegram_bot.py

pause