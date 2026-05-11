---
title: A Cargar e Gerir Motoristas
shortTitle: Motoristas
intro: 'Aprenda a criar, importar e manter a base de motoristas no GoalBus, revisar o seu perfil operativo e deixar uma plantilla fidedigna antes de passar a adscrição, regras e cálculo de Rostering.'
contentType: how-tos
versions:
  - '*'

## Criando ou Importando a Plantilla de Motoristas

Antes de falar de regras de Rostering, ausências ou atribuição de turnos, necessitas ter uma base fidedigna de motoristas. Em GoalBus, a gestão de motoristas actua como a fonte principal de verdade para a operatividade humana: permite combinar criação manual e carga em massa, e concentra identidade, afiliação ao depósito e disponibilidade num mesmo diretório. fileciteturn38file2L1-L24

Usa esta quick start quando já tiveres clara a transição desde Scheduling a Rostering e necessites preparar a equipa real de pessoas que participará na atribuição.

Antes de começar, assegura-te de que:
1. Já fechaste a transição desde Scheduling em P19.
2. Tens claro qual a equipa de motoristas que participará no cálculo.
3. Sabes se vais a dar de alta alguns poucos motoristas manualmente ou se necessitas de uma carga em massa.
4. Tens acesso ao ambiente com permissões para gerir pessoal.

Para esta quick start, usa este caso de referência:

> **Vou a carregar e revisar a plantilla de motoristas que poderá cobrir a solução de L1 antes de entrar em adscrição, regras e disponibilidade.**

Para criar ou importar a plantilla de motoristas:
1. Em GoalBus, vai ao módulo de **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P20_Imagen1.png | compact
2. Revisa se os motoristas do caso já existem na lista geral.
3. Se necessitas criar poucos motoristas, clica em **Novo Motorista**.
ref: P20_Imagen2.png | compact(2x)
4. Se necessitas carregar muitos motoristas, realiza uma importação em massa mediante arquivo CSV desde **Carga Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolheres importação em massa, prepara o arquivo com os dados mínimos que a tua operação necessita para identificar correctamente a cada pessoa. A janela de importação actuará de ajuda para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Executa a carga e revisa o resultado.
7. Vai à lista geral e verifica que os motoristas aparecem correctamente.
8. Se detectares duplicados ou registos incompletos, corríg-los antes de seguir.

Para o caso de referência, termina esta seção apenas quando puder afirmar:
1. Os motoristas de L1 já estão registados ou importados.
2. A lista geral reflete uma única plantilla de referência.
3. Já pode abrir o perfil de cada motorista para rever o seu contexto operativo.

Quando terminar esta seção, deverias ter uma plantilla de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## A revisão do perfil do motorista e dos seus dados estruturais

Uma vez criada a plantilla, necessitas rever o **perfil do motorista**. O perfil não é apenas uma ficha de contacto: é o expediente digital completo do empregado dentro da operação. Ali convivem dados estáticos, contexto operativo e atributos que o sistema usará mais tarde para razonar sobre a sua elegibilidade. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de começar esta seção, certifica-te de que:
1. Já tens motoristas visíveis na lista geral.
2. Já sabes qual motorista ou qual grupo usarás como exemplo.
3. Queres validar que o registo não é apenas administrativo, mas operativo.

Para rever o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revisa a barra lateral de dados estáticos.
3. Comprueba pelo menos estes grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operativos, como convenio colectivo ou tipo de contrato,
   3. enlaces operativos, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural chave faltar, complete-o antes de continuar.
5. Guarda qualquer alteração necessária.
6. Repete a revisão em vários motoristas para confirmar consistência na plantilla.

Para o caso de referência, revisa pelo menos:
1. O código do motorista.
2. Seu depósito principal.
3. Seu grupo de trabalho.
4. As propriedades operativas que condicionarão sua atribuição posterior.

Quando terminar esta seção, deveria ter claro que cada motorista conta com um expediente operativo coerente e utilizable. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente a como o sistema raciocina sobre a pessoa. Na aba de administração pode revisar contadores e padrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica de atribuição. fileciteturn38file0L12-L17

