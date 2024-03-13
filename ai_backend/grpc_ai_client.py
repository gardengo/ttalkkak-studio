import grpc
import io

from proto import image_pb2 as pb2
from proto import image_pb2_grpc as pb2_grpc

import matplotlib.pyplot as plt
import numpy as np


class TestClient(object):
    def __init__(self):
        self.host = "localhost"
        self.server_port = 9090

        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        self.stub = pb2_grpc.CreateImageStub(self.channel)

    def inputImage(self, originalImage, options):
        OriginalImageInfo = pb2.OriginalImageInfo(
            originalImage=originalImage, options=options
        )

        return self.stub.sendImage(OriginalImageInfo)


if __name__ == "__main__":
    client = TestClient()
    original_image_path = "./src/female_test1.jpg"
    with open(original_image_path, "rb") as f:
        original_image = f.read()

    # print("original image:\n", original_image[:50])
    options = {
        "background": "0",
        "suit": "0",
        "hair": "0",
        "sex": "FEMALE",
    }

    result = client.inputImage(originalImage=original_image, options=options)

    print("processedImage:")
    print()
    print("responseUrl:")
    print(result.responseUrl)