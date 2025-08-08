# 🔒 Política de Segurança

## 🎯 Visão Geral

A segurança é uma prioridade fundamental em projetos de Engenharia de Programação, especialmente quando lidamos com sistemas embarcados, IoT e infraestrutura crítica. Este documento estabelece diretrizes e procedimentos para manter nossos projetos acadêmicos seguros e responsáveis.

## 📋 Escopo

Esta política aplica-se a:
- **Repositórios** da organização acadêmica
- **Projetos** de hardware e software
- **Sistemas embarcados** e dispositivos IoT
- **Infraestrutura** de desenvolvimento e teste
- **Dados** coletados em projetos de pesquisa

## 🛡️ Versões Suportadas

Como organização acadêmica, fornecemos suporte de segurança para:

| Categoria | Versão/Período | Suporte de Segurança |
| --------- | -------------- | -------------------- |
| **Templates atuais** | 2024.2 - atual | ✅ Suporte completo |
| **Templates anteriores** | 2023.1 - 2024.1 | ⚠️ Correções críticas apenas |
| **Projetos ativos** | Semestre atual | ✅ Suporte completo |
| **Projetos anteriores** | Até 2 semestres | ⚠️ Sob demanda |
| **Projetos legados** | > 2 semestres | ❌ Sem suporte |

## 🚨 Reportando Vulnerabilidades

### **📧 Canal Principal**
Para reportar vulnerabilidades de segurança, use **APENAS** os canais seguros:

- **Email criptografado**: [security@enc.ara.ufsc.br](mailto:security@enc.ara.ufsc.br)
- **Formulário confidencial**: [Link para formulário interno da instituição]
- **Conversa presencial**: Com coordenação ou professores responsáveis

### **⚠️ NÃO Use Para Vulnerabilidades**
- ❌ Issues públicas no GitHub
- ❌ Pull Requests
- ❌ Discussões públicas
- ❌ Redes sociais
- ❌ Chats públicos da turma

### **📋 Informações Necessárias**

Ao reportar uma vulnerabilidade, inclua:

```markdown
## Informações da Vulnerabilidade

### Identificação
- **Repositório/Projeto**: [nome do projeto]
- **Arquivo(s) afetado(s)**: [caminhos dos arquivos]
- **Tipo de vulnerabilidade**: [categoria]
- **Severidade estimada**: [baixa/média/alta/crítica]

### Descrição
- **Resumo**: [descrição concisa do problema]
- **Impacto**: [consequências potenciais]
- **Cenário de exploração**: [como pode ser explorada]

### Ambiente
- **Hardware**: [plataforma, componentes]
- **Software**: [SO, versões, dependências]
- **Rede**: [configuração de rede relevante]

### Evidências
- **Steps to reproduce**: [passos para reproduzir]
- **Logs**: [anexar logs relevantes]
- **Screenshots**: [se aplicável]
- **Código de prova**: [se disponível]

### Propostas
- **Correção sugerida**: [se houver]
- **Mitigação temporária**: [workarounds]
- **Referências**: [CVEs, artigos, etc.]
```

### **⏱️ Tempo de Resposta**

| Severidade | Primeira Resposta | Correção Target |
| ---------- | ----------------- | --------------- |
| **Crítica** | 24 horas | 7 dias |
| **Alta** | 72 horas | 30 dias |
| **Média** | 1 semana | 90 dias |
| **Baixa** | 2 semanas | Próximo release |

## 🔐 Diretrizes de Segurança

### **💻 Desenvolvimento Seguro**

#### **Código Fonte**
- ✅ **Não committar** credenciais, senhas ou chaves
- ✅ **Usar variáveis de ambiente** para dados sensíveis
- ✅ **Validar entradas** de usuário e sensores
- ✅ **Implementar logs** de segurança apropriados
- ✅ **Seguir** práticas de coding seguro da linguagem

#### **Hardware**
- ✅ **Proteger interfaces** de debug (JTAG, UART)
- ✅ **Implementar** boot seguro quando possível
- ✅ **Criptografar** comunicações wireless
- ✅ **Validar** firmware antes da atualização
- ✅ **Isolar** circuitos críticos

#### **Comunicação**
- ✅ **Usar TLS/SSL** para comunicações web
- ✅ **Implementar** autenticação mútua
- ✅ **Criptografar** dados sensíveis
- ✅ **Validar** certificados e chaves
- ✅ **Implementar** rate limiting

### **🗂️ Gestão de Dados**

#### **Dados Pessoais (LGPD)**
- ✅ **Minimizar** coleta de dados pessoais
- ✅ **Obter consentimento** explícito quando necessário
- ✅ **Criptografar** dados pessoais armazenados
- ✅ **Implementar** direito ao esquecimento
- ✅ **Documentar** fluxo de dados pessoais

#### **Dados de Pesquisa**
- ✅ **Anonimizar** dados quando possível
- ✅ **Usar** armazenamento institucional seguro
- ✅ **Implementar** backup e versionamento
- ✅ **Controlar** acesso baseado em necessidade
- ✅ **Documentar** origem e tratamento dos dados

### **🌐 Segurança de Infraestrutura**

#### **Servidores e Cloud**
- ✅ **Usar** infraestrutura institucional quando possível
- ✅ **Configurar** firewalls apropriadamente
- ✅ **Manter** sistemas atualizados
- ✅ **Implementar** monitoramento de segurança
- ✅ **Fazer** backup regular e seguro

#### **Dispositivos IoT**
- ✅ **Trocar** senhas padrão
- ✅ **Segmentar** rede de dispositivos
- ✅ **Implementar** atualizações automáticas
- ✅ **Monitorar** tráfego anômalo
- ✅ **Documentar** todos os dispositivos

