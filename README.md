# Humpback Whale Identification

## Setup

### Raw Data

The prepare the environment, first do (make sure your Kaggle API key is in `~/.kaggle/kaggle.json`), and then do

```{bash}
sh setup.sh
```

This script will a download and extract the data, generate a CIFAR-like directory substructure, create the `labels.csv` file and create a validation directory from classes with more than one sample image.

For submissions using the Kaggle API, use:

```{bash}
kaggle competitions submit -c humpback-whale-identification -f submission.csv -m "Message"
```

### Pre-processed Data

To use pre-processed data, you can check archive was correctly downloaded using:

```{bash}
md5sum data_MASKED_256.tar.gz
>>> 4ddf5eb697a18a61476f34820d589c21 data_MASKED_256.tar.gz
tar -xzvf data_MASKED_256.tar.gz
```

## Fastai model

The fastai model starts with loading the `from_folder` Imagebunch, where the validation set is created by the `make_validation_dir.py` script.

The model is based on transfer learning on a pre-trained ResNet50. The training process is specified in the `model.ipynb` [notebook](model.ipynb).

To import the pre-trained model, you can use:

```{python}
learn = create_cnn(data, models.resnet50, metrics=[accuracy, map5])
learn.load('stage-1-resnet50')
```

Where in the `models/` directory, `stage-1-resnet50` is before fine-tuning, and `stage-2-resnet50` is after fine tuning.
