# 📦 Guia de Instalação - Calculadora gRPC

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação Passo a Passo

### 1. Verificar Python

```bash
python --version
# ou
python3 --version
```

### 2. Instalar pip (se necessário)

#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3-pip
```

#### Linux (Fedora)
```bash
sudo dnf install python3-pip
```

#### Linux (Arch)
```bash
sudo pacman -S python-pip
```

### 3. Instalar Dependências do Projeto

Opção 1 - Usando o script de setup:
```bash
cd calculadora-grpc
./setup.sh
```

Opção 2 - Manualmente:
```bash
cd calculadora-grpc

# Instalar dependências
python -m pip install -r requirements.txt
# ou
python3 -m pip install -r requirements.txt

# Gerar código dos Protocol Buffers
python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto
# ou
python3 -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto
```

### 4. Verificar Instalação

Após a instalação, o diretório `proto/` deve conter:
- `calculator.proto` (original)
- `calculator_pb2.py` (gerado)
- `calculator_pb2_grpc.py` (gerado)

```bash
ls -la proto/
```

## Executando o Projeto

### Terminal 1 - Servidor
```bash
cd servidor
python server.py
# ou
python3 server.py
```

### Terminal 2 - Cliente
```bash
cd cliente
python client.py
# ou
python3 client.py
```

## Problemas Comuns

### Erro: "No module named 'grpc'"

**Solução**: Instale as dependências
```bash
python -m pip install grpcio grpcio-tools protobuf
```

### Erro: "pip: command not found"

**Solução**: Instale o pip conforme seu sistema (ver passo 2)

### Erro: "Permission denied" ao executar setup.sh

**Solução**: Dê permissão de execução
```bash
chmod +x setup.sh
```

### Porta 50051 já em uso

**Solução**: Encerre processos na porta ou mude a porta no código
```bash
# Ver processos na porta
lsof -i :50051

# Encerrar processo
kill -9 <PID>
```

## Ambiente Virtual (Recomendado)

Para evitar conflitos de dependências:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Gerar código proto
python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto
```

## Verificação Final

Execute o cliente em modo de exemplos para testar:
```bash
cd cliente
python client.py --examples
```

Se tudo estiver correto, você verá os resultados das operações matemáticas.
