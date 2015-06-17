# from ophyd.controls import ProsilicaDetector, EpicsSignal, EpicsScaler
from ophyd.controls import EpicsScaler, EpicsSignal
from ophyd.controls.area_detector import (AreaDetector,
                                          AreaDetectorFileStorePrinceton,
                                          AreaDetectorFileStoreHDF5)

# CSX-1 Scalar

#sclr = EpicsScaler('XF:23ID1-ES{Sclr:1}', name='sclr', numchan=32)
sclr = EpicsScaler('XF:23ID1-ES{Sclr:1}', name='sclr', numchan=8)

# sclr_trig = EpicsSignal('XF:23ID1-ES{Sclr:1}.CNT', rw=True,
#                         name='sclr_trig')
# sclr_ch1 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S1', rw=False,
#                        name='sclr_ch1')
# sclr_ch2 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S2', rw=False,
#                        name='sclr_ch2')
# sclr_ch3 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S3', rw=False,
#                        name='sclr_ch3')
# sclr_ch4 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S4', rw=False,
#                        name='sclr_ch4')
# sclr_ch5 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S5', rw=False,
#                        name='sclr_ch5')
# sclr_ch6 = EpicsSignal('XF:23ID1-ES{Sclr:1}.S6', rw=False,
#                        name='sclr_ch6')
# temp_a = EpicsSignal('XF:23ID1-ES{TCtrl:1-Chan:A}T-I', rw=False,
#                      name='temp_a')
# temp_b = EpicsSignal('XF:23ID1-ES{TCtrl:1-Chan:B}T-I', rw=False,
#                      name='temp_b')

# AreaDetector Beam Instrumentation
# fs1_cam = ProsilicaDetector('XF:23IDA-BI:1{FS:1-Cam:1}')
# diag3_cam = ProsilicaDetector('XF:23ID1-BI{Diag:3-Cam:1}')
# diag5_cam = ProsilicaDetector('XF:23ID1-BI{Diag:5-Cam:1}')
# diag6_cam = ProsilicaDetector('XF:23ID1-BI{Diag:6-Cam:1}')
# diag6_cam = ProsilicaDetector('XF:23ID1-BI{Diag:6-Cam:1}')
# dif_beam_cam = ProsilicaDetector('XF:23ID1-ES{Dif-Cam:Beam}')

fs1_cam = AreaDetector('XF:23IDA-BI:1{FS:1-Cam:1}', name='fs1_cam')
diag3_cam = AreaDetector('XF:23ID1-BI{Diag:3-Cam:1}', name='diag3_cam')
diag5_cam = AreaDetector('XF:23ID1-BI{Diag:5-Cam:1}', name='diag5_cam')
diag6_cam = AreaDetector('XF:23ID1-BI{Diag:6-Cam:1}', name='diag5_cam')
diag6_cam = AreaDetector('XF:23ID1-BI{Diag:6-Cam:1}', name='diag6_cam')
dif_beam_cam = AreaDetector('XF:23ID1-ES{Dif-Cam:Beam}', name='dif_beam_cam')

# Princeton CCD camera

pimte = AreaDetectorFileStorePrinceton('XF:23ID1-ES{Dif-Cam:PIMTE}',
                                       file_path='/GPFS/xf23id/xf23id1/pimte_data/',
                                       ioc_file_path='x:/xf23id1/pimte_data/',
                                       name='pimte')

fshutter = EpicsSignal('XF:23ID1-TS{EVR:1-Out:FP0}Src:Scale-RB',
                       write_pv='XF:23ID1-TS{EVR:1-Out:FP0}Src:Scale-SP',
                       rw=True, name='fshutter')

fccd = AreaDetectorFileStoreHDF5('XF:23ID1-ES{FCCD}',
                                 file_path='/GPFS/xf23id/xf23id1/fccd_data/',
                                 #shutter=fshutter, shutter_val=(4,3),
                                 stats=None,
                                 name='fccd')
# Test CCD

ccdtest = AreaDetectorFileStoreHDF5('XF:23ID1-ES{Tst-Cam:1}',
                                    file_path='/GPFS/xf23id/xf23id1/test_data/',
                                    name='ccdtest')

# pimte_cam = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}cam1:Amecquire_RBV',
#                         write_pv='XF:23ID1-ES{Dif-Cam:PIMTE}cam1:Acquire',
#                         rw=True, name='pimte_cam_trigger')
# pimte_tot1 = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}Stats1:Total_RBV',
#                          rw=False, name='pimte_tot1')
# pimte_tot2 = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}Stats2:Total_RBV',
#                          rw=False, name='pimte_tot2')
# pimte_tot3 = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}Stats3:Total_RBV',
#                          rw=False, name='pimte_tot3')
# pimte_tot4 = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}Stats4:Total_RBV',
#                          rw=False, name='pimte_tot4')
# pimte_tot5 = EpicsSignal('XF:23ID1-ES{Dif-Cam:PIMTE}Stats5:Total_RBV',
#                          rw=False, name='pimte_tot5')
