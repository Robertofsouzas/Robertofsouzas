  

<h1 align="left">Hi <img src="https://raw.githubusercontent.com/kaueMarques/kaueMarques/master/hi.gif" height="30px">, I'm  Roberto souza</h1> <p align="left"> <img src="https://komarev.com/ghpvc/?username=Robertofsouzas&color=blue" alt="Profile views" />
</p>

# 🔥  -Analyst Engineer
 
🎯 **Objetivo**  
Este portfólio reúne projetos pessoais de **Análise de Dados** e **Engenharia de Dados**, demonstrando minha capacidade de resolver desafios de negócios por meio de análises inteligentes e soluções escaláveis.

## 🚀 **Sobre Mim**
Sou um apaixonado por **dados** e **tecnologia**, com experiência em Análise de Dados e  Engenharia de Dados. Meu foco está em criar soluções que transformem dados em **insights acionáveis**, utilizando as melhores práticas de engenharia e arquitetura de dados.

---

## 📊 **Arquitetura de Engenharia de Dados**

<svg width="1000" height="400" viewBox="0 0 1000 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background gradient -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a4d5c;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d2d35;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="bronzeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#d4a574;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#a0826d;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="silverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e8e8e8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#c0c0c0;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ffd700;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#daa520;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Main background -->
  <rect width="1000" height="400" fill="url(#bgGradient)"/>
  
  <!-- LEFT SECTION - Data Sources -->
  <g id="left-section">
    <path d="M 20 50 L 120 50 L 140 100 L 140 350 L 20 350 Z" fill="#0f3a42" opacity="0.6"/>
    <text x="40" y="100" font-size="16" font-weight="bold" fill="#e0f2f1">📊 Data</text>
    <text x="40" y="125" font-size="16" font-weight="bold" fill="#e0f2f1">Sources</text>
    
    <text x="40" y="170" font-size="13" fill="#b2dfdb">🔹 Kafka</text>
    <text x="40" y="195" font-size="13" fill="#b2dfdb">🔹 Kinesis</text>
    <text x="40" y="220" font-size="13" fill="#b2dfdb">🔹 Data Lake</text>
    <text x="40" y="245" font-size="13" fill="#b2dfdb">🔹 CDC</text>
    <text x="40" y="270" font-size="13" fill="#b2dfdb">🔹 APIs</text>
    <text x="40" y="295" font-size="13" fill="#b2dfdb">🔹 Spark</text>
  </g>
  
  <!-- BRONZE LAYER -->
  <g id="bronze">
    <!-- Card background -->
    <rect x="200" y="80" width="180" height="240" fill="#f5f5f0" rx="8" stroke="#333" stroke-width="2"/>
    
    <!-- Title -->
    <text x="290" y="115" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">BRONZE</text>
    
    <!-- Database cylinder -->
    <ellipse cx="290" cy="160" rx="45" ry="18" fill="url(#bronzeGrad)" stroke="#333" stroke-width="1.5"/>
    <rect x="245" y="160" width="90" height="50" fill="#d4a574" stroke="#333" stroke-width="1.5"/>
    <ellipse cx="290" cy="210" rx="45" ry="18" fill="#a0826d" stroke="#333" stroke-width="1.5"/>
    
    <!-- Description -->
    <text x="290" y="250" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">Raw Ingestion</text>
    <text x="290" y="265" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">and History</text>
  </g>
  
  <!-- Arrow Bronze to Silver -->
  <g id="arrow1">
    <line x1="380" y1="200" x2="420" y2="200" stroke="#888" stroke-width="2" stroke-dasharray="5,5"/>
    <text x="400" y="190" font-size="10" fill="#999" text-anchor="middle">→</text>
  </g>
  
  <!-- SILVER LAYER -->
  <g id="silver">
    <!-- Card background -->
    <rect x="430" y="80" width="180" height="240" fill="#f5f5f0" rx="8" stroke="#333" stroke-width="2"/>
    
    <!-- Title -->
    <text x="520" y="115" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">SILVER</text>
    
    <!-- Database cylinder -->
    <ellipse cx="520" cy="160" rx="45" ry="18" fill="url(#silverGrad)" stroke="#333" stroke-width="1.5"/>
    <rect x="475" y="160" width="90" height="50" fill="#e8e8e8" stroke="#333" stroke-width="1.5"/>
    <ellipse cx="520" cy="210" rx="45" ry="18" fill="#c0c0c0" stroke="#333" stroke-width="1.5"/>
    
    <!-- Description -->
    <text x="520" y="250" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">Filtered, Cleaned,</text>
    <text x="520" y="265" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">Augmented</text>
  </g>
  
  <!-- Arrow Silver to Gold -->
  <g id="arrow2">
    <line x1="610" y1="200" x2="650" y2="200" stroke="#888" stroke-width="2" stroke-dasharray="5,5"/>
    <text x="630" y="190" font-size="10" fill="#999" text-anchor="middle">→</text>
  </g>
  
  <!-- GOLD LAYER -->
  <g id="gold">
    <!-- Card background -->
    <rect x="660" y="80" width="180" height="240" fill="#f5f5f0" rx="8" stroke="#333" stroke-width="2"/>
    
    <!-- Title -->
    <text x="750" y="115" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">GOLD</text>
    
    <!-- Database cylinder -->
    <ellipse cx="750" cy="160" rx="45" ry="18" fill="url(#goldGrad)" stroke="#333" stroke-width="1.5"/>
    <rect x="705" y="160" width="90" height="50" fill="#ffd700" stroke="#333" stroke-width="1.5"/>
    <ellipse cx="750" cy="210" rx="45" ry="18" fill="#daa520" stroke="#333" stroke-width="1.5"/>
    
    <!-- Description -->
    <text x="750" y="250" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">Business-level</text>
    <text x="750" y="265" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">Aggregation</text>
  </g>
  
  <!-- RIGHT SECTION - Outputs -->
  <g id="right-section">
    <path d="M 880 50 L 980 50 L 980 350 L 860 350 L 880 100 Z" fill="#0f3a42" opacity="0.6"/>
    <text x="895" y="100" font-size="16" font-weight="bold" fill="#e0f2f1">📈 Output</text>
    <text x="895" y="125" font-size="16" font-weight="bold" fill="#e0f2f1">Layers</text>
    
    <text x="885" y="170" font-size="13" fill="#b2dfdb">📊 Streaming</text>
    <text x="885" y="185" font-size="13" fill="#b2dfdb">Analytics</text>
    <text x="885" y="210" font-size="13" fill="#b2dfdb">📉 BI &</text>
    <text x="885" y="225" font-size="13" fill="#b2dfdb">Reporting</text>
    <text x="885" y="250" font-size="13" fill="#b2dfdb">🤖 ML Models</text>
    <text x="885" y="275" font-size="13" fill="#b2dfdb">& ML Ops</text>
  </g>
  
  <!-- QUALITY ARROW at bottom -->
  <g id="quality-arrow">
    <defs>
      <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
        <polygon points="0 0, 10 3, 0 6" fill="#10b981" />
      </marker>
    </defs>
    <line x1="200" y1="340" x2="880" y2="340" stroke="#10b981" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="540" y="365" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">QUALITY IMPROVEMENT</text>
  </g>
