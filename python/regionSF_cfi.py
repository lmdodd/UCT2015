# -*- coding: utf-8 -*-
# # flake8: noqa
# Eeg_EHSums, physics LUTs (new: CRAFTPhysicsV1 for HCAL), includes HF AND EE

import FWCore.ParameterSet.Config as cms
#These are the region corrections. 
#The first, third, fifth,etc number is a region scale facter.
#The second, fourth, sixth,etc. is an offset(this number is divded by 9 in RegionCorrection.cc, and then that is multiplied by 2 because these number are physicalRegionET)  
#This first set of numbers is RCT eta 0, the second set RCT eta 1, thrid RCT eta 3 
regionSF_8TeV_data = cms.vdouble(
1.27997, 10.0382, 1.45051, 6.49017, 1.52978, 7.53412, 1.61689, 10.1012, 1.29395, 18.7129, 1.22278, 23.6606, 1.25293, 24.4677, 1.22861, 25.2746, 1.21071, 23.4553, 1.16955, 22.6286, 1.1838, 20.9017, 1.18977, 21.1769, 1.21333, 22.1565, 1.23575, 23.0727, 1.27147, 24.363, 1.22103, 24.9567, 1.22637, 24.2517, 1.30175, 18.7771, 1.61674, 10.2858, 1.53865, 7.30213, 1.42139, 6.72587, 1.26112, 10.0601) 


#The first set of 18 numbers are region subtractions (in physicalET) for eta 0 and pum bins 0-17, the second set of 18 numbers is for eta 1 and 18 pum bins. etc.


