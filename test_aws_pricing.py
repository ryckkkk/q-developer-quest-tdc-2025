#!/usr/bin/env python3
import json
import subprocess
import sys
import os

def test_mcp_config():
    """Testa se o arquivo de configuração MCP está válido"""
    config_path = "/home/participant/.aws/amazonq/mcp.json"
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ Arquivo MCP JSON válido")
        return True
    except FileNotFoundError:
        print("❌ Arquivo MCP não encontrado")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido: {e}")
        return False

def test_uvx_available():
    """Testa se uvx está disponível"""
    try:
        result = subprocess.run(['uvx', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ uvx disponível")
            return True
        else:
            print("❌ uvx não funciona")
            return False
    except FileNotFoundError:
        print("❌ uvx não instalado")
        return False

def test_aws_credentials():
    """Testa se há credenciais AWS configuradas"""
    aws_config_dir = os.path.expanduser("~/.aws")
    credentials_file = os.path.join(aws_config_dir, "credentials")
    config_file = os.path.join(aws_config_dir, "config")
    
    has_credentials = os.path.exists(credentials_file)
    has_config = os.path.exists(config_file)
    
    if has_credentials or has_config:
        print("✅ Arquivos de configuração AWS encontrados")
        return True
    else:
        print("⚠️  Credenciais AWS não configuradas")
        return False

def test_pricing_server():
    """Testa se o servidor de preços pode ser executado"""
    try:
        # Tenta executar o servidor por alguns segundos
        result = subprocess.run([
            'uvx', 'awslabs.aws-pricing-mcp-server@latest', '--help'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ AWS Pricing MCP Server executável")
            return True
        else:
            print(f"❌ Erro ao executar servidor: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("⚠️  Timeout ao testar servidor")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def main():
    print("🧪 Testando AWS Pricing MCP Server...\n")
    
    tests = [
        ("Configuração MCP", test_mcp_config),
        ("uvx disponível", test_uvx_available),
        ("Credenciais AWS", test_aws_credentials),
        ("Servidor de Preços", test_pricing_server)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"Testando: {name}")
        result = test_func()
        results.append(result)
        print()
    
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram!")
        sys.exit(0)
    else:
        print("⚠️  Alguns testes falharam")
        sys.exit(1)

if __name__ == "__main__":
    main()