---
title: 'Carregando e gerindo condutores'
shortTitle: 'Condutores'
intro: 'Aprende a criar, importar e manter a base de conductores no GoalBus, revisar o seu perfil operativo e deixar uma folha de cálculo fiável antes de passar à adscrição, regras e cálculo do Rostering.'
contentType: 'how-tos'
versions:
  - '*'
---

## Criando e importando a plantilha de condutores

Antes de falar sobre regras de Rostering, ausências ou atribuição de turnos, precisas ter uma base fiável de condutores. No GoalBus, o gerenciamento de condutores atua como a fonte principal da verdade para a operatividade humana: permite combinar criação manual e carregamento em massa, e concentra identidade, afiliação ao depósito e disponibilidade num mesmo diretório. fileciteturn38file2L1-L24

Usa esta quick start quando já tiveres clara a transição de Scheduling para Rostering e precisares preparar o colectivo real de pessoas que participará na atribuição.

Antes de começar, assegura-te de que:
1. Já fechaste a transição de Scheduling em P19.
2. Tens claro qual é o colectivo de condutores que participará no cálculo.
3. Sabes se vais dar de alta alguns poucos condutores manualmente ou se precisas de um carregamento em massa.
4. tens acesso ao ambiente com permissões para gerir pessoal.

Para esta quick start, usa este caso de referência:

> **Vou carregar e revisar a plantilha de condutores que poderá cobrir a solução L1 antes da adscrição, regras e disponibilidade.**

Para criar ou importar a plantilha de condutores:
1. No GoalBus, vai ao módulo de **Configuração** > **Pessoal** > **Gestão de condutores**.
ref: P20_Imagen1.png | compact
2. Revê se os condutores do caso já existem na lista geral.
3. Se precisares criar poucos condutores, clica em **Novo Condutor**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisares carregar muitos condutores, realiza uma importação em massa através de ficheiro CSV a partir de **Carregamento Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolheres importação em massa, prepara o ficheiro com os dados mínimos que a tua operação precisa para identificar corretamente cada pessoa. A janela de importação actuará como ajuda para preparar o CSV do carregamento.
ref: P20_Imagen4.png
6. Executa o carregamento e revê o resultado.
7. Vai à lista geral e verifica que os condutores aparecem corretamente.
8. Se detectares duplicados ou registos incompletos, corrige-os antes de seguir.

Para o caso de referência, termina esta seção só quando puder afirmar:
1. Os motoristas da L1 já estão inscritos ou importados.
2. A lista geral reflete uma única planilha de referência.
3. Já pode abrir o perfil de cada motorista para revisar o seu contexto operativo.

Quando terminares esta seção, deverias ter uma planilha de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando o perfil do motorista e os seus dados estruturais

Uma vez criada a planilha, precisas revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contacto: é o expediente digital completo do empregado dentro da operação. Ali convivem dados estáticos, contexto operativo e atributos que o sistema usará mais tarde para raciocinar sobre a sua elegibilidade. fileciteturn38file0L7-L19 fileciteturn38file2L24-L39

Antes de começar esta seção, assegura-te de que:
1. Já tens motoristas visíveis na lista geral.
2. Sabes qual ou quais motorista(s) usarás como amostra.
3. Queres validar que o registo não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clica no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revisa a barra lateral com os dados estáticos.
3. Comprueba pelo menos estes grupos de informação:
   1. dados básicos, como o nome e o código,
   2. dados operativos, como convenção coletiva ou tipo de contrato,
   3. enlaces operativos, como depósito principal, equipa, área ou tipos de veículos autorizados.
4. Se algum dado estrutural crucial estiver faltando, completa-o antes de continuar.
5. Guarda qualquer alteração necessária.
6. Repete a revisão em vários motoristas para confirmar coerência na planilha.

Para o caso de referência, revista pelo menos:
1. O código do motorista.
2. Sua unidade principal.
3. Seu grupo de trabalho.
4. As propriedades operativas que condicionarão a sua atribuição posterior.

Quando terminares esta secção, deverás ter claro que cada motorista conta com um expediente operativo coerente e utilzável. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afectam directamente a forma como o sistema raciocina sobre a pessoa. Na pestaña de administração podes revistar contadores e patrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica da atribuição. fileciteturn38file0L12-L17

