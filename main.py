from pypresence import Presence
import time

client_id = "972628599368716338"
RPC = Presence(client_id)
RPC.connect()

while True:
  RPC.update(
    large_image = "large",
    large_text = "discord.gg/thedevhouse",
    details = "Tu veux parler de dev ?",
    state = "Rejoins : discord.gg/thedevhouse",
    buttons = [{ "label": "Rejoindre", "url": "https://discord.gg/thedevhouse" }]
  )
  print("Successfully set the RPC Status on your profile!")
  time.sleep(60)

