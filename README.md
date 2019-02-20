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

And for submissions using the Kaggle API:

```{bash}
kaggle competitions submit -c humpback-whale-identification -f data/submission.csv -m "Message"
```

## Fastai model

The fastai model starts with loading the `csv` Imagebunch



