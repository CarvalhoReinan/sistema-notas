# sistema-notas
Sistema simples em Python para calcular médias e classificar alunos. Ideal para quem está começando! #python #iniciante #educaçâo

# 📚 Sistema de Notas - Console Python

Este é um sistema simples de gerenciamento de notas de alunos feito em Python. O programa coleta o nome de cada aluno, suas três notas e calcula a média final. Com base na média, o aluno será classificado como:

✅ Aprovado  
🟡 Recuperação  
❌ Reprovado

## 🚀 Funcionalidades

- Entrada de dados com validações (nome e notas)
- Cálculo de média de três notas
- Classificação automática dos alunos
- Interface de terminal interativa com o pacote `InquirerPy`
- Opção de cancelar operações ou tentar novamente em caso de erro
- Exibição de um relatório final com totais e listas de alunos por categoria

## 🛠️ Tecnologias usadas

- Python 3
- [InquirerPy](https://github.com/kazhala/InquirerPy)
- Módulos padrões: os, time

## 📦 Instalação

```bash
git clone https://github.com/seuusuario/STUDENT-MANAGER.git
cd STUDENT-MANAGER
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install InquirerPy
python student_manager/main.py
```

## 📊 Critérios de Avaliação

| Média Final | Situação       |
|-------------|----------------|
| ≥ 5.0       | ✅ Aprovado     |
| 3.0 - 4.9   | 🟡 Recuperação  |
| < 3.0       | ❌ Reprovado    |

## 📌 Observações

- O nome do aluno deve conter apenas letras.
- As notas devem estar entre 0 e 10.
- É possível cancelar ou repetir a operação em caso de erro de entrada.

---


Desenvolvido por: Reinan Carvalho (CarvalhoReinan)✍️
