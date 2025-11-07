#!/bin/bash
# Script de configuração do projeto

echo "🔧 Configurando projeto Calculadora gRPC..."

# Detecta o comando Python e pip disponível
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python não encontrado!"
    exit 1
fi

# Instala dependências
echo "📦 Instalando dependências..."
echo "⚠️  Se pip não estiver instalado, execute manualmente:"
echo "    $PYTHON_CMD -m ensurepip --upgrade"
echo "    ou instale: sudo apt install python3-pip (Debian/Ubuntu)"
echo ""

$PYTHON_CMD -m pip install -q -r requirements.txt 2>/dev/null || echo "⚠️  Instale as dependências manualmente: $PYTHON_CMD -m pip install -r requirements.txt"

# Gera código dos Protocol Buffers
echo "🔨 Gerando código dos Protocol Buffers..."
$PYTHON_CMD -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/calculator.proto

if [ $? -eq 0 ]; then
    echo "✅ Código gerado com sucesso!"
else
    echo "❌ Erro ao gerar código. Instale as dependências primeiro."
    exit 1
fi

# Torna os scripts executáveis
chmod +x servidor/server.py
chmod +x cliente/client.py

echo "✅ Configuração concluída!"
echo ""
echo "Para executar:"
echo "  Terminal 1: cd servidor && $PYTHON_CMD server.py"
echo "  Terminal 2: cd cliente && $PYTHON_CMD client.py"
