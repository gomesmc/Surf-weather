 ## Surf Weather

Aloha! Este é um aplicativo em Python que verifica as condições meteorológicas para surfar em uma cidade específica. 
Essa apicação usa a API OpenWeatherMap para obter dados meteorológicos e avalia se é seguro surfar com base na temperatura, velocidade do vento, visibilidade e cobertura de nuvens.

## Funcionalidades

- Solicita ao usuário o nome de uma cidade.
- Faz uma solicitação à API OpenWeatherMap para obter dados meteorológicos.
- Exibe as condições meteorológicas atuais da cidade.
- Avalia se é seguro surfar com base nas condições meteorológicas.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests`

## Instalação

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/SEU_USUARIO/surf-weather-checker.git
    cd surf-weather-checker
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install requests
    ```

4. Obtenha uma chave de API do OpenWeatherMap [aqui](https://home.openweathermap.org/users/sign_up).

5. Adicione sua chave de API no código, substituindo `'YOUR_API_KEY'` pela sua chave.

## Uso

Execute o script:
```sh
python aloha.py
