class Clock(object):
    '''
    A class encapsulating information about an FPGA platform.
    '''

    freq = 100
    source = "sys_clk"
    source_tmp = "sys_clk"
    name = ""

    def __init__(self, name):
        '''
        init
        '''
        self.name = name

    def set_freq(self, freq):
        '''
        set the clock frequency
        '''
        self.freq = freq

    def set_source(self, source):
        '''
        set the source pins of the clock
        '''
        self.source = source
