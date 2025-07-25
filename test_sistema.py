#!/usr/bin/env python3
"""
Teste básico para o sistema de scraping do Euromilhões
Simple test for the Euromillions scraping system
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from db_utils import EuromilhoesDB

def test_database_initialization():
    """Testa a inicialização da classe EuromilhoesDB"""
    print("🧪 Testando inicialização da base de dados...")
    try:
        db = EuromilhoesDB()
        assert db.db_path is not None
        assert db.csv_path is not None
        assert db.url is not None
        print("✅ Inicialização da base de dados: SUCESSO")
        return True
    except Exception as e:
        print(f"❌ Inicialização da base de dados: FALHOU - {e}")
        return False

def test_csv_reading():
    """Testa a leitura do arquivo CSV"""
    print("🧪 Testando leitura do arquivo CSV...")
    try:
        db = EuromilhoesDB()
        ultimo_sorteio, ultima_data, ultimo_registro = db.ler_ultimo_sorteio()
        assert ultimo_sorteio is not None
        print(f"✅ Leitura do CSV: SUCESSO (Último sorteio: {ultimo_sorteio}, Data: {ultima_data})")
        return True
    except Exception as e:
        print(f"❌ Leitura do CSV: FALHOU - {e}")
        return False

def test_database_view():
    """Testa a visualização da base de dados"""
    print("🧪 Testando visualização da base de dados...")
    try:
        db = EuromilhoesDB()
        # Test that database exists and can be viewed
        if db.db_path.exists():
            db.view_database()
            print("✅ Visualização da base de dados: SUCESSO")
            return True
        else:
            # If database doesn't exist, try to import from CSV
            num_records = db.import_from_csv()
            if num_records > 0:
                print(f"✅ Importação e visualização: SUCESSO ({num_records} registros)")
                return True
            else:
                print("⚠️ Base de dados não existe e CSV vazio")
                return False
    except Exception as e:
        print(f"❌ Visualização da base de dados: FALHOU - {e}")
        return False

def test_csv_structure():
    """Testa a estrutura do arquivo CSV"""
    print("🧪 Testando estrutura do CSV...")
    try:
        db = EuromilhoesDB()
        if db.csv_path.exists():
            with open(db.csv_path, 'r') as f:
                header = f.readline().strip()
                expected_columns = ['DRAW_NUMBER', 'DATE', 'YEAR_DRAW', 'NUMBER_1', 'NUMBER_2', 
                                  'NUMBER_3', 'NUMBER_4', 'NUMBER_5', 'STAR_1', 'STAR_2', 
                                  'NUMBER_OF_WINNERS', 'SORTEIO']
                actual_columns = header.split(',')
                
                # Check if all expected columns are present
                for col in expected_columns:
                    if col not in actual_columns:
                        print(f"❌ Estrutura do CSV: FALHOU - Coluna {col} não encontrada")
                        return False
                
                print("✅ Estrutura do CSV: SUCESSO")
                return True
        else:
            print("⚠️ Arquivo CSV não existe")
            return False
    except Exception as e:
        print(f"❌ Estrutura do CSV: FALHOU - {e}")
        return False

def run_all_tests():
    """Executa todos os testes"""
    print("🚀 Iniciando testes do sistema Euromilhões...")
    print("=" * 50)
    
    tests = [
        test_database_initialization,
        test_csv_reading,
        test_csv_structure,
        test_database_view
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 30)
    
    print("=" * 50)
    print(f"📊 Resultados: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O sistema está funcionando corretamente.")
        return True
    else:
        print("⚠️ Alguns testes falharam. Verifique os problemas acima.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)