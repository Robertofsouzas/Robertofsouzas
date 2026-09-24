  <!-- =====================================================================
  GUIA RÁPIDO DE EDIÇÃO (comentários HTML não aparecem no GitHub)
  - Linhas marcadas com "CONFIRMAR" têm descrição inferida do nome do repositório.
    Abra o repo, ajuste a frase para o que ele realmente faz e apague o comentário.
  - Se o nome de algum repositório estiver diferente, corrija o link.
===================================================================== -->

<h1 align="center">Roberto Souza</h1>

<p align="center">
  <b>Analytics Engineer</b> · Pipelines de dados, modelagem dimensional e BI ponta a ponta<br>
  Salvador, Bahia 🇧🇷
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/roberto-fonseca-de-souza/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://rfstech.vercel.app/"><img src="https://img.shields.io/badge/Portf%C3%B3lio%20Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Portfólio Power BI"></a>
  <a href="mailto:Robertofonsecas83@gmail.com"><img src="https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
</p>

---

## 👋 Sobre mim

Trabalho com dados desde 2021, construindo o caminho completo entre o dado bruto e a decisão: **extração, pipelines ETL/ELT, modelagem dimensional (Star Schema), Data Warehouse / Lakehouse e dashboards executivos**.

- 🏢 Já atuei com dados de **Finanças, RH, Suprimentos, Operações e Engenharia**.
- 🧱 Meu foco hoje é **Analytics Engineering**: dados confiáveis, bem modelados e documentados, prontos para virar análise.
- ☁️ Estou aprofundando **Microsoft Fabric** (Lakehouse, OneLake, pipelines) e preparando a certificação **DP-600**.
- 🤝 Aberto a oportunidades como Analytics Engineer e a projetos de dados, automação e IA (também pela **RFStechs**).

---

## 🛠️ Stack

| Camada | Ferramentas |
|---|---|
| **Consumo e BI** | ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black) ![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat-square) |
| **Modelagem e armazenamento** | ![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white) ![Microsoft Fabric](https://img.shields.io/badge/Microsoft%20Fabric-117865?style=flat-square&logo=microsoft&logoColor=white) Star Schema · Data Warehouse · Lakehouse |
| **Processamento e ETL/ELT** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) Apache Hop / Pentaho PDI · Data Factory |
| **Versionamento** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) |

### 💻 Linguagens que mais utilizo

| Linguagem | Onde eu uso |
|---|---|
| **SQL** | Consultas analíticas, views, stored procedures, modelagem de tabelas fato e dimensão |
| **DAX** | Medidas e métricas de negócio em Power BI, otimização de modelos semânticos |
| **Python** | Tratamento e limpeza de dados, automações, análises exploratórias em notebooks |
| **PySpark** | Transformações em Lakehouse (Fabric), processamento em maior volume |

---

## 🏗️ Arquitetura de referência

Fluxo que costumo seguir nos projetos: fontes → ingestão → camadas de transformação → modelo dimensional → consumo em BI.

<p align="center">
  <img src="arquitetura-dados%20(1).svg" alt="Arquitetura de engenharia de dados" width="90%">
</p>

---

## 🚀 Projetos

> Todos os projetos abaixo são **projetos de estudo e portfólio**, criados para praticar ferramentas e padrões que uso e quero aprofundar na engenharia de dados.

### ⭐ Projeto em destaque: [Brasileirão 360](https://github.com/Robertofsouzas/brasileirao360)

Plataforma analítica *end-to-end* sobre o Campeonato Brasileiro Série A: da ingestão de APIs esportivas ao dashboard interativo.

- 🏗️ **Arquitetura Medalhão** (Bronze → Silver → Gold) com **Star Schema** em PostgreSQL / Supabase
- 📑 **Data Contract** documentando esquemas de tabelas e definições de métricas
- 🎲 **Modelo de Poisson + 10.000 simulações de Monte Carlo** para projetar título, vagas e rebaixamento
- 📊 **Visualização espacial** (D3.js e deck.gl): mapas de calor e de chutes por atleta
- 🧰 **Stack:** Python · Pandas · NumPy · SQL (Supabase/PostgreSQL) · D3.js · deck.gl

