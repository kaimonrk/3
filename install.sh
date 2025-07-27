#!/bin/bash
echo "Installing Security Helper Bot..."
pkg update && pkg upgrade -y
pkg install python -y
pip install python-telegram-bot requests
echo "✅ Bot dependencies installed!"