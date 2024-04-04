import numpy as np
import healpy as hp
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


NSIDE = 8

print('nside:', NSIDE)

npix = hp.nside2npix(NSIDE)
resolution = hp.nside2resol(NSIDE, arcmin=True) / 60
print('npix:', npix)
print('approximate resolution:', resolution)

theta, phi = hp.pix2ang(NSIDE, np.arange(npix))
print('theta min max:', min(theta), max(theta))
print('phi min max:', min(phi), max(phi))

# plt.hist2d(np.rad2deg(psi), np.rad2deg(theta), bins=20)
# plt.show()

n_psi_sampling_points = int(360 / resolution)
psi = np.linspace(0, 2 * np.pi, n_psi_sampling_points, endpoint=False)
print('psi min max:', min(psi), max(psi))

phitheta = np.stack((phi, theta), axis=1)
phithetapsi = np.concatenate(
    (
        np.repeat(phitheta, len(psi), axis=0),
        np.tile(psi, len(phitheta))[:, np.newaxis]
    ),
    axis=1
)
print(phithetapsi.shape)
print(phithetapsi)
