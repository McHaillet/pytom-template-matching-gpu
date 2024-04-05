import numpy as np
import sys
import pathlib
from pytom_tm.io import read_mrc, write_mrc

file_name = pathlib.Path(sys.argv[1])
print(file_name)

template = read_mrc(file_name)

ft = np.fft.rfftn(template)
amplitude = np.abs(ft)
new_phases = np.random.random_sample(amplitude.shape) * 2 * np.pi - np.pi
new_template = np.fft.irfftn(amplitude * np.exp(1j * new_phases), s=template.shape)

write_mrc(
    file_name.parent.joinpath(file_name.stem + '_pr.mrc'),
    new_template,
    13.79
)