# Registrador de Curva de Carga para Baterias de Lítio
Este projeto consiste em um sistema de registro de curva de carga para baterias de lítio. O sistema é composto por um dispositivo de medição que envia dados de tensão a cada segundo por meio da porta serial. Um script Python recebe, processa e armazena esses dados em um banco de dados PostgreSQL. Posteriormente, os dados podem ser visualizados no Power BI, incluindo um gráfico que apresenta a curva de carga da bateria.

## Este projeto foi feito para exercitar o uso de banco de dados PostgreSQL e de PowerBI.

## Pré-requisitos
Antes de executar o sistema, certifique-se de ter os seguintes elementos configurados:

Um servidor PostgreSQL instalado e em execução.
Credenciais configuradas no arquivo .env.
Um ambiente virtual configurado usando o script create_env.
## Configuração do Ambiente
Siga estas instruções para configurar o ambiente:

- Execute o script create_env.py para criar a database e as tabelas.
- Se desejar crie um virtualenv e ative
```
python create_env.py
virtualenv venv
.\venv\Scripts\activate    # Windows
```
Instale as bibliotecas necessárias a partir do arquivo requirements.txt.
```
pip install -r requirements.txt
```
## Executando o Programa
Certifique-se de que o servidor PostgreSQL está em execução.

Execute o script principal Main.py.
```
python Main.py
```
## Aquisição de Dados Analógicos (Opcional)
Se você deseja adquirir dados analógicos usando um Arduino, consulte a pasta AnalogInput para obter o script correspondente.

## Visualização dos Dados no Power BI
Os dados armazenados podem ser visualizados no Power BI. Importe o banco de dados PostgreSQL e crie relatórios personalizados.


## Arquivos no Repositório
requirements.txt: Lista de bibliotecas Python necessárias.
create_env.py: Script para criar o ambiente virtual.
.env: Arquivo de configuração para as credenciais.
Main.py: Arquivo principal para executar o programa.
AnalogInput/: Pasta contendo script para aquisição de dados analógicos usando Arduino.
Nota: Certifique-se de revisar e personalizar as variáveis de ambiente, como a porta serial, no arquivo .env conforme necessário.

Lembre-se: Mantenha suas credenciais e informações sensíveis seguras e não as compartilhe publicamente.

Este projeto é uma solução flexível e escalável para monitorar e registrar a curva de carga de baterias de lítio. Caso encontre algum problema ou tenha sugestões de melhoria, sinta-se à vontade para contribuir ou entrar em contato com os mantenedores.