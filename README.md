# Conversor zimbra → mdaemon

App para conversão do arquivo de contatos exportado do cliente Zimbra para importação no Mdaemon.

## Requerimentos
- Windows
- Python >= 3.10

## Configuração

Para rodar utilizando o arquivo `wsgi.py`:

```
git clone https://github.com/vsbits/zimbra_mdaemon_converter
cd zimbra_mdaemon_converter
python -m venv .venv
source .venv/Acripts/Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

**Necessário configurar a variável de ambiente `SECRET_KEY` antes inicialização do app, ou criar um arquivo `.env` na pasta raiz (mesma do arquivo `app.conf`) definindo a variável. Pode ser feito também pelo script `genetate_secret_key.py`:

```
python generate_secret_key.py
```

Para iniciar (assumindo que já está no ambimente virtual):

```
python wsgi.py
```

### Arquivo `app.conf`

#### SERVER
- `host`, `port`: utilizado apenas caso seja rodado pelo script `wsgi.py`. Endereço e porta que o app deve escutar.
- `log_file`: caminho para o arquivo de log.

#### HEADERS
Cabeçalhos dos arquivos no formato: `cabeçalhoZimbra = cabeçalhoMdaemon`

Para incluir novas colunas, verificar o nome gerado pelo zimbra e procurar a coluna equivalente no [manual do mdaemon](https://knowledge.mdaemon.com/csv-fields-importing-contacts-to-webmail).
