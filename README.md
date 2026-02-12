
## 🛡️ Project Verdandi
> Automação de Backup Inteligente & Monitoramento de Arquivos em Tempo Real.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📋 Sobre o Projeto

O **Project Verdandi** é uma ferramenta de automação de backup (daemon) desenvolvida para resolver o problema de perda de dados em ambientes de desenvolvimento voláteis. Diferente de backups agendados (Cron), o Verdandi opera com **Monitoramento Baseado em Eventos**.

Ele vigia diretórios específicos e dispara rotinas de backup instantaneamente após a detecção de alterações (modificação ou criação de arquivos), utilizando lógica de **Debounce** para otimizar operações de I/O e garantir integridade.

## 🚀 Key Features (Destaques Técnicos)

* **Monitoramento em Tempo Real:** Utiliza a biblioteca `watchdog` para escutar eventos do sistema de arquivos (File System Events) com zero latência.
* **Smart Debounce (Concorrência):** Implementação de lógica com `threading.Timer` para prevenir condições de corrida e "backup storm". Se um arquivo é salvo múltiplas vezes em milissegundos, apenas a versão estável é processada.
* **Arquitetura Modular:** Separação clara de responsabilidades seguindo princípios SOLID:
    * `GuardianHandler`: Lógica de eventos e threads.
    * `ConfigManager`: Persistência de configurações JSON.
    * `CLI UI`: Interface interativa para usuários finais.
* **Configuração Dinâmica:** Suporte a persistência de configurações via JSON e hot-swap de parâmetros via menu.

## 🛠️ Arquitetura do Sistema

O núcleo do sistema reside na classe `GuardianHandler`, que herda de `FileSystemEventHandler`.

### Fluxo de Execução:
1.  **Detecção:** O sistema operacional notifica o Verdandi sobre uma mudança (`on_modified`).
2.  **Filtragem:** O arquivo passa por filtros de extensão (ex: `.psd`, `.py`) e checagem de loop infinito (origem != destino).
3.  **Agendamento (Threading):** Um Timer é instanciado. Se um novo evento ocorrer antes do Timer expirar, o anterior é cancelado (`timer.cancel()`).
4.  **Execução:** O backup é efetivado usando `shutil`, com timestamping para versionamento (`arquivo_2024-02-12_10-00-00.ext`).

## ⚙️ Instalação e Uso

### Pré-requisitos
* Python 3.10 ou superior
* Pip (Gerenciador de pacotes)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Soulahh/project-verdandi.git](https://github.com/Soulahh/project-verdandi.git)
    cd project-verdandi
    ```

2.  **Instale as dependências:**
    ```bash
    pip install watchdog
    ```

3.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

## 🔧 Configuração (`config.json`)

O comportamento do Verdandi é controlado pelo arquivo `config.json`. O sistema gera um padrão se não existir:

```json
{
    "origem": "/home/user/pasta_monitorada",
    "destino": "/home/user/backup",
    "extensoes": [".txt", ".py", ".jpg", ".png", ".psd"],
    "delay": 2.0,
    "silent": true,
    "mode": "interactive"
}

```

* **delay:** Tempo (em segundos) de espera do *Debounce* antes de copiar o arquivo.
* **mode:** `interactive` (Menu CLI) ou `script` (Headless/Background).
* **silent:** `true` para suprimir outputs não críticos.

## 📂 Estrutura do Projeto

```text
project-verdandi/
├── main.py                  # Entrypoint e Orquestrador
├── config.json              # Configurações Persistentes
├── src/
│   ├── guardian.py          # Lógica Core (Watchdog + Threading)
│   ├── config_manager.py    # Leitura/Escrita de JSON
│   ├── cli.py               # Lógica de Negócio do CLI
│   └── cli_ui.py            # Interface Visual (Menu ASCII)
└── README.md                # Documentação

```

## 🗺️ Roadmap

* [x] MVP: Monitoramento e Backup local.
* [x] Interface CLI Interativa.
* [ ] **Sistema de Logs:** Substituir `print` por `logging` rotativo.
* [ ] **Dockerização:** Containerizar a aplicação para deploy fácil.
* [ ] **Integração Cloud:** Upload automático para AWS S3 ou Google Drive.

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

**Desenvolvido por [Tiago Freitas](https://www.linkedin.com/in/tiago-freitas-ferreira/)**
