# Código de fallback caso grpcio-tools não esteja disponível
print("⚠️  Para usar gRPC, você precisa instalar as dependências:")
print("   1. Instale o pip: sudo pacman -S python-pip")
print("   2. Instale gRPC: python -m pip install --user grpcio grpcio-tools protobuf")
print("   3. Execute: python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto")