regionSubtraction_PU20_MC13TeV = cms.vdouble(0.000000, 0.120605, 0.169256, 0.268826, 0.382774, 0.513016, 0.663822, 0.832437, 1.027508, 1.243615, 1.484510, 1.748505, 2.046062, 2.398011, 2.850694, 3.134921, 0.000000, 0.000000, 0.000000, 0.156470, 0.206591, 0.316716, 0.437151, 0.575129, 0.724797, 0.900622, 1.100065, 1.319216, 1.566611, 1.840780, 2.146836, 2.512393, 2.978403, 3.746032, 0.000000, 0.000000, 0.000000, 0.123418, 0.266302, 0.359626, 0.484167, 0.622231, 0.777349, 0.951710, 1.152564, 1.374389, 1.628914, 1.912047, 2.231072, 2.600804, 3.047708, 3.246032, 0.000000, 0.000000, 0.000000, 0.073136, 0.119262, 0.170035, 0.220106, 0.275605, 0.345793, 0.421699, 0.516175, 0.624704, 0.753339, 0.897683, 1.068766, 1.261715, 1.510694, 1.773810, 0.000000, 0.000000, 0.055556, 0.246835, 0.273910, 0.336138, 0.416017, 0.486257, 0.575602, 0.688235, 0.841946, 1.037108, 1.312716, 1.656287, 2.139884, 2.717933, 3.581944, 4.833333, 0.000000, 0.000000, 0.027778, 0.081575, 0.159538, 0.185340, 0.203983, 0.233673, 0.261819, 0.298637, 0.346385, 0.404360, 0.478642, 0.565410, 0.688215, 0.843343, 1.077222, 1.757937, 0.000000, 0.000000, 0.000000, 0.140999, 0.150780, 0.173510, 0.211846, 0.234709, 0.266815, 0.302040, 0.350794, 0.405643, 0.469773, 0.544242, 0.643746, 0.772390, 0.966111, 1.341270, 0.000000, 0.000000, 0.027778, 0.073136, 0.168649, 0.194531, 0.217132, 0.257744, 0.288562, 0.330748, 0.380863, 0.433790, 0.506866, 0.593113, 0.698211, 0.848414, 1.000417, 1.559524, 0.000000, 0.000000)+cms.vdouble(0.027778, 0.182138, 0.189746, 0.215618, 0.241512, 0.278904, 0.310158, 0.358551, 0.408175, 0.472616, 0.550445, 0.642227, 0.759521, 0.896945, 1.104861, 1.801587, 0.000000, 0.000000, 0.055556, 0.146273, 0.191632, 0.227958, 0.274799, 0.314503, 0.360935, 0.407808, 0.466380, 0.537669, 0.622278, 0.738058, 0.858959, 1.020501, 1.268681, 1.182540, 0.000000, 0.000000, 0.027778, 0.298875, 0.194157, 0.266737, 0.302445, 0.352081, 0.396646, 0.445615, 0.510057, 0.585290, 0.678849, 0.792132, 0.923268, 1.092671, 1.272917, 1.674603, 0.000000, 0.000000, 0.027778, 0.196906, 0.215701, 0.272407, 0.314203, 0.350184, 0.403693, 0.451630, 0.513017, 0.591138, 0.684406, 0.794723, 0.934995, 1.096773, 1.263472, 2.682540, 0.000000, 0.000000, 0.000000, 0.203586, 0.211865, 0.234317, 0.279873, 0.326339, 0.363821, 0.417158, 0.477276, 0.548621, 0.640194, 0.746714, 0.881186, 1.042592, 1.211389, 2.154762, 0.000000, 0.000000, 0.000000, 0.176864, 0.175042, 0.210207, 0.240979, 0.280980, 0.319586, 0.361009, 0.415540, 0.478681, 0.556795, 0.650872, 0.764839, 0.917022, 1.078958, 1.361111, 0.000000, 0.000000, 0.083333, 0.138186, 0.148255, 0.183218, 0.226484, 0.255919, 0.297690, 0.336035, 0.384665, 0.441222, 0.510402, 0.604469, 0.712385, 0.839121, 0.968333, 1.460317, 0.000000, 0.000000, 0.000000, 0.118495, 0.143076, 0.176666, 0.196477, 0.232085, 0.263392, 0.302656, 0.341165, 0.396920, 0.460773, 0.541928, 0.640016, 0.757635, 0.937917, 0.928571, 0.000000, 0.000000, 0.000000, 0.163502, 0.137706, 0.171678, 0.199074, 0.227707, 0.257758, 0.294587, 0.336764, 0.397252, 0.466851, 0.558507, 0.674198, 0.830031, 1.021111, 1.325397, 0.000000, 0.000000, 0.000000, 0.207103, 0.280303, 0.339056, 0.406884, 0.482201, 0.571267, 0.680040, 0.830221, 1.028213, 1.286050, 1.642039, 2.097342, 2.676099, 3.580764, 4.214286, 0.000000, 0.000000, 0.000000, 0.075246, 0.109896, 0.171037, 0.223973, 0.276169, 0.343961, 0.423382, 0.515281, 0.625262, 0.754821, 0.898535, 1.065229, 1.261645, 1.510694, 1.674603, 0.000000, 0.000000, 0.116737, 0.241242, 0.361715, 0.486229, 0.621300, 0.777202, 0.951448, 1.153620, 1.373879, 1.629597, 1.911760, 2.235784, 2.591466, 3.051528, 3.539683, 0.000000, 0.000000, 0.000000, 0.088608, 0.199431, 0.315091, 0.434705, 0.572647, 0.728147, 0.901087, 1.100828, 1.318835, 1.568081, 1.839141, 2.157059, 2.508234, 2.937361, 3.087302, 0.000000, 0.000000, 0.111111, 0.103024, 0.169000, 0.268494, 0.380306, 0.512103, 0.664542, 0.835524, 1.027807, 1.242631, 1.484586, 1.748726, 2.050053, 2.398987, 2.804097, 2.888889, 0.000000, 0.000000)


