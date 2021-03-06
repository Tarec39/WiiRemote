import bluetooth

print("Searching for nearby devices.")
print("wait for a second ...")

devices = bluetooth.discover_devices(lookup_names=True)

print("Found {} devices." .format(len(devices)))
for address, name in devices:
  print(" {} - {}".format(name, address))

'''
Your Wiimote address is {58:BD:A3:B9:2E:72}
'''