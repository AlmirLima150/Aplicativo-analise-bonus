import pandas as pd
from twilio.rest import Client

account_sid = 'AC0aaab1f5fe6883317de5cfa621b9de8d'
auth_token  = 'fc27da778df7d44acfe9bc3ee4308024'

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to='+5581988430919', 
            from_='+15075745355',
            body=f'No mês {mes}, alguem bateu a meta. Vendedor: {vendedor}. Valor vendido: {vendas}')
        print(message.sid)