</svg>

---

## 💡 **Habilidades**

### **🔍 Análise de Dados**  
- **Power BI**: Desenvolvimento de dashboards interativos.  
- **SQL Server e NoSQL (MongoDB)**: Consultas, manipulação e otimização de bancos de dados.  
- **Pentaho**: Soluções ETL para integrar dados.  
- **SQL**: Criação de consultas avançadas e modelagem de dados.  

### **⚙️ Engenharia de Dados**  
- **Databricks**: Processamento e análise de grandes volumes de dados.  
- **Azure Data Factory**: Integração e automação de pipelines de dados.  
- **PySpark**: Processamento distribuído para tarefas de ETL robustas. 
- **Microsoft Fabric**:  Automatiza e otimiza tarefas de processamento e análise de dados, tornando os fluxos de trabalho mais eficientes e escaláveis.
 
## 🛠 &nbsp;Projetos
 - 🔭 Projeto [Projeto Soluões Fabric](https://github.com/Robertofsouzas/solucoes-fabric)
 - 🔭 Projeto [Consolidação de faturas](https://github.com/Robertofsouzas/ConsolidacaoDeFaturas)
 - 🔭 Projeto [Relatório_Financeiro](https://github.com/Robertofsouzas/Git-fabric)
 - 🔭 Projeto [LojaVrinda](https://github.com/Robertofsouzas/LojaVrinda/tree/main)
 - 🔭 Projeto [Healthcare-Dataset](https://github.com/Robertofsouzas/Healthcare-Dataset)
 - 🔭 Projeto [Analise de cesta de Compra](https://github.com/Robertofsouzas/Analise_Cesta_de_Compras)
 - 🔭 Projeto [Pre-Processamento de dados no Mongodb](https://github.com/Robertofsouzas/Pre-Processamento-de-dados-de-texto-Extraido-do-Mongodb)
 - 🔭 Projeto [Análise e Limpeza dos dados](https://github.com/Robertofsouzas/Analise-e-Limpeza-de-Dados-)

- 🔭 Projeto [Modern data stack](https://github.com/Robertofsouzas/modern-data-stack)

- 🤝 Atualmente estou trabalhando nesse projeto [Previsão de vendas na loja](https://github.com/Robertofsouzas/DatascienceEmproducao)

- 👨‍💻 Projetos em Power BI [Power BI](https://sites.google.com/view/portfoliorobertosouza/home)

- 📫 How to reach me **Robertofonsecas83@gmail.com**



<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://www.databricks.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/databricks/databricks-icon.svg" alt="databricks" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="40" height="40"/> </a> <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a>
</p>


<br><br>

## ⚙️ &nbsp;GitHub Analytics

<p align="left">
<img width="530em" src="https://github-readme-stats.vercel.app/api?username=robertofsouzas&show_icons=true&theme=vision-friendly-dark" alt="maykbrito's stats"/>
<img width="530em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=robertofsouzas&layout=compact&theme=vision-friendly-dark" alt="maykbrito's most languages"/>
</p>

<br><br>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/roberto-fonseca-de-souza/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/roberto-fonseca-de-souza/" height="30" width="40" /></a>
<a href="https://instagram.com/robertosouzas" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="robertosouzas" height="30" width="40" /></a>
</p>

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5571986072596)

