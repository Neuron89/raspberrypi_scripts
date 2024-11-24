#!/bin/bash

# Launch VLC
vlc &

# Wait for VLC to start (adjust the sleep time if VLC takes longer to launch)
sleep 5

# Simulate pressing "Ctrl+1"
xdotool search --onlyvisible --class vlc windowactivate --sync key ctrl+1

# Done

