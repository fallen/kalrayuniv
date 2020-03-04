from migen import *
from migen.fhdl import verilog

class Blinker(Module):
	def __init__(self, sys_clk_freq, period):
		self.led = led = Signal()

		toggle = Signal()
		counter_preload = int(sys_clk_freq * period/2)
		counter = Signal(max=counter_preload + 1)

		self.comb +=  \
			toggle.eq(counter == 0),
		self.sync += \
		If(toggle,
			led.eq(~led),
			counter.eq(counter_preload)
		).Else(
			counter.eq(counter - 1)
		)

blinker = Blinker(sys_clk_freq=100e6, period=1e-1)
print(verilog.convert(blinker, {blinker.led}))
