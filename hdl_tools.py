class Port(object):

   name      = ''
   direction = 'input'
   width     = 1
   _valid_dirs = ['output', 'input']

   def __init__(self, name, direction, width):
     self.name      = name
     self.direction = direction
     self.bitwidth  = width
     assert self.name != ''
     assert self.width >= 1
     assert self.direction in self._valid_dirs

class Parameter(object):

   name        = ''
   default_Val = 1

   def __init__(self, name, default_val):
     self.name         = name
     self.default_val  = default_val
     assert self.name != ''


class Module(object):

   name       = ''
   parameters = []
   ports      = []

   def __init__(self, name):
      self.name = name
      assert name != ''


   def CreateVerilogInstance (self, ports, parameters):
      self.ports = ports
      self.parameters = parameters
      module = "module %s # (\n" % name
      for i in range(len(parameters)):
         if (i != len(parameters)-1):
            module += "      parameter %s = %s,\n" %(parameters[i].name, parameters[i].default_val)
         else:
            module += "      parameter %s = %s\n" %(parameters[i].name, parameters[i].default_val)
      module += "   ) (\n"
      for i in range(len(ports)):
         if (i != len(ports)-1):
            module += "      %s [%s-1:0] %s,\n" %(ports[i].direction, ports[i].width, ports[i].name)
         else:
            module += "      %s [%s-1:0] %s\n" %(ports[i].direction, ports[i].width, ports[i].name)
      module += "   );\n"
      module += "\\\\ insert code here\n"
      module += "endmodule"
      print(module)
   
   
   def CreateVerilogModule (self, ports, parameters):
      self.ports = ports
      self.parameters = parameters
      module = "module %s # (\n" % name
      for i in range(len(parameters)):
         if (i != len(parameters)-1):
            module += "      parameter %s = %s,\n" %(parameters[i].name, parameters[i].default_val)
         else:
            module += "      parameter %s = %s\n" %(parameters[i].name, parameters[i].default_val)
      module += "   ) (\n"
      for i in range(len(ports)):
         if (i != len(ports)-1):
            module += "      %s [%s-1:0] %s,\n" %(ports[i].direction, ports[i].width, ports[i].name)
         else:
            module += "      %s [%s-1:0] %s\n" %(ports[i].direction, ports[i].width, ports[i].name)
      module += "   );\n"
      module += "\\\\ insert code here\n"
      module += "endmodule"
      print(module)


class TopModule(Module):
   
   def __init__(self, name):
      super(TopModule, self).__init__(name)




if __name__ == "__main__":
   name = "test"
   ports = [Port('clk', 'input', 1), Port('data_in', 'input', 32), Port('data_out', 'input', 32)]
   parameters = [Parameter('DATA_WIDTH', 32), Parameter('ADDR_WIDTH', 12)]
   #top_level = TopModule('test_top_level')
   #print(top_level.name)
   #test_mod = Module('test')
   #test_mod.CreateVerilogModule(ports, parameters)
