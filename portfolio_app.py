# coding: utf-8
import streamlit as st
import pandas as pd
import altair as alt

# --- INSTRUÇÕES PARA EXECUTAR ---
# (Instruções de execução omitidas para brevidade, são as mesmas de antes)
# ---------------------------------------------------------


# --- INÍCIO DO SEU APP PORTFÓLIO ---

st.set_page_config(
    page_title="Letícia Vieira - Portfolio",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- SEÇÃO DE TÍTULO (IMAGEM E NOME LADO A LADO) ---
# Substituímos o st.markdown centralizado por colunas
col1, col2 = st.columns(
    [1, 3],  # Proporção: 1 parte para a imagem, 3 para o texto
    vertical_alignment="center" # Alinha os conteúdos verticalmente
)

##with col1:
    # --- COMO ADICIONAR SUA FOTO ---
    # 1. (Recomendado) Crie uma pasta chamada "assets" no mesmo local do seu script.
    # 2. Coloque sua foto (ex: "foto_perfil.png") dentro dessa pasta "assets".
    # 3. Descomente a linha de código abaixo (remova o '#') e apague o st.image() do "placehold.co".
    
    ##st.image("assets/foto_perfil.jpg", width=150)
    

with col2:
    # Usamos HTML para controlar melhor o espaçamento entre o H1 e H2
    st.markdown(
        """
        <div style='line-height: 1.5;'>
            <h1 style='margin-bottom: 0px; color:#FF8C00;'>LETÍCIA VIEIRA</h1>
            <h2 style='margin-top: 0px; font-weight: 300;'>Analytics Engineer</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("---")

# --- NAVEGAÇÃO POR ABAS (SUBSTITUI DO MENU LATERAL) ---
tab_sobre_mim, tab_trajetoria, tab_projetos, tab_falecomigo = st.tabs(["👋 Sobre Mim", "✨ Minha Trajetória", "🚀 Meus Projetos"," 📱 Fale comigo"])

# --- CONTEÚDO DA ABA "SOBRE MIM" ---
with tab_sobre_mim:
    ##st.header("Bem-vindo ao meu portfólio!")
    st.markdown("""
    Olá! Seja bem vindo (a) ao espaço que eu criei para compartilhar um pouco da minha trajetória e principais projetos. 
                
    Sou formada em Ciências Contábeis pela Universidade Federal de Santa Catarina (UFSC) e  MBA em Gestão Estratégica em Finanças pela PUC Minas. Dediquei parte do meu tempo ao mundo financeiro e contábil. Passado isso, decidi migrar para a área de tecnologia. Conectando meus conhecimentos financeiros com a paixão por tecnologia e automatização. Com previsão para conclusão em outubro de 2025, atualmente estou cursando uma pós graduação em Engenharia de IA pela Data Science Academy (DSA).
                
    Meu objetivo principal é resolver problemas do mundo real utilizando dados e tecnologia. Acredito que a análise de dados é uma ferramenta poderosa para tomar decisões informadas e impulsionar o crescimento dos negócios.   
    
    """)

    ###############

    st.markdown("### Soft Skills")   
    # --- SEÇÃO DE HABILIDADES COM BARRAS DE PROGRESSO ---   
    # Habilidade 1: Senso crítico (80%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Senso crítico</span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(80)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**80%**</span>", unsafe_allow_html=True)
    
    # Habilidade 2: Comunicação Executiva (70%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Comunicação Executiva </span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(70)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**90%**</span>", unsafe_allow_html=True)
    
    # Habilidade 2: Inglês (70%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Python</span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(70)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**70%**</span>", unsafe_allow_html=True)

################# FIM DA SEÇÃO DE HABILIDADES SOFTSKILLS ####################
    
    st.markdown("### Hards Skills")   
    # --- SEÇÃO DE HABILIDADES COM BARRAS DE PROGRESSO ---   
    # Habilidade 1: SQL (90%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>SQL</span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(90)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**80%**</span>", unsafe_allow_html=True)
    
    # Habilidade 2: Tableau e Looker (90%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Tableau e Looker </span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(90)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**90%**</span>", unsafe_allow_html=True)

    # Habilidade 2: Appscript, Appsheet e Sheets (90%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Appscript, Appsheet e Sheets </span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(90)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**90%**</span>", unsafe_allow_html=True)

    # Habilidade 2: Python (30%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Python</span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(30)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**90%**</span>", unsafe_allow_html=True)
    
    # Habilidade 2: Slack (80%)
    st.markdown("<span style='font-size: small; font-weight: bold;'>Slack e Automatizações </span>", unsafe_allow_html=True)
    col_progress, col_percent = st.columns([4, 1]) # 4 para a barra, 1 para o texto
    with col_progress:
            st.progress(80)
    with col_percent:
    # Usamos o mesmo font-size para alinhar com o texto da habilidade
            st.markdown("<span style='font-size: small;'>**90%**</span>", unsafe_allow_html=True)


   
    # --- FIM DA SEÇÃO DE HABILIDADES ---



# ==============================================================================
with tab_trajetoria:
    st.header("Minha Trajetória Profissional")
    st.markdown("Aqui você pode visualizar as minhas experiências de trabalho, em ordem cronológica inversa.")

    st.subheader("🏢 Grupo Boticário")
    st.markdown("""
    **Analytics Engineer** (Jan de 2025 - o momento | 11 meses) - Remota
    * Data Product Owner (Out de 2024 - Jan de 2025 | 4 meses)
        * Responsável por gerenciar o backlog dos engenheiros de dados.
        * Produtos desenvolvidos e focados para as áreas de FPA do grupo.
    * Especialista de FP&A (Fev de 2023 - Out de 2024 | 1 ano 9 meses) - Curitiba, Paraná, Brasil
        * Relatórios financeiros, Análise de dados e mais 4 competências
    """)
    st.markdown("---") # Separador visual

    st.subheader("🏢 Triven")
    st.markdown("""
    **Controller** (Dez de 2021 - Fev de 2023 | 1 ano 3 meses)
    * Modelagem financeira, Estudos de viabilidade e mais 1 competência
    * **Analista financeiro** (Out de 2020 - Nov de 2021 | 1 ano 2 meses) - Florianópolis, Santa Catarina, Brasil
        * Relatórios financeiros
    """)
    st.markdown("---") # Separador visual

    st.subheader("🏢 Construtora CFO")
    st.markdown("""
    **Analista financeiro** (Fev de 2018 - Out de 2020 | 2 anos 9 meses) - Florianópolis, Santa Catarina, Brasil
    * **Estagiaria departamento financeiro** (Jan de 2017 - Fev de 2018 | 1 ano 2 meses) - Florianópolis e Região
    """)
    st.markdown("---") # Separador visual
        ## FIM NOVO CÓDIGO

# ==============================================================================
# 2. CONTEÚDO DA ABA "MEUS PROJETOS"
# ==============================================================================
with tab_projetos:
    st.header("Portfólio de Projetos")
    st.markdown("Espaço dedicado ao meus principais projetos categorizados pelo nível de profundidade e tempo de execução.")

    # --- SUBSEÇÕES ANINHADAS DENTRO DE PROJETOS ---
    tab_rapido, tab_aprofundado = st.tabs(["⚡️ Projetos Relâmpago (Quick Wins)", "🏗️ Projetos Aprofundados"])

    with tab_rapido:
        st.header("Minha trajetória de projetos")
        
        # --- PROJETO 1 ---
        st.subheader("👉 Projetos de Sites utilizando o Google Sites")
        st.write("""
        Já construi dois sites oficiais utilizando o Google Sites. O primeiro foi um portal de finanças para diversas áreas entrarem e visualizarem os principais indicadores financeiros da companhia. Nesse site, dei manuteção um dashboard embedado Camada Semantica do Looker, usando HTML e a própria linguagem do Camada Semântica para criar filtros e visualizações customizadas.
                
        O segundo site foi um portal para a área onde eu estava alocada. Nesse portal, focamos em imagens e site mais visual, com menos dados. O objetivo era criar um espaço de comunicação interna para a equipe. Nessa construção, tinhamos a possibilidade de conectar um script em HTML para customizar ainda mais. 
                
        *** Por questões de confidencialidade, não posso compartilhar os links dos sites. ***
        """)

        # --- PROJETO 2 ---
        st.subheader("👉 Construção de +600 arquivos Sheets automatizados com Appscript e Sheet")
        st.write("""
        A necessidade era construir +600 arquivos Sheets para diversas áreas da empresa. Cada arquivo tinha que ser customizado de acordo com a necessidade de cada área, com filtros e dados específicos. Para isso, utilizei o Appscript para automatizar a criação desses arquivos. O Appscript permitiu criar um script que gerava os arquivos de forma automática, economizando tempo e reduzindo erros manuais. Além disso, utilizei o Google Sheets para organizar e armazenar os dados de forma eficiente. O resultado foi uma solução escalável e eficiente para a criação dos arquivos necessários.
                
        *** Por questões de confidencialidade, não posso compartilhar o arquivo ***
        """)

        # --- PROJETO 3 ---
        st.subheader("👉 Disparo de e-mails automatizados com Appscript")
        st.write("""
        Utilizando o Appscript, criei uma solução para o disparo de e-mails automatizados para diversas áreas da empresa. O objetivo era enviar relatórios e atualizações de forma automática, sem a necessidade de intervenção manual. Com o Appscript, desenvolvi um script que coletava os dados necessários e enviava os e-mails de forma personalizada para cada destinatário. Isso não só economizou tempo, mas também garantiu que as informações fossem enviadas de forma consistente e precisa.
                
        *** Por questões de confidencialidade, não posso os e-mails ***
        """)

        # --- PROJETO 4 ---
        st.subheader("👉 Portal de Acessos utilizando Appsheet")
        st.write("""
        Criei um portal de acessos utilizando o Appsheet para gerenciar e controlar os acessos dos colaboradores a diferentes sistemas e ferramentas da empresa. O Appsheet permitiu criar um aplicativo personalizado que facilitou o processo de solicitação e aprovação de acessos. Com esse portal, os colaboradores podiam solicitar acessos de forma rápida e fácil, enquanto os gestores podiam aprovar ou rejeitar essas solicitações de maneira eficiente. Isso resultou em um processo mais ágil e organizado para a gestão de acessos na empresa.
                
        Para o slack, fiz uma conexão com weebooks para disparo de mensagens automáticas para determinados canais, como lembretes e avisos importantes dos acessos.
                
        *** Por questões de confidencialidade, não posso compartilhar o link do portal. ***
        """)
        
    with tab_aprofundado:

        # --- PROJETO 1 ---
        st.subheader("Construção de regras de negócio e modelagem de dados do BusinessMap")
        st.markdown("""
        O BusinessMap é uma ferramenta de gestão de projetos que permite mapear e acompanhar o progresso dos projetos de forma visual e intuitiva. Minha contribuição foi na construção das regras de negócio e na modelagem de dados do BusinessMap, garantindo que a ferramenta atendesse às necessidades específicas da equipe que eu estava inserida. 
                    
        A modelagem de dados envolveu a criação da principal tabela BI (Looker Studio), com todas as métricas e dimensões necessárias para as análises de performance dos projetos. Além disso, desenvolvi dashboards interativos no Looker Studio para facilitar a visualização e interpretação dos dados pelos stakeholders.
                    
        No projeto, utilizei diversas tecnologias, incluindo SQL para a manipulação e consulta dos dados, Google Sheets para a organização e armazenamento das informações, e Looker Studio para a criação dos dashboards e ainda fluxos de trabalho no slack para recebimento de aviso quando regras não fossem atendidas. 
                    
        Para divulgação interna do projeto, participei de treinamentos e workshops para capacitar a equipe no uso do BusinessMap, garantindo que todos estivessem alinhados com as funcionalidades e benefícios da ferramenta.
                    
        No fim, o projeto é benchmark na empresa e já está em sua segunda versão, com melhorias contínuas baseadas no feedback dos usuários. A ferramenta tem sido fundamental para a gestão eficiente dos projetos e para a tomada de decisões informadas pela equipe.
        """)

        # --- PROJETO 2 ---
        st.subheader("Chatbot com IA para atendimento de dúvidas frequentes")
        st.markdown(""" Em construção... """)

# ==============================================================================


# --- CONTEÚDO DA ABA "Fale Comigo" ---
with tab_falecomigo:
    st.header("Vamos nos conectar!")
    st.markdown("""
    Sou de Florianópolis, Santa Catarina, Brasil. A gente pode se encontrar em qualquer ponto dessa cidade. Acate, shoppings ou cafés são sempre boas opções.

    Abaixo estão meus contatos profissionais. Sinta-se à vontade para me chamar!
    
    - **🏢 LinkedIn:** [linkedin.com/in/seu-perfil](https://www.linkedin.com/in/leticiasvieira/)
    - **💻 GitHub:** https://github.com/lsvleticiavieira)
    """)