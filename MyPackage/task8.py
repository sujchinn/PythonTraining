__author__ = 'sujchinn'
zones=[
    "north-10 45 30 7",
    "south-43 54 65 23",
    "east-60 34 7 37",
    "west-45 98 65 56"
]

for zone in zones:
    zone_name=zone.split("-")[0]
    zone_vals = zone.split("-")[1]
    print zone_name,"best is",max(map(int, zone_vals.split()))
