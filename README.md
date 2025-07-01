# 🥗 Suap Meals

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-00FFFF?style=for-the-badge)

**`Sistema para reservas automáticas de refeições`**  

> Esse projeto efetua reservas diárias de refeições no restaurante universitário do [IFPI - Campus Parnaíba](https://www.ifpi.edu.br/parnaiba)  
por meio do [SUAP](https://suap.ifpi.edu.br/accounts/login/?next=/) (Sistema Unificado de Administração Pública) da instituição.  

## Ferramentas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Instruções de Uso

> ⚠️ **Atenção**: certifique-se de estar com seu **acesso ativo** ao [SUAP](https://suap.ifpi.edu.br/accounts/login/?next=/)!

>📝 **Nota**: no momento o script efetua apenas a **reserva do almoço**. 

### 1. Fork do repositório

**`Uma cópia independente do repositório será criada na sua conta do github`**  

* Vá no **canto superior direito** desse repositório e click no botão "**Fork**";
* Na tela seguinte confirme a criação do fork.

### 2. Configuração de credenciais do SUAP

**`O repositório/script terá acesso a sua matrícula e senha do SUAP de forma segura e confidencial por meio do GitHub Secrets.`**

* Dentro do repositório criado na sua conta, acesse o **menu de configurações**;
* Na barra **lateral esquerda**, role para baixo e selecione a opção "**Secrets and variables**";
* Em seguida, selecione a opção "**Actions**";
* Na tela seguinte, clique em "**New repository secret**" e defina **cada um** dos dois pares de chave-valor:  
    * **Name***: SUAP_USERNAME | **Secret***: *sua_matricula*
    * **Name***: SUAP_PASSWORD | **Secret***: *sua_senha*

### 3. Pronto!🎉🥳

**`O próprio GitHub ficará responsável por executar o código de forma agendada e garantir a reserva automática de sua refeição.`**  
> 📝 **Nota**: O script agora é executado **de domingo a quinta-feira, às 21:30 (horário de Brasília)**. Isso é configurado no GitHub Actions com a expressão cron `30 0 * * 0-4`. Lembre-se que o GitHub Actions opera em UTC, então `00:30 UTC` corresponde a `21:30 BRT/BRST` (horário de Brasília, que é UTC-3).
