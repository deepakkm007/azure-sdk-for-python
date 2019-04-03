# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageRegionCreateBatch(Model):
    """Batch of image region information to create.

    :param regions:
    :type regions:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegionCreateEntry]
    """

    _attribute_map = {
        'regions': {'key': 'regions', 'type': '[ImageRegionCreateEntry]'},
    }

    def __init__(self, *, regions=None, **kwargs) -> None:
        super(ImageRegionCreateBatch, self).__init__(**kwargs)
        self.regions = regions
