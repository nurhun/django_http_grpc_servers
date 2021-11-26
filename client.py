# Working with ./manage.py grpcrunserver
import grpc
import account_pb2
import account_pb2_grpc


with grpc.insecure_channel('0.0.0.0:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)
    for user in stub.List(account_pb2.UserListRequest()):
        print(user, end='')



# # For grpcWSGI
# import grpcWSGI.client
# import account_pb2_grpc
# import account_pb2

# with grpcWSGI.client.insecure_web_channel(
#     f"http://0.0.0.0:50051"
# ) as channel:
#     # stub = account_pb2_grpc.UserControllerStub(channel)
#     # for user in stub.List(account_pb2.UserListRequest()):
#     #     print(user, end='')
#     stub = account_pb2_grpc.UserControllerStub(channel)
#     print(stub.List)
#     # for user in stub.List(account_pb2.UserListRequest):
#     #     print(user, end='')