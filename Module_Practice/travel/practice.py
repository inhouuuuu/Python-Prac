# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
#
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to2 = thailand.ThailandPackage()
# trip_to2.detail()

import inspect
import random
print(inspect.getfile(random))   #패키지 경로 확인
print(inspect.getfile(thailand))
