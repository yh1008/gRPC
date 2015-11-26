#!/usr/bin/python


from grpc.beta import implementations
import debate_pb2
import argparse

_TIMEOUT_SECONDS = 10

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument("x", help="choose the method for Candidate service")
parser.add_argument("y", help="asking a question|topic", type=str)
parser.add_argument("z", help ="choose timeout|repeated blah_run field", nargs='+', type=int)

args = parser.parse_args()


#print args.x
#print args.y
#print args.z
def run():
        channel = implementations.insecure_channel('localhost', 80000)
        stub = debate_pb2.beta_create_Candidate_stub(channel)

        if args.x == 'answer':
                timeout = args.z[0]
                _TIMEOUT_SECONDS = timeout + 11
                response = stub.Answer(debate_pb2.AnswerRequest(question=args.y, timeout=timeout), _TIMEOUT_SECONDS)
        elif args.x == 'elaborate':
                response = stub.Elaborate(debate_pb2.ElaborateRequest(topic=args.y, blah_run=args.z), _TIMEOUT_SECONDS)

        print response.answer

if __name__ == '__main__':
        run()





