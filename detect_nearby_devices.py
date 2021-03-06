import bluetooth

devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices." .format(len(devices)))

for address, name in devices:
  print(" {} - {}".format(address, name))