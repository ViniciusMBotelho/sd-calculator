#!/usr/bin/env python3
"""
Servidor gRPC - Calculadora Remota
Implementa operações matemáticas básicas via gRPC
"""

import grpc
from concurrent import futures
import sys
import os

# Adiciona o diretório proto ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'proto'))

import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    """Implementação do serviço de calculadora"""
    
    def Add(self, request, context):
        """Soma dois números"""
        result = request.num1 + request.num2
        print(f"[ADD] {request.num1} + {request.num2} = {result}")
        return calculator_pb2.OperationResponse(
            result=result,
            message=f"Soma executada com sucesso"
        )
    
    def Subtract(self, request, context):
        """Subtrai dois números"""
        result = request.num1 - request.num2
        print(f"[SUBTRACT] {request.num1} - {request.num2} = {result}")
        return calculator_pb2.OperationResponse(
            result=result,
            message=f"Subtração executada com sucesso"
        )
    
    def Multiply(self, request, context):
        """Multiplica dois números"""
        result = request.num1 * request.num2
        print(f"[MULTIPLY] {request.num1} * {request.num2} = {result}")
        return calculator_pb2.OperationResponse(
            result=result,
            message=f"Multiplicação executada com sucesso"
        )
    
    def Divide(self, request, context):
        """Divide dois números"""
        if request.num2 == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Divisão por zero não é permitida')
            print(f"[DIVIDE] Erro: tentativa de divisão por zero")
            return calculator_pb2.OperationResponse(
                result=0,
                message="Erro: divisão por zero"
            )
        
        result = request.num1 / request.num2
        print(f"[DIVIDE] {request.num1} / {request.num2} = {result}")
        return calculator_pb2.OperationResponse(
            result=result,
            message=f"Divisão executada com sucesso"
        )


def serve():
    """Inicia o servidor gRPC"""
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server
    )
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    
    print(f"🚀 Servidor de Calculadora iniciado na porta {port}")
    print("Aguardando requisições...")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\n🛑 Servidor encerrado")
        server.stop(0)


if __name__ == '__main__':
    serve()
