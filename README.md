# API-sheets-cloud-
Alimentação de base de dados por meio de uma API REST utilizando o Google sheets + google cloud

Esse projeto alimenta uma base de dados(Planilha Google) de forma automatica, ideal para usar em dashboards de atualização automática no Looker studio, toda vez que for feita uma requisição "POST" dos endpoints "/pg1" ou "/pg2" e o email do serviço criado no Google Cloud estiver como editor da planilha automáticamente será adicionado a nova linha com os dados preenchidos e passados no body.

Deixarei uma breve explicação de como configurar os serviços do Google e um passo a passo dessa criação/configuração de serviços

## Passo a passo
### Google cloud:
1- Depois de fazer o login com a sua conta Google no Cloud, você clica em NOVO PROJETO e nomeia o projeto;  
2- Adicionar as bibliotecas "Google Sheets API" e "Google Drive API" ao projeto;  
3- Com o projeto configurado, dentro dele você vai na parte de credenciais e cria uma "ID do cliente OAuth";
4- Novamente na parte de credenciais você cira uma "conta de serviço". Com a conta criada, um e-mail vai ser gerado, ele será importante para o projeto;
5- Com a conta de serviço criada você vai nas chaves e gera uma chave privada e baixa o arquivo da chave.

### Google sheets:
1- Cria uma planilha, e slave o nome;
2- Adicione o email da conta de serviço criada nos editores da planilha.

### Código:
1- Altere o arquivo "Credentials.json", basta apagar tudo e colar as informações que você baixou na chave;
2- Instale as dependencias do projetos (todas elas estão no "requirements.txt", basta dar um pip install);
3- No arquivo "auth.py", defina o username e a password para a autenticação;
4- No arquivo "functions.py" defina o nome dos modelos e os atributos;
5- Ainda no "functions.py" defina o nome da rota, o nome da planilha e o nome da página (o nome da planilha e página devem estar exatamente iguais ao nome do Google Sheets).

## Exemplo de uso/teste:
### Postman
1- Rode o localhost(uvicorn) ou hospede o código;
-DICA- Você pode entra pelo link gerado no terminal quando vc hospedar e escreve "/docs" depois da URL, vc vai encontrar a doc automática do FastAPI, podendo até testar na doc.
2- Abra o postman e crie a requisição de auth de método *POST* e faça o login com o *username* e *password* definidos no código, esse dados serão passados no body;
3- Será retornado um código Bearer, você precisará passar esse código no header da próxima requisição;
4- Crie a requisição também do tipo POST, passando a URL do endpoint e seus atributos, lembre de adicionar um header de *Authorization* e passar "Bearer <código gerado>";
5- Ao fazer a requisição confira na planilha que uma nova linha foi adicionada.

## Nota
Com essa API você pode chamar os endpoints diretamente do seu sistema, passando os atributos específicados no *modelo*(Encontrado em: functions.py), para uma plailha do google sheets para alimentar uma base de dados que pode servir para um dashboard por exemplo no Looker Studio, fazedo com que ele tenha uma atualização automática. 


