#!/bin/bash

kaggle competitions download -c humpback-whale-identification

mkdir data/

mv *.csv data/

unzip_images() {
	echo $1
	echo mkdir data/$1 && unzip $1.zip -d data/$1
	echo rm $1.zip
}

unzip_images train
unzip_images test
