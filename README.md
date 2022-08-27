# Sync dynamic IP with Cloudflare and notify changes

## Instructions

* Rename config_example.py to config.py and fill your data.
* Play cloudflare_sync.py when you need to update your ip.

## Configure crontab

Example:

Play every 1 hour:

0 * * * * /usr/bin/python3 /home/jorge/stop_my_ip/cloudflare_sync.py >> /home/jorge/stop_my_ip/crontab.log 2>&1

Play after reboot:

@reboot sleep 60 && /usr/bin/python3 /home/jorge/stop_my_ip/cloudflare_sync.py >> /home/jorge/stop_my_ip/crontab.log 2>&1
