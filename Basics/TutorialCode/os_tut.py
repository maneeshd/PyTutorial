"""""""""""""""""""""""""""""
"  Created On: 20-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

import os
import subprocess

output = subprocess.check_output("ver", shell=True)
print(output.decode("UTF-8"))

print(os.path.dirname(os.path.abspath(__file__)))
