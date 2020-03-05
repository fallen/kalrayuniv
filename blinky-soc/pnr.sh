#!/bin/bash

if [ -z "$PRJXRAY_DIR" ]; then
	echo "You should set PRJXRAY_DIR env variable"
	exit 1
fi

if [ -z "$NEXTPNR_DIR" ]; then
	echo "You should set NEXTPNR_DIR env variable"
	exit 1
fi

$NEXTPNR_DIR/nextpnr-xilinx --chipdb $NEXTPNR_DIR/nextpnr-xilinx/xilinx/xc7a35t.bin --xdc top.xdc --json top.json --write top_routed.json --fasm top.fasm
source $PRJXRAY_DIR/utils/environment.sh
$PRJXRAY_DIR/utils/fasm2frames.py --db-root $PRJXRAY_DIR/database/artix7 --part xc7a35tcsg324-1 top.fasm > top.frames
$PRJXRAY_DIR/build/tools/xc7frames2bit --part_file $PRJXRAY_DIR/database/artix7/xc7a35tcsg324-1/part.yaml --part_name xc7a35tcsg324-1  --frm_file top.frames --output_file top.bit
