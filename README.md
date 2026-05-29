# 📄 Automação de Tradução de Currículo

Este projeto tem como objetivo automatizar o processo de tradução e manutenção do meu currículo. 

Sempre que o currículo base for atualizado, o sistema detecta as mudanças em relação ao último commit no repositório (GitHub), traduz as novidades para o inglês e gera a versão final do currículo automaticamente.

## 📁 Estrutura do Projeto

Baseado na estrutura do repositório, as pastas principais são organizadas da seguinte forma:

* **`content/`**: Diretório principal de trabalho. É aqui que os arquivos com o conteúdo base do currículo ficam armazenados. **Todas as edições devem ser feitas nesta pasta.**
* **`output/`**: Diretório onde o currículo final traduzido e formatado é gerado após a execução do script.
* **`scripts/`**: Contém scripts auxiliares do projeto.
* **`template/`**: Contém os modelos/templates de formatação para a estrutura visual do arquivo final.
* **`sync.py`**: Script principal responsável por orquestrar a detecção de mudanças (diff), realizar a chamada de tradução e gerar o novo documento.
* **`.env`**: Arquivo para variáveis de ambiente (como chaves de API do serviço de tradução que está sendo utilizado).

## 🚀 Como Usar

1. **Atualize seu currículo base:**
   Faça qualquer adição, remoção ou alteração de texto nos arquivos localizados dentro da pasta `content/`.

2. **Execute a sincronização:**
   No terminal, rode o script principal:
```bash
   python sync.py
   ```

3. **Como o processo funciona?**
   * O script `sync.py` utiliza o Git para analisar as diferenças (`git diff`) entre o seu estado atual (na pasta `content/`) e o último commit.
   * Apenas os trechos alterados ou adicionados são enviados para a API de tradução para o inglês.
   * O script aplica as alterações no idioma de destino e reconstrói o arquivo final, salvando-o na pasta `output/`.

## ⚙️ Configuração e Instalação

1. Certifique-se de ter o **Python 3.x** e o **Git** devidamente instalados e configurados na sua máquina.
2. Instale as bibliotecas necessárias (caso possua um `requirements.txt`):
```bash
   pip install -r requirements.txt
   ```
3. Crie ou configure o arquivo `.env` na raiz do projeto com as chaves de API necessárias para realizar as traduções.
4. Lembre-se de sempre comitar suas alterações após a geração com sucesso para que o próximo ciclo de detecção funcione corretamente!
