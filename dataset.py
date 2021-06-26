"""Pytorch dataset for loading images and annotations."""
import torch


class OxfordPetDataset(torch.utils.data.IterableDataset):
    """A pytorch dataset for the Oxford Pets Dataset."""
    # TODO :-)