<!-- CONFIRMAR: se publicar no GitHub Pages, coloque aqui o link "Ver demo ao vivo" -->

### ⚙️ Engenharia de Dados

| Projeto | O que faz | Tecnologias |
|---|---|---|
| [**Soluções Fabric**](https://github.com/Robertofsouzas/solucoes-fabric) | Projeto prático em Microsoft Fabric com transformações sobre dados de vendas, em paralelo aos estudos para a DP-600 | Fabric · PySpark · SQL <!-- CONFIRMAR: camadas (bronze/silver/gold?) e o que o pipeline entrega --> |
| [**Modern Data Stack**](https://github.com/Robertofsouzas/modern-data-stack) | Ambiente de estudo de uma stack de dados moderna, da ingestão à transformação | Shell · ELT <!-- CONFIRMAR: ferramentas usadas (Airbyte, dbt, orquestrador?) --> |
| [**Relatório Financeiro (Fabric + Git)**](https://github.com/Robertofsouzas/Git-fabric) | Relatório financeiro no Fabric com versionamento via Git | Fabric · Power BI · Git <!-- CONFIRMAR --> |
| [**Consolidação de Faturas**](https://github.com/Robertofsouzas/ConsolidacaoDeFaturas) | Automação para consolidar faturas em uma base única e padronizada | Python <!-- CONFIRMAR: formato de entrada/saída --> |
| [**Pré-processamento de dados do MongoDB**](https://github.com/Robertofsouzas/Pre-Processamento-de-dados-de-texto-Extraido-do-Mongodb) | Extração e pré-processamento de dados de texto vindos do MongoDB | Python · MongoDB · Jupyter <!-- CONFIRMAR --> |

### 📊 Análise de Dados e IA

| Projeto | O que faz | Tecnologias |
|---|---|---|
| [**Agente de Vendas com IA**](https://github.com/Robertofsouzas/ai-agente-vendas) | Agente de IA aplicado a um fluxo de vendas | Python · IA <!-- CONFIRMAR: qual modelo/framework e qual tarefa o agente resolve --> |
| [**Análise de Cesta de Compras**](https://github.com/Robertofsouzas/Analise_Cesta_de_Compras) | Análise de padrões de compra (produtos comprados juntos) | Python · Jupyter <!-- CONFIRMAR: técnica usada (regras de associação?) --> |
| [**Análise e Limpeza de Dados**](https://github.com/Robertofsouzas/Analise-e-Limpeza-de-Dados-) | Etapas de exploração, tratamento e limpeza de um conjunto de dados | Python · Jupyter <!-- CONFIRMAR --> |
| [**Healthcare Dataset**](https://github.com/Robertofsouzas/Healthcare-Dataset) | Análise de um dataset público da área da saúde | Python <!-- CONFIRMAR --> |
| [**Loja Vrinda**](https://github.com/Robertofsouzas/LojaVrinda/tree/main) | Análise de dados de vendas de uma loja | <!-- CONFIRMAR: Power BI ou Python? --> |

### 📈 Dashboards em Power BI

Meus dashboards e painéis executivos estão no portfólio:
👉 **[Portifólio de projetos BI](https://rfstech.vercel.app/)**

---

## 🎓 Formação e certificações

- 🔄 **DP-600** (Fabric Analytics Engineer Associate): em estudo
- 🔄 **PL-300** (Power BI Data Analyst Associate): em preparação

---

## 📫 Contato

- LinkedIn: [roberto-fonseca-de-souza](https://www.linkedin.com/in/roberto-fonseca-de-souza/)
- E-mail: Robertofonsecas83@gmail.com

