import json

with open('sampledata.json', 'r') as sample:
  data=sample.read()

parsed_data=json.loads(data)


print("Interface Status")
print("="*80)
print("{:<51}{:<22}{:<9}{:<5}".format("DN","Description", "Speed", "MTU"))
print("-"*80)


finaldata=parsed_data.get("imdata", [])


for i in finaldata:
  phys=i.get('l1PhysIf', {})
  att=phys.get('attributes', {})

  dn=att.get('dn', '')
  description=att.get('descr', '')
  speed=att.get('speed', '')
  mtu=att.get('mtu', '')
  print("{:<51}{:<22}{:<9}{:<5}".format(dn, description, speed, mtu))



