all: blinky.bin blinky_timing_report.txt

blinky_timing_report.txt: blinky.asc
	icetime -tmd hx1k blinky.asc > $@

blinky.bin: blinky.asc
	icepack blinky.asc blinky.bin

blinky.asc: blinky.json
	nextpnr-ice40 --hx1k --json blinky.json --package tq144 --pcf blinky.pcf --asc blinky.asc --pcf-allow-unconstrained

blinky.json:
	yosys -p 'synth_ice40 -top top -json blinky.json' blinky.v

flash: blinky.bin
	iceprog blinky.bin

.PHONY: all clean flash

clean:
	rm -f blinky.asc blinky.json blinky.bin blinky_timing_report.txt