regionSubtraction_PU40_MC13TeV=cms.vdouble(0.000000, 0.000000, 0.000000, 0.000000, 0.444444, 0.551170, 0.770085, 0.958352, 1.214790, 1.486655, 1.801059, 2.146229, 2.522583, 2.944799, 3.429136, 3.984393, 4.673410, 6.388889, 0.000000, 0.000000, 0.000000, 0.000000, 0.319444, 0.548246, 0.810256, 0.977690, 1.229211, 1.510501, 1.826860, 2.178931, 2.562520, 2.993610, 3.489558, 4.060866, 4.757649, 5.527778, 0.000000, 0.000000, 0.000000, 0.000000, 0.513889, 0.618421, 0.801496, 1.010128, 1.248957, 1.524992, 1.843374, 2.196967, 2.585665, 3.024237, 3.525665, 4.104405, 4.837409, 5.277778, 0.000000, 0.000000, 0.000000, 0.000000, 0.138889, 0.178363, 0.328846, 0.438023, 0.537074, 0.655743, 0.818238, 0.997956, 1.198403, 1.428185, 1.693293, 1.998691, 2.428744, 2.861111, 0.000000, 0.000000, 0.000000, 0.000000, 0.222222, 0.355263, 0.568803, 0.681711, 0.776114, 0.999194, 1.286749, 1.690190, 2.228222, 2.944096, 3.893814, 5.151409, 7.084399, 8.500000, 0.000000, 0.000000, 0.000000, 0.000000, 0.347222, 0.260234, 0.282479, 0.305702, 0.330235, 0.386729, 0.472834, 0.574252, 0.713821, 0.883901, 1.117625, 1.419786, 1.887530, 2.583333, 0.000000, 0.000000, 0.000000, 0.000000, 0.333333, 0.181287, 0.294444, 0.311500, 0.324732, 0.380449, 0.447851, 0.537887, 0.643667, 0.770106, 0.932555, 1.137137, 1.425775, 1.138889, 0.000000, 0.000000, 0.000000, 0.000000, 0.069444, 0.144737, 0.329701, 0.345149, 0.361473, 0.428805, 0.500501, 0.595122, 0.709161, 0.849070, 1.019010, 1.234842, 1.563255, 3.944444, 0.000000, 0.000000, 0.000000, 0.000000, 0.083333, 0.195906, 0.232692, 0.309886, 0.383756, 0.439078, 0.515435, 0.615713, 0.735333, 0.879855, 1.062850, 1.299136, 1.575533, 1.861111, 0.000000, 0.000000, 0.000000, 0.000000, 0.222222, 0.181287, 0.245085, 0.393035, 0.422420, 0.496332, 0.583994, 0.694272, 0.829494, 0.990583, 1.194619, 1.450821, 1.804499, 2.361111)+cms.vdouble(0.000000, 0.000000, 0.000000, 0.000000, 0.388889, 0.435673, 0.398077, 0.391201, 0.464790, 0.536569, 0.632543, 0.749761, 0.889213, 1.059990, 1.267241, 1.540288, 1.857136, 2.194444, 0.000000, 0.000000, 0.000000, 0.000000, 0.125000, 0.576023, 0.420513, 0.396154, 0.485091, 0.546055, 0.641076, 0.754781, 0.897755, 1.070265, 1.278160, 1.532439, 1.927529, 1.805556, 0.000000, 0.000000, 0.000000, 0.000000, 0.694444, 0.235380, 0.311111, 0.368633, 0.424446, 0.499583, 0.595857, 0.712276, 0.844093, 1.011457, 1.216950, 1.472430, 1.853009, 1.722222, 0.000000, 0.000000, 0.000000, 0.000000, 0.166667, 0.336257, 0.301923, 0.313005, 0.387602, 0.441673, 0.524899, 0.625752, 0.744597, 0.888570, 1.073132, 1.318219, 1.614533, 1.333333, 0.000000, 0.000000, 0.000000, 0.000000, 0.111111, 0.368421, 0.269231, 0.302253, 0.380310, 0.436402, 0.508579, 0.607197, 0.718574, 0.857328, 1.033980, 1.245847, 1.534823, 1.972222, 0.000000, 0.000000, 0.000000, 0.000000, 0.027778, 0.228070, 0.195085, 0.278585, 0.322639, 0.374968, 0.446104, 0.529719, 0.631725, 0.758136, 0.916622, 1.111448, 1.417572, 2.277778, 0.000000, 0.000000, 0.000000, 0.000000, 0.041667, 0.157895, 0.186752, 0.254513, 0.320827, 0.378098, 0.463270, 0.570900, 0.696241, 0.871445, 1.097610, 1.396127, 1.857488, 2.750000, 0.000000, 0.000000, 0.000000, 0.000000, 0.138889, 0.612573, 0.624573, 0.634669, 0.790229, 0.989867, 1.282201, 1.672201, 2.205610, 2.922829, 3.850628, 5.104290, 6.823571, 10.972222, 0.000000, 0.000000, 0.000000, 0.000000, 0.194444, 0.345029, 0.353846, 0.411016, 0.509851, 0.661643, 0.814750, 0.995329, 1.199998, 1.431079, 1.694189, 2.000995, 2.378925, 3.111111, 0.000000, 0.000000, 0.000000, 0.000000, 0.541667, 0.573099, 0.766453, 0.977836, 1.239705, 1.530437, 1.840524, 2.197025, 2.585155, 3.027299, 3.525292, 4.112540, 4.873339, 5.972222, 0.000000, 0.000000, 0.000000, 0.000000, 0.486111, 0.513158, 0.721581, 0.976956, 1.225950, 1.510261, 1.824951, 2.179360, 2.561912, 2.995865, 3.485821, 4.053826, 4.729921, 5.805556, 0.000000, 0.000000, 0.000000, 0.000000, 0.319444, 0.564327, 0.694872, 0.950903, 1.201596, 1.488093, 1.801121, 2.145727, 2.523690, 2.946160, 3.422785, 3.963287, 4.633907, 5.972222)

