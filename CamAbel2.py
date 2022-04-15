# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os.path
from scipy import ndimage as nd
import numpy as np
import matplotlib.pyplot as plt
import abel
import cv2 as cv
# This example demonstrates a BASEX transform of an image obtained using a
# velocity map imaging (VMI) photoelecton spectrometer to record the
# photoelectron angualar distribution resulting from above threshold ionization
# (ATI) in xenon gas using a ~40 femtosecond, 800 nm laser pulse.
# This spectrum was recorded in 2012 in the Kapteyn-Murnane research group at
# JILA / The University of Colorado at Boulder
# by Dan Hickstein and co-workers (contact DanHickstein@gmail.com)
# https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.109.073004
#
# Before you start your own transform, identify the central pixel of the image.
# It's nice to use a program like ImageJ for this.
# https://imagej.nih.gov/ij/

# Specify the path to the file
filename = 'D:/1DataAnalysis/April_first/Timing/14/phi_minus_background_circ.png'

# Step 1: Load an image file as a numpy array
print('Loading ' + filename)
raw_data = plt.imread(filename).astype('float64')

src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
src = nd.rotate(src,4.35)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # converts to grayscale

# Step 2: Specify the origin in (row, col) format
# origin = (1,170)
# or, use automatic centering
origin = 'com'
# origin = 'gaussian'

# Step 3: perform the BASEX transform!


recon = abel.Transform(src_gray, direction='inverse', method='basex').transform
recon2 = abel.Transform(src_gray, direction='inverse', method = 'hansenlaw').transform


fig = make_subplots(
    rows=1, cols=3,
    specs=[[{'type': 'surface'}, {'type': 'surface'}, {'type': 'surface'}]])

fig.add_trace(
    go.Surface(z = src_gray, colorscale='Viridis', showscale=False),
    row=1, col=1)


fig.add_trace(
    go.Surface(z = recon, colorscale='Viridis', showscale=False),
    row=1, col=2)

fig.add_trace(
    go.Surface(z = recon2, colorscale='Viridis', showscale=False),
    row=1, col=3)

fig.show()


