# Python Global Solution - Projeção do nível do mar

## Descrição

Este projeto calcula o nível futuro do mar com base em uma altura inicial e um aumento anual. O programa projeta o nível do mar para um número definido de anos pelo usuário e exibe os resultados.

## Como Funciona

1. **Entrada do Usuário**: O programa solicita ao usuário que insira o número de anos para os quais deseja projetar o nível do mar.
2. **Cálculo**: Usando a altura inicial (101 mm em 2024) e um aumento anual de 3,4 mm, o programa calcula o nível do mar para cada ano.
3. **Saída**: O programa exibe os níveis projetados do mar para cada ano de forma formatada.

  - **Parâmetros**:
    - `altura_inicial`: A altura inicial do nível do mar em mm.
    - `aumento_anual`: O aumento anual da altura do nível do mar em mm.
    - `anos`: O número de anos para a projeção.
    - `exibir_alturas(alturas)`: Exibe os níveis projetados do mar.
    - `alturas` (list): Uma lista de tuplas contendo o ano e a altura projetada do nível do mar.
  
  - `entrada_anos()`: Solicita ao usuário que insira o número de anos para a projeção, e retorna um inteiro representando o número de anos.

Os dados utilizados são do [Sea Level Portal da NASA](https://sealevel.nasa.gov/faq/8/is-the-rate-of-sea-level-rise-increasing/), segue gráfico abaixo para demonstração.
![Gráfico](https://sealevel.nasa.gov/internal_resources/471)


