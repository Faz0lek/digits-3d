import torch
from torchvision import datasets, transforms
from model import Net


IMAGE_FOLDER = r"images"


def get_dataloader():
    transform = transforms.Compose([transforms.Grayscale(),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    dataset = datasets.ImageFolder(IMAGE_FOLDER, transform=transform)

    return torch.utils.data.DataLoader(dataset, batch_size=8, shuffle=True)


def train():
    dataloader = get_dataloader()

    model = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(10):
        for images, labels in dataloader:
            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


if __name__ == "__main__":
    train()
