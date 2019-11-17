import time
import random

# refactor: make this asynchronous
def get_elapsed_time(start):
    end_time = time.time()

    return end_time - start

def calculate(start_time, rate):
    # end_time = time.time()
    elapsed_time = get_elapsed_time(start_time)
    raw_minutes = elapsed_time / 60.0000000000
    amt_of_data = raw_minutes * rate
    minutes, seconds = divmod(elapsed_time, 60.00)
    fminutes = round(minutes, 2)
    fseconds = round(seconds, 1)

    if minutes <= 60:
        f_time = f"{fminutes} minutes {fseconds} seconds"
    else:
        hours, minutes = divmod(minutes, 60.00)
        fhours = round(hours, 2)
        f_time = f"{fhours} hrs {fminutes} minutes {fseconds} seconds"

    return (amt_of_data, f_time)

def get_site():
    sites = [
        ("Facebook",1000000,"logins"),
        ("SMS",18100000, "text messages sent"),
        ("You Tube",4500000, "videos viewed"),
        ("App Store", 390030, "apps downloaded"),
        ("Instagram", 347222, "posts were scrolled"),
        ("Twitter", 87500, "people tweeted"),
        ("Tinder", 1400000, "swipes"),
        ("Mail",188000000,"emails sent"),
        ("Twitch",1000000,"views"),
        ("Streaming music",41,"new subscriptions"),
        ("Smart Home Devices (Echo, GoogleHome, etc)",180,"smart speakers shipped"),
        ("Giphy",4800000, "GIFs served"),
        ("DM (Facebook, WhatsApp)", 416000000, "direct messages sent"),
        ("Snapchat", 2100000, "snaps created"),
        ("Ecommerce", 996956, "dollars spent online"),
        ("Netflix", 694444, "hours streamed"),
        ("Google", 3800000, "search queries")
    ]

    select_index = random.randrange(0, len(sites) - 1)
    selection = sites[select_index]

    return selection

site_selected = get_site()
print("************* WELCOME TO THE INTERNET-MINUTE CALCULATOR 2019 ***********")
print(f"\nUsing Data Source: {site_selected[0]}...\n\n\n")

start_time = time.time()
rate = site_selected[1]

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    (amount, totaltime) = calculate(start_time, rate)
    f_amount = round(amount, 1)

    print(f"\n\n{f_amount} {site_selected[2]} in {totaltime} \n\n")
