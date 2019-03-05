#!/bin/bash

square_images() {
	echo $1
	for IMG in data_MASKED_256/$1/*.jpg;
	do
		convert $IMG -resize 256x256! $IMG
	done
}

square_images train
square_images test
