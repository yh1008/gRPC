
#implement the method of Answer && Elaborate`

from random import randint
from grpc.beta import implementations
import re
import debate_pb2
import consultation_pb2
import time
#from time import time
_TIMEOUT_SECONDS = 10
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

#start_word_list = ['why', 'what', 'how', 'who', 'when']
class Candidate(debate_pb2.BetaCandidateServicer):

        def Answer(self, request, context): #? is it the right argument to take in?
                t0 = time.clock()
                sentence = request.question.split()
                start_word = sentence[0].lower()
                match = re.search(r'what|why|how|who|when',start_word)
                if not match:
                        rand_num = randint (0,1)
                        if rand_num == 0:
                                ran_answer = "your 3 cent titanium tax goes too far"
                        else:
                                ran_answer = "your 3 cent titanium tax doesn't go too far enough"
                                #AnswerReply.answer
                        return debate_pb2.AnswerReply(answer=ran_answer)
                if match:
                        answer_sub = []
                        for word in sentence:
                                word = word.lower()
                                if word == "you":
                                        word = "I"
                                elif word == "your":
                                        word = "my"
                                #re.sub('\.', '', word)
                                answer_sub.append(word + " ")
                        answer_string = ''.join(answer_sub)
                #makes an RPC call to external server CampainManager.Retort with request = "answer_sub "
                        channel = implementations.insecure_channel('54.88.18.92', 50051)
                        stub = consultation_pb2.beta_create_CampaignManager_stub(channel)
                        t1 = time.clock()
                        time_lapsed = t1 - t0

                        t1 = time.clock()
                        time_lapsed = t1 - t0
                        time_remain = 10 + request.timeout - time_lapsed
                        _TIMEOUT_SECONDS = time_remain
                        RetortReply = stub.Retort(consultation_pb2.RetortRequest(original_question=answer_string), _TIMEOUT_SECONDS)
                        print ("CampaignManager service replied: " + RetortReply.retort)
                        t2 = time.clock()
                        if t2-t0 > 10 + request.timeout:

                                return debate_pb2.AnswerReply(answer='No comment.')
                        else:
                                answer = 'You asked me ' + answer_string + 'but I want to say that ' + RetortReply.retort

                                return debate_pb2.AnswerReply(answer=answer)
        def Elaborate(self, request, context):
                answer = []
                topic = request.topic
                num_blah = request.blah_run
                #num_blah is empty list
                if not num_blah:
                        answer_string = topic

                if num_blah:
                        for i in num_blah:
                                for j in range(i):
                                        answer.append('blah_run ')

                                answer.append(topic)
                                answer.append(" ")
                        length = len(topic)
                        answer_string = ''.join(answer)
                        if len(num_blah) > 1:
                                answer_string= answer_string[:-( length+1)]

                return debate_pb2.ElaborateReply(answer=answer_string)
def serve():
        server = debate_pb2.beta_create_Candidate_server(Candidate())
        server.add_insecure_port('[::]:80000') #bind to any port that is higher than 20000
        server.start()
        try:
                while True:
                        time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
                server.stop()
       except KeyboardInterrupt:
                server.stop()

if __name__ == '__main__':
        serve()
