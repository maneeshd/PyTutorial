"""""""""""""""""""""""""""""
"  Created On: 12-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

import random
import urllib.request

num = random.randrange(1, 1234)
_file = 'IMG-' + str(num) + '.jpg'
urllib.request.urlretrieve("https://pbs.twimg.com/profile_images/762795006801375232/9pzALLqA.jpg", _file)
