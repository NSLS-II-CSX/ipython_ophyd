from ophyd.userapi.scan_api import Scan, AScan, DScan, Count, estimate

scan = Scan()
ascan = AScan()
ascan.default_detectors = [sclr]
dscan = DScan()

# Use ct as a count which is a single scan.

ct = Count()

from csxtools.ophyd_tools import CSXAScan

cscan = CSXAScan()
