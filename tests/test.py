import pandas as pd
import pytest

# Função que será testada
def clean_data(df):
    df = df.dropna(subset=["value"])  # Remove linhas com valores nulos na coluna "value"
    df["value"] = df["value"].astype(float)  # Converte para float
    return df

# Teste TDD
def test_clean_data():
    data = pd.DataFrame({"value": [10.22, None, 20.21]})
    cleaned_df = clean_data(data)
    
    # assert cleaned_df.shape[0] == 2  # Deve ter apenas 2 linhas após remover nulos
    assert cleaned_df["value"].dtype == float  # A coluna deve ser float