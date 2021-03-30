def hist(s):
    print(f"\n{s}\n")
    kata = ['u','w','x','z']
    tam = []
#     result = ""
    for i in kata:
        if i in s:
             tam.append(f"{i}  {s.count(i)}     {str('*'*s.count(i))}")
    return('\r'.join(tam))
#     if s in :
#         print('halo bandung')


    testing("tpwaemuqxdmwqbqrjbeosjnejqorxdozsxnrgpgqkeihqwybzyymqeazfkyiucesxwutgszbenzvgxibxrlvmzihcb", 
            "u  3     ***\rw  4     ****\rx  6     ******\rz  6     ******")
    testing("aaifzlnderpeurcuqjqeywdq", "u  2     **\rw  1     *\rz  1     *")
    testing("sjeneccyhrcpfvpujfaoaykqllteovskclebmzjeqepilxygdmzvdfmxbqdzubkzturnuqxsewrwgmdfwgdx", 
        "u  4     ****\rw  3     ***\rx  4     ****\rz  4     ****")
    testing("bnxyytdtqrkeaswymiwbxnuydwthweyzny", "u  1     *\rw  4     ****\rx  2     **\rz  1     *")
    testing("tpaemqdmqbqrjbeosjnejqordosnrgpgqkeihqybyymqeafkyicestgsbenvgibrlvmihcb", "")