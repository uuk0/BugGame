import json
import os


local = os.path.dirname(os.path.dirname(__file__))


TRIGGERED_BUGS = 0
COLLECTED_BUGS = set()


ALL_BUGS = {"startup:esc_crash"}


def save():
    with open(local+"/stats.json", mode="w") as f:
        json.dump({"triggered": TRIGGERED_BUGS, "collected": list(COLLECTED_BUGS)}, f)


def load():
    if os.path.exists(local+"/stats.json"):
        with open(local + "/stats.json", mode="r") as f:
            d = json.load(f)

        global TRIGGERED_BUGS, COLLECTED_BUGS
        TRIGGERED_BUGS = d["triggered"]
        COLLECTED_BUGS = set(d["collected"])
    else:
        save()

