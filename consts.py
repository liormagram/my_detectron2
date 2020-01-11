SPLIT_RATE = 0.66

NETS = {}

NETS['faster_rcnn_R_50_FPN_3x'] = { 'config_file'          :"COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml",
                                    'local_coco_weights'   :'model_final_280758.pkl',
                                    'download_coco_weights':'detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl'}