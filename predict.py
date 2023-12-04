# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
import os


class Predictor(BasePredictor):
    def setup(self) -> None:
        #os tail -f /dev/null
        #os.system("tail -f /dev/null")
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        zip: Path = Input(description="a zip containing the colmap infos and images"),
        resolution: int = Input(description="Specifies resolution of the loaded images before training. If provided 1, 2, 4 or 8, uses original"),
        
    ) -> Path:
        """Run a single prediction on the model"""
        # if data folder exists, remove it
        if os.path.exists("data"):
            os.system("rm -rf data")
        # if output folder exists, remove it
        if os.path.exists("output"):
            os.system("rm -rf output")
        # if output.zip exists, remove it
        if os.path.exists("output.zip"):
            os.system("rm output.zip")

        print("zip: ", str(zip))
        #unzip the zip files in folder data
        os.system("unzip " + str(zip) + " -d data")
        os.system("ls data")
        # # move data/colmap/sparse to data/
        os.system("mv data/colmap/sparse data/")
        os.remove("data/transforms.json")
        # remove data/colmap
        os.system("rm -rf data/colmap")
        # print("==========================")
        os.system("ls data")
        folder = "data/"
        # python train.py -s <path to COLMAP or NeRF Synthetic dataset>
    
        train = os.system("python train.py --model_path=./output --resolution=" + str(resolution) + " -s " + folder )
        print(train)

        # zip the output folder
        os.system("zip -r output.zip output")

        return Path("output.zip")


        # processed_input = preprocess(image)
        # output = self.model(processed_image, scale)
        # return postprocess(output)
