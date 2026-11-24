#!/bin/sh
# Собирает самодостаточную страницу (three.js встроен): index.html для GitHub Pages
# и офлайн-копию на рабочий стол Мака.
set -e
cd "$(dirname "$0")/.."
python3 -I tools/build_offline.py studio-room.html vendor studio-room-offline.html
cp studio-room-offline.html index.html
if [ -d "$HOME/хранилище/Desktop" ]; then cp studio-room-offline.html "$HOME/хранилище/Desktop/"; echo "скопировано на Мак: ~/Desktop/studio-room-offline.html"; fi
