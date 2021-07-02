from odin import Odin

if __name__ == "__main__":
    server_list = ["xx.yy.zz.ll"]
    odc = Odin(server_list)
    odc.establish_connection()
    print(odc.execute_command("echo sample_value", server_list[0]))
    print(odc.execute_command("date", server_list[0]))
    odc.deconstruct_connection()
