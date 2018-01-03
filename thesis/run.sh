#!/bin/bash

function die {
	echo -e "\033[01;31m$1\033[00m"
	exit 1
}

#REPO=https://github.com/bblum/talks
CHECKOUT_DIR=talks
REPO_SUBDIR=thesis
LOG=log.csv

LOG_PATH=$PWD/$LOG

#rm -rf $CHECKOUT_DIR
#git clone $REPO $CHECKOUT_DIR

cd $CHECKOUT_DIR/$REPO_SUBDIR || die "no cd subdir"
git pull || die "no git pull"
make >/dev/null || die "no make"
((git show -s --format=%h,%ci HEAD; pdftk thesis.pdf dump_data | grep NumberOfPages | cut -d' ' -f2; wc -w thesis.tex | cut -d' ' -f1) | tr '\n' ,; echo) >> $LOG_PATH || die "no pdftk"
make clean >/dev/null