## 🚫 Vulnerabilidades Comuns

### **🔴 Críticas - Ação Imediata Necessária**

#### **Hardware**
- **Exposição de interfaces de debug** em produção
- **Firmware não criptografado** em flash externa
- **Backdoors** em código de produção
- **Bypass de autenticação** via hardware
- **Acesso root** sem proteção

#### **Software**
- **Injeção de código** (SQL, command injection)
- **Buffer overflows** não tratados
- **Exposição de credenciais** em código/logs
- **Autenticação quebrada** ou inexistente
- **Execução remota de código** não autorizada

### **🟠 Altas - Correção Urgente**

#### **Comunicação**
- **Transmissão não criptografada** de dados sensíveis
- **Certificados** inválidos ou expirados
- **Protocolos** depreciados (WEP, SSL < 3.0)
- **Man-in-the-middle** attacks possíveis
- **Replay attacks** não prevenidos

#### **Configuração**
- **Permissões excessivas** de usuário/sistema
- **Serviços desnecessários** expostos
- **Configurações padrão** não alteradas
- **Logs** com informações sensíveis
- **Backup** não criptografado

### **🟡 Médias - Correção Planejada**

#### **Validação**
- **Validação insuficiente** de entrada
- **Rate limiting** inadequado
- **Error messages** reveladores
- **Path traversal** vulnerabilities
- **File upload** restrictions inadequadas

#### **Monitoramento**
- **Logs** insuficientes de segurança
- **Alertas** não configurados
- **Monitoring** de integridade ausente
- **Audit trail** incompleto
- **Incident response** não definido

## 🛠️ Ferramentas Recomendadas

### **🔍 Análise de Segurança**

#### **Código**
- **Bandit** (Python security linting)
- **ESLint security plugins** (JavaScript)
- **Cppcheck** (C/C++ static analysis)
- **SonarQube** (múltiplas linguagens)
- **GitHub Security Alerts** (dependências)

#### **Hardware**
- **Hardware Security Modules** (HSM) para chaves
- **Secure boot** implementations
- **JTAG protection** techniques
- **Side-channel** analysis tools
- **Firmware** analysis tools

#### **Infraestrutura**
- **Nmap** (network scanning)
- **OpenVAS** (vulnerability scanning)
- **Wireshark** (traffic analysis)
- **Metasploit** (penetration testing)
- **Docker security** scanning

### **🔐 Criptografia**

#### **Recomendações Atuais**
- **AES-256** para criptografia simétrica
- **RSA-4096** ou **ECC P-384** para assimétrica
- **SHA-3** ou **SHA-256** para hashing
- **PBKDF2** ou **Argon2** para senhas
- **TLS 1.3** para comunicações

#### **⚠️ Deprecados - Não Usar**
- ❌ **DES, 3DES** (cifras fracas)
- ❌ **MD5, SHA-1** (hashes quebrados)
- ❌ **RSA < 2048** bits
- ❌ **SSL < 3.0, TLS < 1.2**
- ❌ **WEP, WPA** (usar WPA3)

## 📚 Recursos Educacionais

### **🎓 Cursos e Certificações**
- **OWASP Top 10** (vulnerabilidades web)
- **IoT Security** guidelines (NIST, ENISA)
- **Embedded Security** courses
- **Hardware Security** modules
- **Secure Coding** practices

### **📖 Documentação**
- [OWASP IoT Security Verification Standard](https://owasp.org/www-project-iot-security-verification-standard/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Hardware Security Guidelines](https://csrc.nist.gov/publications/detail/sp/800-193/final)
- [Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

### **🛠️ Labs e Práticas**
- **WebGoat** (vulnerabilidades web)
- **Damn Vulnerable IoT Device** (IoT security)
- **Hardware Hacking Labs**
- **Capture The Flag** (CTF) events
- **Bug Bounty** programs educacionais

## 📞 Contatos de Emergência

### **🚨 Incidentes Críticos**
- **Coordenação do Curso**: [coordenacao.enc@contato.ufsc.br](mailto:coordenacao.enc@contato.ufsc.br)
- **TI Institucional**: [ti@ufsc.br](mailto:ti@ufsc.br)
- **CERT.br**: Para incidentes de escala nacional
- **Polícia Civil**: Para crimes cibernéticos

### **📋 Escalação**
1. **Professor responsável** da disciplina
2. **Coordenação** do curso
3. **TI** da instituição
4. **Autoridades** competentes (se necessário)

## 🏆 Reconhecimento

### **🎖️ Hall of Fame**
Pesquisadores que reportam vulnerabilidades de forma responsável são reconhecidos em:
- **Lista pública** de contribuidores de segurança
- **Certificados** de reconhecimento
- **Cartas de recomendação** acadêmica
- **Apresentações** em eventos da instituição

### **🎁 Recompensas Acadêmicas**
- **Créditos extras** em disciplinas relevantes
- **Oportunidades** de pesquisa em segurança
- **Mentoria** para projetos de TCC
- **Referências** para estágios e empregos

---

## 📝 Atualizações da Política

Esta política é revisada **semestralmente** e atualizada conforme:
- **Novas ameaças** identificadas
- **Mudanças** na legislação
- **Feedback** da comunidade
- **Melhores práticas** da indústria

**Versão**: 1.0  
**Última atualização**: Janeiro 2025  
**Próxima revisão**: Julho 2025  
**Aprovado por**: Coordenação do Curso de Engenharia de Computação - UFSC Araranguá
