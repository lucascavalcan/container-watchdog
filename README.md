# Container Watchdog

## Descrição

O **Container Watchdog** é uma ferramenta que monitora eventos de contêineres Docker e envia notificações para um canal do Discord quando um contêiner é encerrado. Ele utiliza o Docker Python SDK para ouvir eventos e a API de Webhook do Discord para enviar mensagens de notificação.

## Funcionalidades

- Monitora eventos de encerramento de contêineres Docker.
- Envia uma mensagem para um webhook do Discord com informações sobre o contêiner encerrado.
- Configurável com diferentes URLs de webhook e parâmetros de eventos.

## Requisitos

- **Python 3.x**: A versão 3 do Python é necessária para executar o script.
- **Docker Python SDK**: Biblioteca para interagir com o Docker.
- **Requests**: Biblioteca para enviar solicitações HTTP.

## Instalação

1. **Clone o Repositório**

   Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/<seu-usuario>/container-watchdog.git
   cd container-watchdog
2. **Instale as Dependências**

   Instale as bibliotecas necessárias usando o pip:
   ```bash
   pip install docker requests
## Configuração

1. **Configure o Webhook do Discord**

   Obtenha a URL do webhook do Discord e substitua no script Python. Edite a linha no script watchdog.py com a URL do seu webhook::
   ```bash
   webhook_url = "https://discord.com/api/webhooks/SEU_ID/SEU_TOKEN"
2. **Ajuste a URL do Docker Daemon**

   Certifique-se de que o Docker daemon esteja acessível na URL especificada no script Python. Se o Docker estiver configurado para escutar em outro endereço ou porta, ajuste a linha abaixo no script:
   ```bash
   client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
## Uso

**Para iniciar o monitoramento, execute o script Python:**

   ```bash
python events.py