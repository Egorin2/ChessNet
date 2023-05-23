from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os
pnconfig = PNConfiguration()
print("Имя пользователя:")
userId = input("")
pnconfig.publish_key = 'pub-c-f60b5e45-2e40-4e34-a45c-34ce61062fd7'
pnconfig.subscribe_key = 'sub-c-34a1b99e-36c6-4179-ac76-fec5eb278b7b'
pnconfig.user_id = userId
pnconfig.ssl = True
pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    pass
class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, presence):
    pass
  def status(self, pubnub, status):
    pass
  def message(self, pubnub, message):
    if message.publisher == userId : return
    print ("from device " + message.publisher + ": " + message.message)
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()

## publish a message
while True:
  msg = input("")
  if msg == 'exit': os._exit(1)
  pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)