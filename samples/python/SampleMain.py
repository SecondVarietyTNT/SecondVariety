#!/bin/env python3

import grpc
from messages_pb2 import *
import requests_pb2
from objects_pb2 import *
from objects_pb2_grpc import *


def GetObjects():
    host='51.250.109.24:5000'
    auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI2IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvdXJpIjpbIi9PYmplY3RzU2Vydi9HZXRCeUlkIiwiL09iamVjdHNTZXJ2L0dldEFsbCJdLCJuYmYiOjE2NjM1MzA5NTksImV4cCI6MTY2NDEzNTc1OSwiaWF0IjoxNjYzNTMwOTU5LCJpc3MiOiJTZWNvbmRWYXJpZXR5IiwiYXVkIjoiQ2xpZW50cyJ9.goQEHMzxCpSzPi7_gwkqtwqcNL6exvCPGk8j0izOVOg'
    metadata = []
    metadata.append(('authorization', 'Bearer ' + auth_token ))
    
    channel = grpc.insecure_channel(host)

    stub =  ObjectsServStub( channel)

    empty = requests_pb2.messages__pb2.Empty()
    objs=stub.GetAll(empty,timeout=2000, metadata = metadata)
    for itm in objs.items:
        print(itm)


    

    
if __name__=="__main__" :
    GetObjects()
