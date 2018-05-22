# -*- coding: utf-8 -*- #
import pytest
import tempfile
import os

from donkeycar.templates.train import multi_train
from donkeycar.parts.datastore import Tub
from donkeycar.parts.simulation import SquareBoxCamera, MovingSquareTelemetry

#fixtures
from .setup import tub, tub_path, on_pi

@pytest.mark.skipif(on_pi() == True, reason='Too slow on RPi')
def test_train_cat(tub, tub_path):
    t = Tub(tub_path)
    assert t is not None

    import donkeycar.templates.config_defaults as cfg
    tempfolder = tub_path[:-3]
    model_path = os.path.join(tempfolder, 'test.h5')
    cfg.MAX_EPOCHS = 1
    cfg.BATCH_SIZE = 10
    cfg.SHOW_PLOT = False
    cfg.VEBOSE_TRAIN = False
    cfg.OPTIMIZER = "adam"

    tub = tub_path
    model = model_path
    transfer = None
    model_type = "categorical"
    continuous = False
    aug = False
    multi_train(cfg, tub, model, transfer, model_type, continuous, aug)