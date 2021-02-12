from TORic import TORic

toric = TORic(socks_port="23000")
toric.construct_torprocess()
toric.constuct_controller()
print(toric.get_ip())
toric.deconstruct_controller()
toric.deconstruct_torprocess()