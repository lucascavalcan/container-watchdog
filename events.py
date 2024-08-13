import docker
import datetime
import requests

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
webhook_url = "https://discord.com/api/webhooks/1272715325087023206/hyZo7uJESOjdHbaoXYNU2-hmLx315cBk3k9skEjm-G9s0Ps2O3-smsoUFE75lkb5Nkho"

for event in client.events(decode=True, filters={"event": "die"}):
  container_id = event["id"]
  container_name = event["Actor"]["Attributes"]["name"]
  epoch_time = event["time"]
  date_time = datetime.datetime.fromtimestamp(epoch_time)

  payload = {"content": "The container %s (%s) terminated at %s" % (container_name, container_id, date_time)}

  print (payload)
  requests.post(webhook_url, data=payload)