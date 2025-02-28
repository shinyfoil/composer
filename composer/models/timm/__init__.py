# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""A wrapper around `timm.create_model() <https://rwightman.github.io/pytorch-image-models/#load-a-pretrained-model>`_
used to create :class:`.ComposerClassifier`."""

from composer.models.timm.model import Timm as Timm
from composer.models.timm.timm_hparams import TimmHparams as TimmHparams

__all__ = ['Timm', 'TimmHparams']
