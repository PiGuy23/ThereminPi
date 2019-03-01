set -e
echo Opening Sonic Pi

sudo sonic-pi &

sleep 60
echo Done
sudo -H -u pi /usr/bin/python3 /home/pi/Desktop/Theremin/FullRun1.py &
echo Done


/bin/bash