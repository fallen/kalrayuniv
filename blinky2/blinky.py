from migen import *
from migen.build.platforms import ice40_hx8k_b_evn as board

class Blinker(Module):
	def __init__(self, sys_clk_freq, period, led):
		self.led = led

		toggle = Signal()
		counter_preload = int(sys_clk_freq * period/2)
		counter = Signal(max=counter_preload + 1)

		self.comb += toggle.eq(counter == 0)
		self.sync += \
		If(toggle,
			led.eq(~led),
			counter.eq(counter_preload)
		).Else(
			counter.eq(counter - 1)
		)

platform = board.Platform()
led = platform.request("user_led")

blinker = Blinker(sys_clk_freq=100e6, period=1e-1, led=led)
platform.build(blinker)
