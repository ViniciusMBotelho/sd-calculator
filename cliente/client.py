#!/usr/bin/env python3
"""
Cliente gRPC - Calculadora Remota
Envia operações matemáticas para o servidor executar
"""

import grpc
import sys
import os

# Adiciona o diretório proto ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'proto'))

import calculator_pb2
import calculator_pb2_grpc


def run_calculator():
    """Executa o cliente da calculadora"""
    
    # Conecta ao servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        print("=" * 50)
        print("  CALCULADORA REMOTA - Cliente gRPC")
        print("=" * 50)
        
        while True:
            print("\nOperações disponíveis:")
            print("1. Adição")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("0. Sair")
            
            try:
                opcao = input("\nEscolha uma operação: ")
                
                if opcao == '0':
                    print("Encerrando cliente...")
                    break
                
                if opcao not in ['1', '2', '3', '4']:
                    print("❌ Opção inválida!")
                    continue
                
                # Solicita os números
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                # Cria a requisição
                request = calculator_pb2.OperationRequest(num1=num1, num2=num2)
                
                # Chama a operação correspondente
                if opcao == '1':
                    response = stub.Add(request)
                    operacao = "+"
                elif opcao == '2':
                    response = stub.Subtract(request)
                    operacao = "-"
                elif opcao == '3':
                    response = stub.Multiply(request)
                    operacao = "*"
                elif opcao == '4':
                    response = stub.Divide(request)
                    operacao = "/"
                
                # Exibe o resultado
                print(f"\n✅ Resultado: {num1} {operacao} {num2} = {response.result}")
                print(f"📝 {response.message}")
                
            except grpc.RpcError as e:
                print(f"\n❌ Erro na comunicação: {e.details()}")
            except ValueError:
                print("\n❌ Por favor, digite números válidos!")
            except KeyboardInterrupt:
                print("\n\nEncerrando cliente...")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")


def run_examples():
    """Executa exemplos de operações"""
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        print("\n" + "=" * 50)
        print("  EXEMPLOS DE OPERAÇÕES")
        print("=" * 50)
        
        # Exemplos de operações
        operations = [
            (10, 5, 'Add', '+'),
            (10, 5, 'Subtract', '-'),
            (10, 5, 'Multiply', '*'),
            (10, 5, 'Divide', '/'),
            (100, 0, 'Divide', '/'),  # Teste de divisão por zero
        ]
        
        for num1, num2, operation, symbol in operations:
            try:
                request = calculator_pb2.OperationRequest(num1=num1, num2=num2)
                response = getattr(stub, operation)(request)
                print(f"\n{num1} {symbol} {num2} = {response.result}")
                print(f"   {response.message}")
            except grpc.RpcError as e:
                print(f"\n{num1} {symbol} {num2} = ERRO")
                print(f"   {e.details()}")


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1 and sys.argv[1] == '--examples':
            run_examples()
        else:
            run_calculator()
    except grpc.RpcError:
        print("\n❌ Erro: Não foi possível conectar ao servidor.")
        print("   Certifique-se de que o servidor está rodando.")
