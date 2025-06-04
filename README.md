# sistema-notas
Sistema simples em Python para calcular médias e classificar alunos. Ideal para quem está começando! #python #iniciante #educaçâo

# 📚 Sistema de Notas - Console Python

Este é um sistema simples de gerenciamento de notas de alunos feito em Python. O programa coleta o nome de cada aluno, suas três notas e calcula a média final. Com base na média, o aluno será classificado como:

- ✅ **Aprovado**
- 🟡 **Recuperação**
- ❌ **Reprovado**

---

## 🚀 Funcionalidades

- Entrada de dados com validações (nome e notas)
- Cálculo de média de três notas
- Classificação automática dos alunos
- Interface de terminal interativa com o pacote `InquirerPy`
- Opção de cancelar operações ou tentar novamente em caso de erro
- Exibição de um relatório final com totais e listas de alunos por categoria

---

## 🛠️ Tecnologias usadas

- Python 3
- [InquirerPy](https://github.com/kazhala/InquirerPy) (para inputs mais amigáveis no terminal)
- Módulos padrões: `os`, `time`

---

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/sistema-notas.git
cd sistema-notas
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install InquirerPy
```

---

## ▶️ Como usar

Execute o programa no terminal com:

```bash
python sistema_notas.py
```

Você será guiado por uma interface simples para inserir:
- A quantidade de alunos
- Nome de cada aluno
- Três notas (de 0 a 10)

Ao final, um resumo será exibido com totais e a lista de alunos classificados.

---

## 📊 Critérios de Avaliação

| Média Final | Situação       |
|-------------|----------------|
| ≥ 5.0       | ✅ Aprovado     |
| 3.0 - 4.9   | 🟡 Recuperação  |
| < 3.0       | ❌ Reprovado    |

---

## 📌 Observações

- O nome do aluno deve conter apenas letras.
- As notas devem estar entre 0 e 10.
- É possível cancelar ou repetir a operação em caso de erro de entrada.

---



Desenvolvido por: Reinan Carvalho (@CarvalhoReinan)✍️
