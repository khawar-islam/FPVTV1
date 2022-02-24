import torch
from vit_pytorch.vits_face import ViTs_face

v = ViTs_face(
    image_size = 256,
    patch_size = 32,
    dim = 1024,
    depth = 6,
    heads = 16,
    mlp_dim = 2048,
    dropout = 0.1,
    emb_dropout = 0.1
)

# import Recorder and wrap the ViT

from vit_pytorch.recoder import Recorder
v = Recorder(v)

# forward pass now returns predictions and the attention maps

img = torch.randn(1, 3, 256, 256)
preds, attns = v(img)

# there is one extra patch due to the CLS token

attns # (1, 6, 16, 65, 65) - (batch x layers x heads x patch x patch)