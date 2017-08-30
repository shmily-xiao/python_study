#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plot
import matplotlib.cm as cm


def create_font(fontname="Tahoma", fontsize=10):
    return {"fontname": fontname, "fontsize": fontsize}


def subplot(title, images, rows, cols, sptitle=[], colormap=cm.gray,
            ticks_visible=True, filename=None):
    fig = plot.figure()
    fig.text(.5, .95, title, horizontalalignment="center")
    for i in xrange(len(images)):
        ax0 = fig.add_subplot(rows, cols, (1 + 1))
        plot.setp(ax0.get_xticklabels(), visible=False)
        plot.setp(ax0.get_yticklabels(), visible=False)
        if len(sptitle) == len(images):
            plot.title("%s #%s" % (sptitle, str(sptitle[i])), create_font())
        else:
            plot.title("%s #%s" % (sptitle, (i+1)), create_font())
        plot.imshow(np.asarray(images[i]), cmap=colormap)
    if filename is None:
        plot.show()
    else:
        plot.savefig(filename)