Antes de começar esta seção, certifica-te de que:
1. Já revisaste os dados estáticos do perfil.
2. Já sabes se sua operação usa contadores ou padrões cíclicos.
3. Quer comprobar que o motorista não só existe, mas que tem um contexto operativo interpretável.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abre a aba de **Detalhes de administração**.
2. Revisa os **contadores** ou KPI associados ao motorista se existirem.
3. Comprima se o motorista está vinculado a algum **padrão de trabalho**.
4. Se sua operação usa padrões cíclicos, revisa também o desfasamento ou posição atual do motorista dentro do padrão.
5. Confirma que esses dados têm sentido para o contexto real.
6. Se a informação dinâmica não é correcta, ajusta-a antes de passar a regras ou cálculo.

Para o caso de referência, pergunta-te:
1. Este motorista tem o padrão que deveria ter?
2. Os seus contadores ou KPI estão disponíveis se o processo os necessitar?
3. O sistema poderia raciocinar correctamente sobre esta pessoa num cálculo de atribuição?

Quando terminares esta seção, deverias ter validada não apenas a identidade do motorista, mas também o seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar o motorista em Rostering

Antes de considerar um motorista como elegível, precisas de rever as suas **habilitações**. Estas habilitações respondem à pergunta “Pode esta pessoa trabalhar legal ou tecnicamente nesse depósito, grupo ou unidade?”. Elas são geridas em uma linha temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, caducado ou próximo a caducar para facilitar a leitura. Se uma pessoa não está habilitada para o contexto requerido, o motor gera um erro ao tentar atribuí-la. fileciteturn38file0L17-L34

Antes de começar esta seção, certifica-te de que:
1. Já revisaste o perfil do motorista.
2. Já sabes qual depósito, grupo ou unidade necessitará para o seu caso.
3. Entendes que uma habilitação não é o mesmo que uma cessão ou uma adscrição temporal.

Para rever e validar as habilitações:
1. Dentro do perfil do motorista, abre a pestaña **Habilitações / Cualificações**.
2. Revisa se existem registos vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócios.
3. Comprima o estado visual de cada habilitação:
   1. ativa,
   2. futura,
   3. próxima a caducar,
   4. caducada.
4. Se falta uma habilitação necessária, adiona-a com as suas datas corretas.
5. Se uma habilitação já caducou e não deveria ser usada, deixa-a como histórico sem tentar reescrever o passado.
6. Guarda os alterações.
7. Confirma que o motorista já está habilitado para o contexto onde o esperas usar.

Para o caso de referência, não continúes até poder afirmar:
1. O motorista está habilitado para o depósito correcto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade atual.

Quando terminares esta seção, deverias ter motoristas que não só existem na plantilla, mas também são elegíveis desde o ponto de vista operativo e normativo. 

## A confirmar que a plantilla já está lista para a próxima capa de Rostering

O último passo é verificar que a base de motoristas já está lista para entrar na próxima capa: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é só ter nomes carregados, mas uma plantilla coerente, trazável e utilizable pelo planeador.

Antes de terminar, assegura-te de que:
1. Já carregaste ou importaste a plantilla.
2. Já revisaste os perfis principais.
3. Já comprovaste dados estruturais e dinâmicos.
4. Já validaste habilitações essenciais.

Para confirmar que a plantilla já está preparada:
1. Volta à lista geral de motoristas.
2. Revisa que o colectivo necessário para o teu caso está presente.
3. Comprima que os perfis críticos não têm buracos de informação importantes.
4. Assegura-te de que as pessoas que esperas usar estão habilitadas para o contexto correcto.
5. Pergunta-te se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continua com o próximo quick start.
7. Se a resposta for não, corrige a base de motoristas antes de seguir.

Para o caso de referência, termina esta quick start apenas quando puder afirmar:
1. A plantilha de motoristas de L1 já está carregada.
2. Os perfis-chave já foram revisados.
3. As habilitações essenciais já estão vigentes.
4. A base já está pronta para passar à adscrição operativa.

Quando terminares esta seção, deverias ter uma plantilha de motoristas suficientemente sólida como para continuar com a próxima capa de Rostering.

## Leituras adicionais

- [Gestão da adscrição operativa do motorista](P21_Gestão_da_adscrição_operativa_do_motorista.md)