Requirements:

* nextpnr (PNR for Lattice ice40 and ECP5)
  * https://github.com/YosysHQ/nextpnr
* nextpnr-xilinx (PNR for Xilinx xc7 and xcup)
  * https://github.com/daveshah1/nextpnr-xilinx
* IceStorm (bitstream generation for ice40)
  * https://github.com/cliffordwolf/icestorm.git
* Yosys (synthesis tool)
  * https://github.com/YosysHQ/yosys
* xc3sprog (jtag / flashing tool for Xilinx FPGA/CPLD)
  * svn co https://xc3sprog.svn.sourceforge.net/svnroot/xc3sprog/trunk xc3sprog
* openocd (jtag / flashing tool)
  * https://git.code.sf.net/p/openocd/code
  * use the git version, not your system package, to support flashing Arty board.
