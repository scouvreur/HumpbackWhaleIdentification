# Humpback Whale Identification

## Setup

The prepare the environment, first do (make sure your Kaggle API key is in `~/.kaggle/kaggle.json`):

```{bash}
kaggle competitions download -c humpback-whale-identification
```

And then to generate the CIFAR-like directory substructure do:

```{bash}
python3 subfolders.py
```

And to create the `labels.csv` file:

```{bash}
sh labels.sh
```

To create the validation directory:

```{bash}
python3 make_validation_dir.py
```

And for submissions using the Kaggle API:

```{bash}
kaggle competitions submit -c humpback-whale-identification -f data/submission.csv -m "Message"
```

## Data

Check archive was correctly downloaded using:

```{bash}
md5sum data_MASKED_256.tar.gz
>>> 4ddf5eb697a18a61476f34820d589c21 data_MASKED_256.tar.gz
```

## Fastai model

The fastai model starts with loading the `from_folder` Imagebunch, where the validation set is created by the `make_validation_dir.py` script.

The model is based on transfer learning on a pre-trained ResNet50.
