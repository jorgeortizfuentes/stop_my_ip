from cloudflare_ddns import CloudFlare

from config import api_key, domain, email, notify_to_mail, notify_to_telegram, subdomain
from get_ip import ip_monitor
from notify_to_mail import sent_ip_to_email
from notify_to_telegram import send_telegram_message

cf = CloudFlare(email, api_key, domain)

ip_monitor = ip_monitor()

if ip_monitor["change"]:
    cf.update_record("A", f"{subdomain}.{domain}", ip_monitor["ip"])
    if notify_to_telegram:
        send_telegram_message(
            f"IP address in {subdomain}.{domain} has changed to {ip_monitor['ip']}"
        )
        print("Notification has been sent to Telegram.")
    if notify_to_mail:
        sent_ip_to_email(
            f"IP address has changed to {ip_monitor['ip']}",
            f"IP address in {subdomain}.{domain} has changed",
        )
        print("Notification has been sent to email.")
