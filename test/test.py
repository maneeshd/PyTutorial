"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 24-Feb-17
"""
masterAdapterDictionary = {
    "Intel Ethernet I350-T4 Onboard Controller": "i350mlom",
    "LSI 1234 MegaRaid Controller": "lsi1234",
    "Cisco VIC 1234 Somethin": "vic1234",
    "Simon": "Mathai"
}

platformListFromExcelSheet = ["Intel Ethernet I350-T4 Onboard Controller",
                              "qwertyuityuio",
                              "LSI 1234 MegaRaid Controller",
                              "asdajksdkjasasd",
                              "Cisco VIC 1234 Somethin",
                              "simon",
                              "Simon"
                              ]

myList = list()
for adapter in platformListFromExcelSheet:
    if adapter in masterAdapterDictionary:
        myList.append(masterAdapterDictionary.get(adapter))

print(myList)
