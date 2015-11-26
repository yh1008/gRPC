### author: Emily Hua
## gRPC exercise that makes fun of politicians
### demonstrates how to use grpc to write a server that talks to an external server written in another language
### implements Prof.Yair Sovran's design idea to create a candidate_server, which takes client request and answers in an evasive way.
### (*candidate server talks to an external campaign_manager server to get retorted answer, incorporates it to form the final answer)
### sample client request: "what is your campaign budget"
### sample server response: "You asked me what is my campaign budget but I want to say that you can't be a Pro-Macbook, and own a Macbook Pro. That's unfair"



#### how to invoke protoc in order to generate the stubs: 
$ protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` debate.proto


####how run your server (on localhost):
#####//this is running on local host port 80000
$ python candidate_server.py


####how to run command lint tool:
$ chmod +x moderator.py \n
$ ./moderator.py elaborate finance 2 3 1\n
$ ./moderator.py answer "what is your campaign budget" 5





