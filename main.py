from telethon.sync import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import InputReportReasonViolence
import time
import random
import json

f = open('api_config.json')
data = json.load(f)

api_id = data["api_id"]
api_hash = data["api_hash"]
dicks = data["orcs"]
message = data["message"]


client = TelegramClient('anon', api_id, api_hash)


client.start()

for channel in dicks:
    response = client(ReportPeerRequest(peer=channel, reason=InputReportReasonViolence(), message=message))
    print(response)
    sleeptime = random.randint(8, 20)
    time.sleep(sleeptime)
