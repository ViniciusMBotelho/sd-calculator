# Calculadora Remota com gRPC

Projeto de calculadora distribuída usando gRPC e Python para a disciplina de Sistemas Distribuídos.

## 📋 Descrição

Este projeto implementa uma calculadora remota usando gRPC (Google Remote Procedure Call). O cliente envia operações matemáticas (soma, subtração, multiplicação e divisão) para um servidor remoto, que executa o cálculo e retorna o resultado.

## 🎯 Objetivo

Entender o ciclo de chamada remota de procedimento (RPC):
- Cliente envia requisição → Servidor processa → Cliente recebe resposta
- Comunicação através de Protocol Buffers
- Serialização/deserialização automática de dados

## 🛠️ Tecnologias

- **Python 3.7+**
- **gRPC** - Framework de RPC do Google
- **Protocol Buffers** - Serialização de dados

## 📁 Estrutura do Projeto

```
calculadora-grpc/
├── proto/
│   ├── calculator.proto      # Definição do serviço e mensagens
│   ├── calculator_pb2.py     # Código gerado (mensagens)
│   └── calculator_pb2_grpc.py # Código gerado (serviço)
├── servidor/
│   └── server.py             # Implementação do servidor
├── cliente/
│   └── client.py             # Implementação do cliente
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.7+** instalado
- **pip** (gerenciador de pacotes Python)

Verifique se estão instalados:
```bash
python --version
pip --version
```

### Passo 1: Configurar o Ambiente Virtual

É **recomendado** usar um ambiente virtual para evitar conflitos de dependências:

```bash
# Navegue até o diretório do projeto
cd calculadora-grpc

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

> **Nota**: No Arch Linux e sistemas com PEP 668, o ambiente virtual é **obrigatório** para instalar pacotes Python.

### Passo 2: Instalar Dependências

Com o ambiente virtual ativado:

```bash
pip install grpcio grpcio-tools protobuf
```

Ou usando o arquivo de requisitos:

```bash
pip install -r requirements.txt
```

### Passo 3: Gerar Código dos Protocol Buffers

Este passo é necessário para gerar os arquivos Python a partir do arquivo `.proto`:

```bash
python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto
```

Após este comando, você verá dois novos arquivos em `proto/`:
- `calculator_pb2.py` (mensagens)
- `calculator_pb2_grpc.py` (serviço)

### Passo 4: Iniciar o Servidor

**Terminal 1** - Execute o servidor:

```bash
# Certifique-se de que o ambiente virtual está ativo
cd servidor
python server.py
```

Você verá:
```
🚀 Servidor de Calculadora iniciado na porta 50051
Aguardando requisições...
```

### Passo 5: Executar o Cliente

**Terminal 2** - Execute o cliente (em outro terminal):

```bash
# Ative o ambiente virtual novamente neste terminal
source venv/bin/activate  # ou venv\Scripts\activate no Windows

cd cliente
python client.py
```

#### Modo Interativo

O cliente apresentará um menu:

```
==================================================
  CALCULADORA REMOTA gRPC
==================================================

Operações disponíveis:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
0. Sair

Escolha uma operação: 
```

Digite o número da operação, depois os dois números para calcular.

#### Modo Exemplos (opcional)

Para executar exemplos pré-definidos automaticamente:

```bash
python client.py --examples
```

Este modo executa várias operações e exibe os resultados:
```
10 + 5 = 15.0
10 - 5 = 5.0
10 * 5 = 50.0
10 / 5 = 2.0
100 / 0 = ERRO (divisão por zero não é permitida)
```

### Resumo dos Comandos (Completo)

```bash
# 1. Criar e ativar ambiente virtual
cd calculadora-grpc
python -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install grpcio grpcio-tools protobuf

# 3. Gerar código protobuf
python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto

# 4. Em um terminal: iniciar servidor
cd servidor
python server.py

# 5. Em outro terminal: executar cliente
cd cliente
python client.py
# ou para exemplos automáticos:
python client.py --examples
```

## 💡 Funcionalidades

O servidor implementa 4 operações:

1. **Adição** (`Add`) - Soma dois números
2. **Subtração** (`Subtract`) - Subtrai dois números
3. **Multiplicação** (`Multiply`) - Multiplica dois números
4. **Divisão** (`Divide`) - Divide dois números (com tratamento de divisão por zero)

## 📝 Exemplo de Uso

```
Operações disponíveis:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
0. Sair

Escolha uma operação: 1
Digite o primeiro número: 10
Digite o segundo número: 5

✅ Resultado: 10.0 + 5.0 = 15.0
📝 Soma executada com sucesso
```

## 🔍 Como Funciona

### Protocol Buffers (calculator.proto)

Define o contrato entre cliente e servidor:
- **Serviço**: Calculator com 4 métodos RPC
- **Mensagens**: OperationRequest (entrada) e OperationResponse (saída)

### Servidor (server.py)

- Implementa a classe `CalculatorServicer`
- Define a lógica de cada operação matemática
- Trata erros (exemplo: divisão por zero)
- Aguarda conexões na porta 50051

### Cliente (client.py)

- Conecta ao servidor via gRPC
- Envia requisições com dois números
- Recebe e exibe o resultado
- Interface interativa no terminal

## 🎓 Conceitos Aprendidos

1. **RPC (Remote Procedure Call)**: Chamada de procedimentos remotos como se fossem locais
2. **gRPC**: Framework moderno de RPC usando HTTP/2
3. **Protocol Buffers**: Serialização eficiente de dados estruturados
4. **Arquitetura Cliente-Servidor**: Comunicação entre processos distribuídos
5. **Tratamento de Erros**: Lidando com exceções em sistemas distribuídos

## 📚 Vantagens do gRPC

- ✅ Alta performance (HTTP/2, Protocol Buffers)
- ✅ Suporte a múltiplas linguagens
- ✅ Streaming bidirecional
- ✅ Geração automática de código
- ✅ Tipagem forte

## 🔧 Possíveis Extensões

- Adicionar mais operações (potência, raiz quadrada, etc.)
- Implementar histórico de operações
- Adicionar autenticação
- Criar interface gráfica (GUI)
- Implementar streaming para múltiplas operações

## 👥 Autor

Projeto desenvolvido para a disciplina de Sistemas Distribuídos.

## 📄 Licença

Este projeto é de uso educacional.
