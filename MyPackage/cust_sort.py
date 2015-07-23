__author__ = 'sujchinn'
studs=["arun-cse-85",
        "arun-ece-85",
        "mani-ise-90",
        "manu-mech-20"
        ]

studs.sort(key=lambda x: int(x.split('-')[-1]))
print studs