regionSubtraction_8TeV_data = cms.vdouble(0.010441, 0.033569, 0.076139, 0.134926, 0.215131, 0.315947, 0.440691, 0.590090, 0.763479, 0.954096, 1.165015, 1.398629, 1.683007, 1.815972, 1.77203, 1.9169, 2.06177, 2.20664, 0.019504, 0.079245, 0.161079, 0.259405, 0.375101, 0.509040, 0.658624, 0.834895, 1.037906, 1.269427, 1.527555, 1.806770, 2.122432, 2.454861, 2.32241, 2.50715, 2.69189, 2.87663, 0.050236, 0.142153, 0.261321, 0.393866, 0.540058, 0.700833, 0.879533, 1.085475, 1.326028, 1.601942, 1.908101, 2.241114, 2.623016, 2.859375, 2.82869, 3.04762, 3.26656, 3.4855, 0.039204, 0.081432, 0.139123, 0.201018, 0.266189, 0.341224, 0.427140, 0.532787, 0.659366, 0.811138, 0.982102, 1.170575, 1.376401, 1.699653, 1.51952, 1.63901, 1.7585, 1.87798, 0.080575, 0.086574, 0.102992, 0.114889, 0.130342, 0.149101, 0.177773, 0.223754, 0.291260, 0.389749, 0.543918, 0.773737, 1.103058, 1.456597, 1.05908, 1.14673, 1.23438, 1.32202, 0.062254, 0.072400, 0.089447, 0.095072, 0.103068, 0.114387, 0.129867, 0.153517, 0.186295, 0.230942, 0.288501, 0.385637, 0.454949, 0.593750, 0.475434, 0.510634, 0.545834, 0.581033, 0.085894, 0.087120, 0.109594, 0.125375, 0.139899, 0.155169, 0.174657, 0.202974, 0.237287, 0.289819, 0.360799, 0.434404, 0.525327, 0.494792, 0.503818, 0.538393, 0.572967, 0.607542, 0.057526, 0.115358, 0.138153, 0.153401, 0.170169, 0.187625, 0.211676, 0.243570, 0.290025, 0.346998, 0.425472, 0.520479, 0.587535, 0.751736, 0.642629, 0.688315, 0.734002, 0.779688, 0.046887, 0.123209, 0.152373, 0.171349, 0.186956, 0.204511, 0.229616, 0.266009, 0.317784, 0.385385, 0.469888, 0.567544, 0.700280, 0.737847, 0.696978, 0.746484, 0.795989, 0.845495, 0.066785, 0.139747, 0.184865, 0.202233, 0.225127, 0.244204, 0.272017, 0.312892, 0.373693, 0.454546, 0.555616, 0.699500, 0.809407, 0.871528, 0.823557, 0.88182, 0.940083, 0.998346, 0.109338, 0.184232, 0.231926, 0.260245, 0.276835, 0.298845, 0.334375, 0.380241, 0.446422, 0.526246, 0.644314, 0.761724, 0.919001, 1.083333, 0.954682, 1.02048, 1.08627, 1.15207, 0.106777, 0.192281, 0.230472, 0.244452, 0.264401, 0.285554, 0.319316, 0.364508, 0.427508, 0.510525, 0.617983, 0.753151, 0.871849, 1.060764, 0.92273, 0.986241, 1.04975, 1.11326)+cms.vdouble(0.078211, 0.155514, 0.184269, 0.204553, 0.226632, 0.245843, 0.273920, 0.315276, 0.372498, 0.448208, 0.558120, 0.678564, 0.768674, 0.951389, 0.827739, 0.886088, 0.944437, 1.00279, 0.083727, 0.129112, 0.151096, 0.170769, 0.188178, 0.201568, 0.225954, 0.259387, 0.307563, 0.373679, 0.455165, 0.585692, 0.738679, 0.762153, 0.705181, 0.755084, 0.804987, 0.854889, 0.056541, 0.125523, 0.137377, 0.160796, 0.173807, 0.191319, 0.216251, 0.248073, 0.294409, 0.352219, 0.432466, 0.546585, 0.704248, 0.647569, 0.65019, 0.696051, 0.741913, 0.787775, 0.055359, 0.088174, 0.111034, 0.129357, 0.138106, 0.155326, 0.176148, 0.203725, 0.241826, 0.295441, 0.360934, 0.447882, 0.563375, 0.670139, 0.572066, 0.613705, 0.655344, 0.696983, 0.060875, 0.070815, 0.084721, 0.091203, 0.100025, 0.109039, 0.125200, 0.144570, 0.178759, 0.221135, 0.288795, 0.375060, 0.474090, 0.644097, 0.489745, 0.526774, 0.563803, 0.600832, 0.063436, 0.087525, 0.104860, 0.116044, 0.128848, 0.145621, 0.173978, 0.215899, 0.279411, 0.376471, 0.519026, 0.729521, 0.949580, 1.305556, 0.960485, 1.03907, 1.11765, 1.19623, 0.050433, 0.080045, 0.130324, 0.189256, 0.252757, 0.323573, 0.407174, 0.505875, 0.626692, 0.770640, 0.933436, 1.119468, 1.305789, 1.581597, 1.43348, 1.54578, 1.65809, 1.77039, 0.075650, 0.146606, 0.257979, 0.393018, 0.537308, 0.697458, 0.874601, 1.080887, 1.318170, 1.591370, 1.891174, 2.246224, 2.555672, 3.062500, 2.86054, 3.08263, 3.30471, 3.5268, 0.034870, 0.090329, 0.167785, 0.273728, 0.393035, 0.531421, 0.688272, 0.868013, 1.073915, 1.308847, 1.569478, 1.869793, 2.161648, 2.364583, 2.3389, 2.52318, 2.70745, 2.89173, 0.013396, 0.038878, 0.082565, 0.147201, 0.233471, 0.341180, 0.471723, 0.626414, 0.801051, 0.997313, 1.212176, 1.463288, 1.711368, 1.961806, 1.85829, 2.00985, 2.16142, 2.31298) 
