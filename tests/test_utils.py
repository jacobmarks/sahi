import urllib.request
from os import path

import mmdet
from sahi.utils.file import create_dir


def mmdet_version_as_integer():
    return int(mmdet.__version__.replace(".", ""))


class MmdetTestConstants:
    MMDET_CASCADEMASKRCNN_MODEL_URL = "http://download.openmmlab.com/mmdetection/v2.0/cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco/cascade_mask_rcnn_r50_fpn_1x_coco_20200203-9d4dcb24.pth"
    MMDET_CASCADEMASKRCNN_MODEL_PATH = "tests/data/models/mmdet_cascade_mask_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco_20200203-9d4dcb24.pth"
    MMDET_RETINANET_MODEL_URL = "http://download.openmmlab.com/mmdetection/v2.0/retinanet/retinanet_r50_fpn_2x_coco/retinanet_r50_fpn_2x_coco_20200131-fdb43119.pth"
    MMDET_RETINANET_MODEL_PATH = "tests/data/models/mmdet_retinanet/retinanet_r50_fpn_2x_coco_20200131-fdb43119.pth"

    if mmdet_version_as_integer() < 290:
        MMDET_CASCADEMASKRCNN_CONFIG_PATH = "tests/data/models/mmdet_cascade_mask_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py"
        MMDET_RETINANET_CONFIG_PATH = (
            "tests/data/models/mmdet_retinanet/retinanet_r50_fpn_1x_coco.py"
        )
    else:
        MMDET_CASCADEMASKRCNN_CONFIG_PATH = "tests/data/models/mmdet_cascade_mask_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco_v290.py"
        MMDET_RETINANET_CONFIG_PATH = (
            "tests/data/models/mmdet_retinanet/retinanet_r50_fpn_1x_coco_v290.py"
        )


def download_mmdet_cascade_mask_rcnn_model():

    create_dir("tests/data/models/mmdet_cascade_mask_rcnn/")

    if not path.exists(MmdetTestConstants.MMDET_CASCADEMASKRCNN_MODEL_PATH):
        urllib.request.urlretrieve(
            MmdetTestConstants.MMDET_CASCADEMASKRCNN_MODEL_URL,
            MmdetTestConstants.MMDET_CASCADEMASKRCNN_MODEL_PATH,
        )


def download_mmdet_retinanet_model():

    create_dir("tests/data/models/mmdet_retinanet/")

    if not path.exists(MmdetTestConstants.MMDET_RETINANET_MODEL_PATH):
        urllib.request.urlretrieve(
            MmdetTestConstants.MMDET_RETINANET_MODEL_URL,
            MmdetTestConstants.MMDET_RETINANET_MODEL_PATH,
        )
