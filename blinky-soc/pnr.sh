#!/bin/bash
/home/fallen/dev/nextpnr-xilinx/nextpnr-xilinx --chipdb /home/fallen/dev/nextpnr-xilinx/xilinx/xc7a35t.bin --xdc top.xdc --json top.json --write top_routed.json --fasm top.fasm
source ~/dev/prjxray/utils/environment.sh
/home/fallen/dev/prjxray/utils/fasm2frames.py --db-root /home/fallen/dev/prjxray/database/artix7 --part xc7a35tcsg324-1 top.fasm > top.frames
/home/fallen/dev/prjxray/build/tools/xc7frames2bit --part_file /home/fallen/dev/prjxray/database/artix7/xc7a35tcsg324-1/part.yaml --part_name xc7a35tcsg324-1  --frm_file top.frames --output_file top.bit
