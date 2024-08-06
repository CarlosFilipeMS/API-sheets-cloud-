# API-sheets-cloud-
Alimentação de base de dados por meio de uma API REST utilizando o Google sheets + google cloud

Esse projeto alimenta uma base de dados(Planilha Google) de forma automatica, ideal para usar em dashboards de atualização automática no Looker studio, toda vez que for feita uma requisição "POST" dos endpoints "/pg1" ou "/pg2" e o email do serviço criado no Google Cloud estiver como editor da planilha automáticamente será adicionado a nova linha com os dados preenchidos e passados no body. 


OBS:  
Criar uma conta no Google Cloud;/n
Baixar as credenciais e substituir no file "Auth";
Criar uma planilha no Google Sheets;
Colocar o nome da página e planilha exatamente igual no projeto;
Adicionar o email do serviço criado no cloud nos editores da planilha;
Importar a planilha como base de dados no Looker Studio.
