# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""ResNet models for CIFAR extending :class:`.ComposerClassifier`."""

from typing import List, Optional

from composer.models.initializers import Initializer
from composer.models.resnet_cifar.resnets import ResNet9, ResNetCIFAR
from composer.models.tasks import ComposerClassifier

__all__ = ['ComposerResNetCIFAR']


class ComposerResNetCIFAR(ComposerClassifier):
    """ResNet models for CIFAR10 extending :class:`.ComposerClassifier`.

    From `Deep Residual Learning for Image Recognition <https://arxiv.org/abs/1512.03385>`_ (He et al, 2015).
    ResNet9 is based on the  model from myrtle.ai `blog`_.

    Args:
        model_name (str): ``"resnet_9"``, ``"resnet_20"``, or ``"resnet_56"``.
        num_classes (int, optional): The number of classes. Needed for classification tasks. Default: ``10``.
        initializers (List[Initializer], optional): Initializers for the model. ``None`` for no initialization. Default: ``None``.

    Example:

    .. testcode::

        from composer.models import ComposerResNetCIFAR

        model = ComposerResNetCIFAR(model_name="resnet_56")  # creates a resnet56 for cifar image classification

    .. _blog: https://myrtle.ai/learn/how-to-train-your-resnet-4-architecture/
    """

    def __init__(
        self,
        model_name: str,
        num_classes: int = 10,
        initializers: Optional[List[Initializer]] = None,
    ) -> None:
        if initializers is None:
            initializers = []

        if model_name == 'resnet_9':
            model = ResNet9(num_classes)  # current initializers don't work with this architecture.
        else:
            model = ResNetCIFAR.get_model_from_name(
                model_name,
                initializers,
                num_classes,
            )
        super().__init__(module=model)
