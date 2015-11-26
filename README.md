# author: Ye Hua yh1008
# gRPC
# demonstrates how to use grpc to write a server that talks to an external server that can be written in another language
# implements prof.Yair Sovran's design idea to create a candidate_server, which takes client request and answers in an evasive way.
# (*candidate server talks to an external campaign_manager server to get retorted answer, incorporates it to form the final answer) 
# sample server response: You asked me what is my campaign budget but I want to say that you can't be a Pro-Macbook, and own a Macbook Pro. That's unfair

# this file contains instructions how to build and run gRPC.

# TODO: document how to invoke protoc in order to generate the stubs 
---------------------------------------------------------------
$ protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` debate.proto
------------------------------------------------------------------

# TODO: document how run your server (on localhost)
# this is running on local host port 80000
------------------------------------------------------------------
$ python candidate_server.py
------------------------------------------------------------------

#TODO: document how to run command lint tool
------------------------------------------------------------------
$ chmod +x moderator.py
$ ./moderator.py elaborate finance 2 3 1





