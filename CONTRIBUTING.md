# 🤝 Guia de Contribuição

> **Como contribuir efetivamente para projetos de Engenharia de Programação**  
> *Padronizando processos para melhorar colaboração e qualidade*

## 📋 Sumário

- [🎯 Antes de Começar](#-antes-de-começar)
- [🏗️ Estrutura de Projetos](#️-estrutura-de-projetos)
- [💻 Desenvolvimento](#-desenvolvimento)
- [📝 Documentação](#-documentação)
- [🔧 Hardware](#-hardware)
- [🧪 Testes](#-testes)
- [📦 Submissão](#-submissão)
- [📞 Suporte](#-suporte)

## 🎯 Antes de Começar

### **📚 Requisitos**
- ✅ Ser membro da comunidade acadêmica (estudante, professor, pesquisador)
- ✅ Ter conhecimento básico de Git e GitHub
- ✅ Ler e aceitar o [Código de Conduta](CODE_OF_CONDUCT.md)
- ✅ Familiarizar-se com os templates de projeto relevantes

### **🔍 Tipos de Contribuição**
- **📝 Projetos Acadêmicos**: TCCs, projetos de disciplina, pesquisa
- **🔧 Componentes Reutilizáveis**: Bibliotecas, drivers, módulos
- **📚 Documentação**: Tutoriais, guias, exemplos
- **🐛 Correções**: Bug fixes, melhorias, otimizações
- **💡 Propostas**: Novas funcionalidades, ferramentas, processos

## 🏗️ Estrutura de Projetos

### **📁 Hardware Projects**
Use o template [`template-hardware/`](../template-hardware/) para projetos de hardware:

```
projeto-hardware/
├── 📁 components/         # Bibliotecas de componentes
├── 📁 design/             # Design e esquemáticos  
├── 📁 documentation/      # Documentação técnica
├── 📁 firmware/           # Código embarcado
├── 📄 README.md           # Documentação principal
├── 📄 LICENSE.md          # Licença do projeto
└── 📄 CHANGELOG.md        # Histórico de mudanças
```

### **💻 Software Projects**
Use o template [`template-software/`](../template-software/) para projetos de software:

```
projeto-software/
├── 📁 backend/            # Código do servidor
├── 📁 frontend/           # Interface do usuário
├── 📁 mobile/             # Aplicação móvel
├── 📁 database/           # Scripts de banco de dados
├── 📁 docs/               # Documentação
├── 📁 tests/              # Testes automatizados
├── 📄 README.md           # Documentação principal
└── 📄 docker-compose.yml  # Ambiente de desenvolvimento
```

### **📝 Nomenclatura de Repositórios**
Siga o padrão: `<CATEGORIA>-<NOME-DESCRITIVO>`

**Exemplos:**
- `hw-estacao-meteorologica` (projeto de hardware)
- `sw-sistema-monitoramento` (projeto de software)
- `lib-sensor-dht22` (biblioteca reutilizável)
- `docs-tutorial-kicad` (documentação/tutorial)

## 💻 Desenvolvimento

### **🌿 Git Workflow**

1. **Fork** o repositório (se não for colaborador direto)
2. **Clone** para sua máquina local
3. **Crie branch** para sua feature: `git checkout -b feature/nome-da-feature`
4. **Desenvolva** seguindo os padrões estabelecidos
5. **Commit** com mensagens descritivas
6. **Push** para seu fork: `git push origin feature/nome-da-feature`
7. **Abra Pull Request** usando o template apropriado

### **📝 Convenções de Commit**

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Formato
<tipo>[escopo opcional]: <descrição>

# Exemplos
feat(firmware): adiciona suporte ao sensor DHT22
fix(pcb): corrige roteamento da trilha de alimentação
docs(readme): atualiza instruções de instalação
test(unit): adiciona testes para módulo de comunicação
refactor(api): melhora estrutura das rotas
style(format): aplica formatação automática no código
```

### **🎯 Padrões de Código**

**Geral:**
- Use **inglês** para nomes de variáveis, funções e comentários
- Mantenha **consistência** de estilo dentro do projeto
- Adicione **comentários** em português para explicar lógica complexa
- Use **nomes descritivos** e significativos

**Hardware (KiCad/Altium):**
- Nomenclatura clara para nets e componentes
- Organize layers logicamente
- Use grid apropriado para componentes
- Mantenha design rules atualizadas

**Firmware (C/C++):**
```c
// ✅ Bom
const int SENSOR_DHT22_PIN = 2;
float readTemperature(void);

// ❌ Evite
int p = 2;
float t(void);
```

**Python:**
```python
# ✅ Bom
MQTT_BROKER_URL = "localhost"
def calculate_average_temperature(readings):
    """Calcula a temperatura média das leituras."""
    return sum(readings) / len(readings)

# ❌ Evite
url = "localhost"
def calc(r):
    return sum(r)/len(r)
```

## 📝 Documentação

### **📚 README.md Obrigatório**

Todo projeto deve incluir um `README.md` com:

```markdown
# Nome do Projeto

## 📋 Descrição
Breve descrição do projeto e seus objetivos.

## 🎯 Funcionalidades
- Lista das principais funcionalidades
- O que o projeto faz

## 🛠️ Tecnologias
- Hardware: Arduino, ESP32, sensores utilizados
- Software: linguagens, frameworks, bibliotecas

## 📦 Instalação
Instruções passo a passo para setup.

## 🚀 Uso
Exemplos de como usar o projeto.

## 📊 Resultados
Fotos, vídeos, gráficos dos resultados obtidos.

## 👥 Autores
- Nome dos desenvolvedores
- Disciplina/contexto acadêmico

## 📄 Licença
Informação sobre a licença utilizada.
```

### **🔧 Documentação de Hardware**

Para projetos de hardware, inclua:
- **Esquemáticos** em PDF e formato nativo
- **Lista de materiais** (BOM) em formato CSV/Excel
- **Diagramas de blocos** da arquitetura
- **Fotos** do protótipo montado
- **Instrucões de montagem** passo a passo

### **💻 Documentação de Código**

- **Docstrings** em funções importantes
- **Comentários inline** para lógica complexa
- **Arquivos de configuração** documentados
- **APIs** documentadas (se aplicável)

## 🔧 Hardware

### **📐 Design de PCB**

**Regras Gerais:**
- Use **Grid 0.1"** (2.54mm) para componentes through-hole
- Use **Grid 0.05"** (1.27mm) para componentes SMD
- Largura mínima de trilha: **0.2mm** (8 mil)
- Via mínimo: **0.3mm** drill, **0.6mm** pad
- Mantenha **clearance** mínimo de 0.15mm

**Layers:**
- **Top/Bottom**: Sinais prioritários
- **Power**: Planos de alimentação
- **Ground**: Plano de terra contínuo

**Checklist de Design:**
- [ ] Design Rule Check (DRC) sem erros
- [ ] Electrical Rule Check (ERC) sem warnings críticos
- [ ] Todos os componentes possuem footprints
- [ ] Silkscreen legível e informativa
- [ ] Furos de montagem definidos
- [ ] Conectores claramente identificados

### **🔌 Componentes**

**Seleção:**
- Prefira componentes **facilmente disponíveis** no Brasil
- Use **packages padronizados** (0805, 1206 para SMD)
- Inclua **componentes alternativos** na BOM
- Verifique **disponibilidade** e **preço**

**Documentação:**
- Mantenha **datasheets** organizados em `components/datasheets/`
- Crie **bibliotecas customizadas** quando necessário
- Use **modelos 3D** para visualização

## 🧪 Testes

### **🔍 Hardware Testing**

**Testes Básicos:**
- [ ] Continuidade de trilhas
- [ ] Isolação entre nets
- [ ] Níveis de tensão corretos
- [ ] Correntes dentro das especificações
- [ ] Funcionalidade de todos os circuitos

**Documentação de Testes:**
```markdown
## 🧪 Resultados de Testes

### Teste de Alimentação
- **Tensão de entrada**: 12V DC
- **Tensão de saída 5V**: 4.98V ✅
- **Tensão de saída 3.3V**: 3.31V ✅
- **Ripple**: < 50mV ✅

### Teste de Comunicação
- **UART**: 115200 baud, sem erros ✅
- **I2C**: Clock 100kHz, ACK recebido ✅
- **SPI**: Transferência de dados OK ✅
```

### **💻 Software Testing**

**Testes Unitários:**
```python
def test_temperature_reading():
    """Testa leitura de temperatura do sensor."""
    sensor = DHT22(pin=2)
    temp = sensor.read_temperature()
    assert 0 <= temp <= 50  # Faixa esperada
```

**Testes de Integração:**
- Hardware + Software funcionando junto
- Comunicação entre módulos
- Performance sob carga

## 📦 Submissão

### **📋 Checklist Pré-Submissão**

**Geral:**
- [ ] README.md completo e atualizado
- [ ] Licença definida (MIT recomendada para projetos acadêmicos)
- [ ] Changelog atualizado
- [ ] Sem arquivos desnecessários (builds, temporários)
- [ ] .gitignore apropriado configurado

**Hardware:**
- [ ] Esquemáticos em PDF gerados
- [ ] Arquivos Gerber para fabricação (se aplicável)
- [ ] Lista de materiais (BOM) atualizada
- [ ] Fotos do protótipo funcionando

**Software:**
- [ ] Código limpo e comentado
- [ ] Dependências documentadas
- [ ] Testes passando
- [ ] Instruções de instalação testadas

### **🔄 Pull Request**

Use o template apropriado:
- **Project Submission**: Para entrega de projetos
- **Feature Addition**: Para novas funcionalidades
- **Bug Fix**: Para correções

**Informações Obrigatórias:**
- Descrição detalhada das mudanças
- Como testar as alterações
- Screenshots/vídeos (se aplicável)
- Issues relacionadas (se houver)

### **👀 Code Review**

Todos os PRs passam por review:
- **Professores/TAs**: Para projetos acadêmicos
- **Peers**: Para colaborações entre estudantes
- **Mantenedores**: Para contribuições gerais

**Critérios de Aprovação:**
- Código funcional e testado
- Documentação adequada
- Segue padrões estabelecidos
- Não quebra funcionalidades existentes

## 📞 Suporte

### **🆘 Onde Buscar Ajuda**

1. **Documentação**: Consulte READMEs e wikis primeiro
2. **Issues**: Busque problemas similares já reportados
3. **Discussions**: Participe de discussões da comunidade
4. **Discord/Slack**: Canais de comunicação da turma
5. **Professores/TAs**: Para dúvidas específicas da disciplina

### **📝 Reportando Problemas**

Use o template de **Bug Report** incluindo:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. observado
- Ambiente (hardware, SO, versões)
- Logs/screenshots relevantes

### **💡 Sugerindo Melhorias**

Use o template de **Feature Request** com:
- Descrição da funcionalidade desejada
- Justificativa/caso de uso
- Implementação sugerida (se houver)
- Alternativas consideradas

## 🏆 Reconhecimento

Contribuições significativas são reconhecidas através de:
- **Contributors list** nos READMEs
- **Mentions** em apresentações e papers
- **Recommendations** acadêmicas
- **Portfolio credits** para uso profissional

---

## 📚 Recursos Adicionais

- [Git Tutorial Interativo](https://learngitbranching.js.org/)
- [GitHub Skills](https://skills.github.com/)
- [KiCad Documentation](https://docs.kicad.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

---

💡 **Lembre-se**: A qualidade da contribuição é mais importante que a quantidade. Foque em fazer bem feito e documentado!

**Última atualização**: Janeiro 2025
