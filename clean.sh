#!/bin/bash
# clean.sh


DIR_SELF="$( cd "$( dirname "$0")" | pwd -P )";
rm "$DIR_SELF/asl-isl-numbers-conversions.zip";
rm -r "${DIR_SELF}/results/";
rm -r "${DIR_SELF}/datasets/";
rm -r "${DIR_SELF}/models/";


