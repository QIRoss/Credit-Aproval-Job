# Drop useless columns
def drop_useless_cols(df):
    return df.drop(columns=['profissao_companheiro','grau_instrucao_companheiro', 
                            'local_onde_trabalha', 'local_onde_reside',
                            'meses_no_trabalho', 'possui_cartao_visa',
                            'possui_cartao_mastercard', 'possui_cartao_diners',
                            'possui_cartao_amex', 'forma_envio_solicitacao', 
                            'qtde_contas_bancarias_especiais',
                            'codigo_area_telefone_trabalho',
                            'codigo_area_telefone_residencial',
                            'estado_onde_trabalha',
                            'possui_telefone_trabalho',
                            'grau_instrucao', 'possui_telefone_celular'
])

# Transform text columns
def encode_string_col(df, col):
    df[col] = df[col].astype('category').cat.codes
    
 
