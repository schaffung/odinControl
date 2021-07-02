# odinControl
A remote command executor

## Why do we need a remote command executor
Well it's an age old requirement. You have X servers and you want to configure them
all without actually going over to each of those servers and doing the operation 
again and again.

One could leverage BASH for doing the same ?
Well technically you can. Create a bash script, then leverage the use of ssh to
remotely execute that BASH script across the servers. ( Actually sounds like a 
challenge, maybe one should take a look into it..). But then comes the 
question of user friendliness.

Is odinControl user friendly?
You tell me. If it isn't, maybe the best way is to either open a BUG or request 
some new feature.

## Wanna quickly try out odin?

Create a virtualenv

```console
[user@sample odinControl]$ virtualenv v1
----some output
```

Activate the virtual env

```console
[user@sample odinControl]$ source v1/bin/activate
```

Install the requirements for odin

```console
[user@sample odinControl]$ pip3 instal -r requirements.txt
```

Set up passwordless ssh with a remote server. Currently the support is only
for root user but this is to be changed to be a configurable model.

```console
[user@sample odinControl]$ ssh-copy-id root@xx.yy.zz.ll
```

Edit the example to reflect the server you've just set-up for the passwordless
ssh. As shown below


```python
from odin import Odin

if __name__ == "__main__":
    server_list = ["xx.yy.zz.ll"] # The ip address change <-----
    odc = Odin(server_list)
    odc.establish_connection()
    print(odc.execute_command("echo sample_value", server_list[0]))
    print(odc.execute_command("date", server_list[0]))
    odc.deconstruct_connection()
```

Run the example code.

``console
[user@sample odinControl]$ python3 example.py
```
