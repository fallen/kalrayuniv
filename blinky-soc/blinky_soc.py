from migen import *
from litex.boards.platforms import arty
from litex.boards.targets.arty import BaseSoC
from litex.boards.targets.utils import csr_map_update

from litex.soc.interconnect.csr import *
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.integration.soc_sdram import *

class Blinker(Module, AutoCSR):
	def __init__(self, led):
		self.frequency_tuning_word = CSRStorage(32, reset=int(100e6)) 

		ftw = self.frequency_tuning_word.storage
		toggle = Signal()
		counter_preload = Signal(32)
		counter = Signal(32, reset=int(100e6))

		self.comb += [
			toggle.eq(counter == 0),
			counter_preload.eq(ftw),
		]
		self.sync += [
		If(toggle,
			led.eq(~led),
			counter.eq(counter_preload)
		).Else(
			counter.eq(counter - 1)
		)
		]


class BlinkySoC(BaseSoC):
	csr_peripherals = (
		"blinker",
	)
	csr_map_update(BaseSoC.csr_map, csr_peripherals)

	def __init__(self, **kwargs):
		kwargs.update({'cpu_type': 'lm32',
                               'cpu_variant': 'minimal'})
		super().__init__(**kwargs)
		led = self.platform.request("user_led")
		self.submodules.blinker = Blinker(led)


def main():
	import argparse

	parser = argparse.ArgumentParser(description="Blinker SoC")
	builder_args(parser)
	soc_sdram_args(parser)
	args = parser.parse_args()

	soc = BlinkySoC(**soc_sdram_argdict(args))
	builder = Builder(soc, **builder_argdict(args))
	builder.build()

if __name__ == "__main__":
	main()
