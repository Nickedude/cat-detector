"""Train a neural network to do cat detection."""
import torch

from dataset import OxfordPetDataset


def main():
    """Train a neural network to do cat detection."""
    dataset = OxfordPetDataset()
    loader = torch.utils.data.DataLoader(dataset)


if __name__ == "__main__":
    main()