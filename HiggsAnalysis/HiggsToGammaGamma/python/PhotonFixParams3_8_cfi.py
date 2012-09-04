import FWCore.ParameterSet.Config as cms

#3_8 parameters
PhotonFixParameters = cms.PSet(
meanScale = cms.vdouble(0.994724,1.98102e-06,1.43015e-05,-0.0908525,0.888348,1.20452e-05,-1.04458e-05,-0.542383,0.999461,4.37414e-06,4.92078e-06,-0.121609,0.324634,9.48206e-05,1e-12,1e-12),
meanAT = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
meanAC = cms.vdouble(-0.00352041,0.00982015,434.32,529.508,-0.00320856,0.0240109,115.145,205.859,-0.000396058,0.0144837,1374.93,945.634,-0.00158311,0.0106161,338.964,797.172),
meanAS = cms.vdouble(-1.1,0.00135995,295.712,51320200,0.0349736,-0.00232864,318.584,1.4e+09,-0.000871036,0.0442747,645.709,962.845,-0.00960269,-0.00496491,934.472,8.32667e-16),
meanAM = cms.vdouble(-0.00140562,0.156322,263.097,222.294,-0.00104798,0.208249,297.049,220.609,0.000434298,0.0658628,1928.49,728.522,-0.00219814,0.653906,0.0949848,0.0977831),
meanBT = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
meanBC = cms.vdouble(-0.00294295,0.011533,562.905,421.097,-0.00420429,0.00203991,172.278,410.677,-0.000452212,0.0129968,1056.08,759.102,-0.00423472,0.0279695,28073.7,118612),
meanBS = cms.vdouble(-0.00204373,0.00347592,36.5614,1265.25,-0.0430854,0.0961883,0.196958,11442.2,-0.000786157,0.0346555,592.239,854.285,-0.0012476,0.02744,390.697,727.861),
meanBM = cms.vdouble(-0.00275381,0.0812447,216.885,264.754,-0.00389457,0.0449086,78.9252,103.237,-0.0665038,-0.00211713,4.84395,11.6644,-1.36573e-05,0.0667504,-80154.4,576.637),
meanR9 = cms.vdouble(0.952584,22.7119,402.816,0,0.0182102,-0.03752,0.0198881,0,0.971355,47.2751,536.907,0,0.113317,0.0142669,-0.125721,0),
sigmaScale = cms.vdouble(0.167184,6.14323e-11,0.00769693,0,0.386681,0.0913412,0.00119232,0,0.254641,0.00264818,0.0114953,0,0.471767,0.211196,0.0240124,0),
sigmaAT = cms.vdouble(0.228255,0,0,0,1.36562,0,0,0,0.935839,0,0,0,0.404395,0,0,0),
sigmaAC = cms.vdouble(-0.00411906,0.077799,23.1033,-3e+17,-0.00504613,-1.09115,8.57406,57.1351,-0.00476475,2.14548,29937,2.6e+11,0.00173151,-0.479291,11583.5,-7e+09),
sigmaAS = cms.vdouble(0,0,0,0,0,0,0,0,-8.17285e-05,1.5821,1928.83,902.519,0.000450387,0.662978,924.051,448.417),
sigmaAM = cms.vdouble(-0.000130695,11.2121,468.535,407.652,-0.00014319,5.39527,432.566,265.165,0.0278577,0.58439,43.3575,19.7836,0.00335603,0.648407,134.672,27.4139),
sigmaBT = cms.vdouble(1.33384e-05,8.77098,324.048,239.868,-0.040161,2.65711,-0.398357,-0.440649,-0.456051,0,0,0,0.602402,0,0,0),
sigmaBC = cms.vdouble(-0.00281964,0.125811,538.949,1358.76,0.00580015,-0.631833,18594.3,400955000,-0.00264527,0.696043,7.49509e+12,96843,-0.00256192,2.01276,114558,2154210),
sigmaBS = cms.vdouble(0,0,0,0,0,0,0,0,0.000258933,1.28387,1668.71,730.716,0.00151576,0.359084,329.414,154.509),
sigmaBM = cms.vdouble(-0.00293676,8.88276,350.032,580.354,-0.00376665,3.74316,102.72,157.396,0.00121506,0.938541,9003.57,288.897,-0.0452587,1.26253,1.9e+09,1058.76),
sigmaR9 = cms.vdouble(0.955876,2254.5,14627,0,-3.12696,1.75114,0,0,1.01207,-816.244,-16283.8,0,4.59667,-5.14404,0,0)
)