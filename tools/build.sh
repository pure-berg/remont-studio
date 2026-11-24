#!/bin/sh
# Собирает офлайн-версию (three.js встроен) и кладёт копию на рабочий стол Мака.
set -e
cd "$(dirname "$0")/.."
python3 -I tools/build_offline.py studio-room.html vendor studio-room-offline.html
if [ -d "$HOME/хранилище/Desktop" ]; then cp studio-room-offline.html "$HOME/хранилище/Desktop/"; echo "скопировано на Мак: ~/Desktop/studio-room-offline.html"; fi
