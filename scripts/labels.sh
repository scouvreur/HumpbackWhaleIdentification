#!/bin/bash

cd data/train/

labels="../labels.csv"
rm $labels

declare -a images=(`find . -name *.jpg`)

make_label_csv() {
	for image in "${images[@]}"
	do
		label=`echo $image | cut -d '/' -f 2`
		name=`echo train${image:1:30}`
		echo $name,$label >> $labels
	done
}

echo "name,label" > $labels
make_label_csv
