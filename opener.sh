set -e


sudo sonic-pi &

sleep 60

sudo -H -u pi /usr/bin/python3 /home/pi/Desktop/Theremin/FullRun4.py &



/bin/bash