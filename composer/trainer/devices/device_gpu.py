# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""The GPU device used for training."""

from __future__ import annotations

from typing import Any, Dict, TypeVar

import torch
import torch.cuda.amp
import torch.utils.data

from composer.trainer.devices.device import Device
from composer.utils import dist

__all__ = ['DeviceGPU']

T_nnModule = TypeVar('T_nnModule', bound=torch.nn.Module)


class DeviceGPU(Device):
    """An extension of :class:`~composer.trainer.devices.device.Device` for GPUs.

    This class takes no arguments.
    """
    dist_backend = 'nccl'

    def __init__(self):
        gpu = dist.get_local_rank()
        self._device = torch.device(f'cuda:{gpu}')
        torch.cuda.set_device(self._device)
        assert torch.cuda.current_device() == gpu

    def module_to_device(self, module: T_nnModule) -> T_nnModule:
        return module.to(self._device)

    def tensor_to_device(self, tensor: torch.Tensor) -> torch.Tensor:
        return tensor.to(self._device, non_blocking=True)

    def state_dict(self) -> Dict[str, Any]:
        return {
            'rng': torch.cuda.get_rng_state(),
        }

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        torch.cuda.set_rng_state(state['rng'])