Antes de iniciar esta secção, assegura-te de:
1. Já revistaste os dados estáticos do perfil.
2. Sabes se a tua operação usa contadores ou patrões cíclicos.
3. Queres comprovar que o motorista não só existe como tem um contexto operativo interpretável.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abre a pestaña de **Detalhes da administração**.
2. Revista os **contadores** ou KPI associados ao motorista se existirem.
3. Comprueba se o motorista está vinculado a algum **patrão de trabalho**.
4. Se a tua operação usa patrões cíclicos, revista também o desfasamento ou posição actual do motorista dentro do patrão.
5. Confirma que estes dados têm sentido para o contexto real.
6. Se a informação dinâmica não for correcta, ajusta-a antes de passar às regras ou cálculo.

Para o caso de referencia, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Os seus contadores ou KPI estão disponíveis se o processo os necessitar?
3. O sistema poderia raciocinar correctamente sobre esta pessoa num cálculo de rendição?

Quando terminar esta secção, deve validar não só a identidade do motorista, mas também o seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar ao motorista na Rendição

Antes de considerar um motorista como elegível, precisa revisar as suas **habilitações**. Estas habilitações respondem à pergunta “pode esta pessoa trabalhar legal ou tecnicamente neste depósito, grupo ou unidade?”. São geridas numa linha temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, vencido ou próximo a vencer para facilitar a leitura. Se uma pessoa não estiver habilitada no contexto requerido, o motor gera um erro ao tentar renderizá-la. fileciteturn38file0L17-L34

Antes de começar esta secção, assegure-se de que:
1. Já revisou o perfil do motorista.
2. JÁ SABE qual depósito, grupo ou unidade necessitará para o seu caso.
3. ENTENDE que uma habilitação não é a mesma coisa que uma cessão ou adscrição temporal.

Para revisar e validar as habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Qualificações**.
2. Verifique se existem registos vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócio.
3. Comprove o estado visual de cada habilitação:
   1. ativa,
   2. futura,
   3. próxima a vencer,
   4. vencida.
4. Se falta uma habilitação necessária, adicione-a com as suas datas corretas.
5. Se uma habilitação já venceu e não deveria ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Guarde os cambios.
7. Confirme que o motorista já está habilitado para o contexto onde esperas usar-o.

Para o caso de referência, não continues até poder afirmar:
1. O motorista está habilitado para o depósito correcto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompan a elegibilidade actual.

Quando terminares esta secção, deverias ter condutores que não só existem na plantilla, mas também são elegíveis desde o ponto de vista operativo e normativo. fileciteturn38file0L17-L34

## Confirmando que a plantilla já está lista para a próxima camada de Rostering

O último passo é verificar se a base de condutores já está pronta para entrar na próxima camada: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é só ter nomes carregados, mas uma plantilla coerente, trazível e utilizável pelo motor.

Antes de terminar, assegura-te de que:
1. Já cargaste ou importaste a plantilla.
2. Já revisaste os perfis principais.
3. Já comprobaste dados estruturais e dinâmicos.
4. Já validaste habilitações essenciais.

Para confirmar que a plantilla já está preparada:
1. Vai à lista geral de condutores.
2. Revê se o colectivo necessário para o teu caso está presente.
3. Comprueba que os perfis críticos não têm lacunas importantes de informação.
4. Asegura-te de que as pessoas que esperas usar estão habilitadas no contexto correcto.
5. Pergunta-te se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continua com o próximo quick start.
7. Se a resposta for não, corrige a base de condutores antes de seguir.

Para o caso de referencia, termina esta quick start solo quando puder afirmar:
1. A planilha de conductores L1 já está carregada.
2. Os perfiles chave já foram revisados.
3. As habilitações essenciais já estão em vigor.
4. A base já está pronta para passar a adscrição operativa.

Quando terminares esta secção, deverias ter uma planilha de conductores suficientemente sólida como para continuar com a próxima camada de Rostering.

## Leituras adicionais

- [Gestão da adscripción operativa do motorista](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)