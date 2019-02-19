#!/bin/bash

declare -a uniq_whale_ids=(`head -n 10 train.csv | cut -d ',' -f 2 | sort | uniq | grep -v Id`)

make_whale_id_dirs() {
	for id in "${uniq_whale_ids[@]}"
	do
		echo $id
		mkdir $id
	done
}

make_whale_id_dirs
