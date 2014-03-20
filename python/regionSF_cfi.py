# -*- coding: utf-8 -*-
# # flake8: noqa
# Eeg_EHSums, physics LUTs (new: CRAFTPhysicsV1 for HCAL), includes HF AND EE

import FWCore.ParameterSet.Config as cms

regionSF = cms.vdouble(
1.27997, 10.0382, 1.45051, 6.49017, 1.52978, 7.53412, 1.61689, 10.1012, 1.29395, 18.7129, 1.22278, 23.6606, 1.25293, 24.4677, 1.22861, 25.2746, 1.21071, 23.4553, 1.16955, 22.6286, 1.1838, 20.9017, 1.18977, 21.1769, 1.21333, 22.1565, 1.23575, 23.0727, 1.27147, 24.363, 1.22103, 24.9567, 1.22637, 24.2517, 1.30175, 18.7771, 1.61674, 10.2858, 1.53865, 7.30213, 1.42139, 6.72587, 1.26112, 10.0601) 

regionSubtraction = cms.vdouble(
0.010441, 0.033569, 0.076139, 0.134926, 0.215131, 0.315947, 0.440691, 0.590090, 0.763479, 0.954096, 1.165015, 1.398629, 1.683007, 1.815972, 1.77203, 1.9169, 2.06177, 2.20664, 0.019504, 0.079245, 0.161079, 0.259405, 0.375101, 0.509040, 0.658624, 0.834895, 1.037906, 1.269427, 1.527555, 1.806770, 2.122432, 2.454861, 2.32241, 2.50715, 2.69189, 2.87663, 0.050236, 0.142153, 0.261321, 0.393866, 0.540058, 0.700833, 0.879533, 1.085475, 1.326028, 1.601942, 1.908101, 2.241114, 2.623016, 2.859375, 2.82869, 3.04762, 3.26656, 3.4855, 0.039204, 0.081432, 0.139123, 0.201018, 0.266189, 0.341224, 0.427140, 0.532787, 0.659366, 0.811138, 0.982102, 1.170575, 1.376401, 1.699653, 1.51952, 1.63901, 1.7585, 1.87798, 0.080575, 0.086574, 0.102992, 0.114889, 0.130342, 0.149101, 0.177773, 0.223754, 0.291260, 0.389749, 0.543918, 0.773737, 1.103058, 1.456597, 1.05908, 1.14673, 1.23438, 1.32202, 0.062254, 0.072400, 0.089447, 0.095072, 0.103068, 0.114387, 0.129867, 0.153517, 0.186295, 0.230942, 0.288501, 0.385637, 0.454949, 0.593750, 0.475434, 0.510634, 0.545834, 0.581033, 0.085894, 0.087120, 0.109594, 0.125375, 0.139899, 0.155169, 0.174657, 0.202974, 0.237287, 0.289819, 0.360799, 0.434404, 0.525327, 0.494792, 0.503818, 0.538393, 0.572967, 0.607542, 0.057526, 0.115358, 0.138153, 0.153401, 0.170169, 0.187625, 0.211676, 0.243570, 0.290025, 0.346998, 0.425472, 0.520479, 0.587535, 0.751736, 0.642629, 0.688315, 0.734002, 0.779688, 0.046887, 0.123209, 0.152373, 0.171349, 0.186956, 0.204511, 0.229616, 0.266009, 0.317784, 0.385385, 0.469888, 0.567544, 0.700280, 0.737847, 0.696978, 0.746484, 0.795989, 0.845495, 0.066785, 0.139747, 0.184865, 0.202233, 0.225127, 0.244204, 0.272017, 0.312892, 0.373693, 0.454546, 0.555616, 0.699500, 0.809407, 0.871528, 0.823557, 0.88182, 0.940083, 0.998346, 0.109338, 0.184232, 0.231926, 0.260245, 0.276835, 0.298845, 0.334375, 0.380241, 0.446422, 0.526246, 0.644314, 0.761724, 0.919001, 1.083333, 0.954682, 1.02048, 1.08627, 1.15207, 0.106777, 0.192281, 0.230472, 0.244452, 0.264401, 0.285554, 0.319316, 0.364508, 0.427508, 0.510525, 0.617983, 0.753151, 0.871849, 1.060764, 0.92273, 0.986241, 1.04975, 1.11326)+cms.vdouble(0.078211, 0.155514, 0.184269, 0.204553, 0.226632, 0.245843, 0.273920, 0.315276, 0.372498, 0.448208, 0.558120, 0.678564, 0.768674, 0.951389, 0.827739, 0.886088, 0.944437, 1.00279, 0.083727, 0.129112, 0.151096, 0.170769, 0.188178, 0.201568, 0.225954, 0.259387, 0.307563, 0.373679, 0.455165, 0.585692, 0.738679, 0.762153, 0.705181, 0.755084, 0.804987, 0.854889, 0.056541, 0.125523, 0.137377, 0.160796, 0.173807, 0.191319, 0.216251, 0.248073, 0.294409, 0.352219, 0.432466, 0.546585, 0.704248, 0.647569, 0.65019, 0.696051, 0.741913, 0.787775, 0.055359, 0.088174, 0.111034, 0.129357, 0.138106, 0.155326, 0.176148, 0.203725, 0.241826, 0.295441, 0.360934, 0.447882, 0.563375, 0.670139, 0.572066, 0.613705, 0.655344, 0.696983, 0.060875, 0.070815, 0.084721, 0.091203, 0.100025, 0.109039, 0.125200, 0.144570, 0.178759, 0.221135, 0.288795, 0.375060, 0.474090, 0.644097, 0.489745, 0.526774, 0.563803, 0.600832, 0.063436, 0.087525, 0.104860, 0.116044, 0.128848, 0.145621, 0.173978, 0.215899, 0.279411, 0.376471, 0.519026, 0.729521, 0.949580, 1.305556, 0.960485, 1.03907, 1.11765, 1.19623, 0.050433, 0.080045, 0.130324, 0.189256, 0.252757, 0.323573, 0.407174, 0.505875, 0.626692, 0.770640, 0.933436, 1.119468, 1.305789, 1.581597, 1.43348, 1.54578, 1.65809, 1.77039, 0.075650, 0.146606, 0.257979, 0.393018, 0.537308, 0.697458, 0.874601, 1.080887, 1.318170, 1.591370, 1.891174, 2.246224, 2.555672, 3.062500, 2.86054, 3.08263, 3.30471, 3.5268, 0.034870, 0.090329, 0.167785, 0.273728, 0.393035, 0.531421, 0.688272, 0.868013, 1.073915, 1.308847, 1.569478, 1.869793, 2.161648, 2.364583, 2.3389, 2.52318, 2.70745, 2.89173, 0.013396, 0.038878, 0.082565, 0.147201, 0.233471, 0.341180, 0.471723, 0.626414, 0.801051, 0.997313, 1.212176, 1.463288, 1.711368, 1.961806, 1.85829, 2.00985, 2.16142, 2.31298) 