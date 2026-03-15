#!/bin/bash
echo "Starting Vector Editor..."
echo "Open http://$(hostname -I | awk '{print $1}'):8000 in your browser"
echo ""
python3 app.py
