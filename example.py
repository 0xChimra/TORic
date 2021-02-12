from TORic import TORic

#initializing TORic
toric = TORic(socks_port="23000")
#constructing a tor process
toric.construct_torprocess()
#constructing a tor controller
toric.constuct_controller()
#getting the exit node ip of the current tor ciruit
print(toric.get_ip())
#deconstructing a tor controller
toric.deconstruct_controller()
#deconstructing a tor process
toric.deconstruct_torprocess()