
import json 


faturamento_diario = [
    1500.00, 2500.00, 0.00, 3000.00, 2200.00,
    0.00, 2800.00, 3100.00, 0.00, 2900.00,
    2700.00, 3500.00, 2000.00, 0.00, 3300.00,
    0.00, 3400.00, 3200.00, 2900.00, 3100.00,
    0.00, 3000.00, 2500.00, 2800.00, 3100.00
]

# Ignorar dias sem faturamento
dias_faturamento = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(dias_faturamento)
maior_faturamento = max(dias_faturamento)
media_mensal = sum(dias_faturamento) / len(dias_faturamento)

dias_acima_media = sum(1 for valor in dias_faturamento if valor > media_mensal)

print(f'Menor valor de faturamento: R$ {menor_faturamento:.2f}')
print(f'Maior valor de faturamento: R$ {maior_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_acima_media}')
print(f'Média mensal: {media_mensal}')