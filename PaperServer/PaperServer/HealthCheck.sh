#!/bin/bash
set -o errexit

if pgrep -f "PaperServer.jar" >/dev/null 2>&1; then
    exit 0
else
    exit 1
fi
