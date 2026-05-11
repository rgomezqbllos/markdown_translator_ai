---
title: Carregando e gerindo motoristas
shortTitle: Motoristas
intro: 'Aprenda a criar, importar e manter a base de motoristas no GoalBus, a revisar o seu perfil operativo e a deixar uma folha de serviço fiável antes de passar à adscrição, regras e cálculo de Rendimento.'
contentType: how-tos
versions:
  - '*'
---

## Criando ou importando a plantilha de condutores

Antes de falar sobre regras de Rostering, ausências ou atribuição de turnos, precisas ter uma base fiable de condutores. No GoalBus, a gestão de condutores actua como a fonte principal de verdade para a operatividade humana: permite combinar criação manual e carga masiva, e concentra identidade, afiliação ao depósito e disponibilidade em um mesmo diretório. fileciteturn38file2L1-L24

 Usa esta quick start quando já tiveres clara a transição desde Scheduling a Rostering e precisares preparar o colectivo real de pessoas que participará na atribuição.

 Antes de começar, assegura-te de que:
1. Já fechaste a transição desde Scheduling em P19.
2. Tens claro qual colectivo de condutores participará no cálculo.
3. Sabes se vais dar de alta alguns condutores manualmente ou se precisas de uma carga masiva.
4. Tens acesso ao ambiente com permissões para gerir pessoal.

 Para esta quick start, usa este caso de referência:

> **Vou carregar e revisar a plantilha de condutores que poderá cobrir a solução de L1 antes de entrar em adscrição, regras e disponibilidade.**

 Para criar ou importar a plantilha de condutores:
1. No GoalBus, vai ao módulo de **Configuração** > **Pessoal** > **Gestão de condutores**.
ref: P20_Imagen1.png | compact
2. Revê se os condutores do caso já existem na lista geral.
3. Se precisares criar poucos condutores, clica em **Novo Condutor**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisares carregar muitos condutores, realiza uma importação masiva através de ficheiro CSV a partir de **Carga Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolheres importação masiva, prepara o ficheiro com os dados mínimos que a tua operação necessita para identificar corretamente cada pessoa. A janela de importação actuará de ajuda para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Executa a carga e revê o resultado.
7. Vai de volta à lista geral e verifica que os condutores aparecem corretamente.
8. Se detectares duplicados ou registos incompletos, corrige-os antes de seguir.

Para o caso de referencia, termina esta seção só quando puder afirmar:
1. Os motoristas de L1 já estão inscritos ou importados.
2. A lista geral reflete uma única planilha de referência.
3. Já podes abrir o perfil de cada motorista para revisar o seu contexto operativo.

Quando terminares esta seção, deverias ter uma planilha de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando o perfil do motorista e os seus dados estruturais

Uma vez criada a planilha, precisas revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contacto: é o expediente digital completo do empregado dentro da operação. Ali convivem dados estáticos, contexto operativo e atributos que o sistema usará mais tarde para raciocinar sobre a sua elegibilidade. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de começar esta seção, asegúrate de que:
1. Já tens motoristas visíveis na lista geral.
2. Já sabes qual motorista ou qual grupo vais usar como amostra.
3. Queres validar que o registo não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clica no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revisa a barra lateral de dados estáticos.
3. Comprueba pelo menos estes grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operativos, como convenção coletiva ou tipo de contrato,
   3. enlaces operativos, como depósito principal, equipa, área ou tipos de veículos autorizados.
4. Se algum dado estrutural chave estiver faltando, completa-o antes de seguir.
5. Guarda qualquer alteração necessária.
6. Repete a revisão em vários motoristas para confirmar coerência na planilha.

Para o caso de referencia, revisa al menos:
1. O código do motorista.
2. Sua principal depósito.
3. Sua equipa de trabalho.
4. As propriedades operativas que condicionarão a sua posterior atribuição.

Quando terminares esta seção, deverias ter claro que cada motorista conta com um expediente operativo coerente e utilzável. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afectam directamente a forma como o sistema raciocina sobre a pessoa. Na pestaña de administração podes revisar contadores e patrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica de atribuição. fileciteturn38file0L12-L17

Antes de começar esta seção, asegúrate de que:
1. Já revisaste os dados estáticos do perfil.
2. Já sabes se a operação usa contadores ou patrões cíclicos.
3. Queres comprovar que o motorista não só existe, mas que tem um contexto operativo interpretável.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abre a pestaña de **Detalhes de administração**.
2. Revisa os **contadores** ou KPI associados ao motorista se existirem.
3. Comprueba se o motorista está vinculado a algum **patrón de trabalho**.
4. Se a operación usa patrões cíclicos, revisa também o desfase ou posição actual do motorista dentro do patrón.
5. Confirma que estes dados têm sentido para o contexto real.
6. Se a informação dinâmica non é correcta, ajustala antes de pasar a regras ou cálculo.

Para o caso de referencia, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Os seus contadores ou KPI estão disponíveis se o processo os necessitar?
3. O sistema poderia raciocinar correctamente sobre esta pessoa num cálculo de rendição?

Quando terminar esta seção, deverá ter validada não só a identidade do motorista, mas também o seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar o motorista na Rendição

Antes de considerar um motorista como elegível, precisa revisar as suas **habilitações**. Estas habilitações respondem à pergunta “pode esta pessoa trabalhar legal ou tecnicamente neste depósito, grupo ou unidade?”. São geridas numa linha temporal com data de início e fim, e o sistema mostra estados como ativa, futura, expirada ou próxima a expirar para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto requerido, o motor gera um erro ao tentar alocá-la. fileciteturn38file0L17-L34

Antes de começar esta seção, assegure-se de que:
1. Já revisou o perfil do motorista.
2. Já sabe qual depósito, grupo ou unidade necessitará para o seu caso.
3. Entende que uma habilitação não é a mesma que uma cessão ou uma adscrição temporal.

Para revisar e validar as habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Cualificações**.
2. Revise se existem registos vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócio.
3. Comprove o estado visual de cada habilitação:
   1. ativa,
   2. futura,
   3. próxima a expirar,
   4. expirada.
4. Se falta uma habilitação necessária, adicione-a com as suas datas correctas.
5. Se uma habilitação já expirou e não deveria ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Guarde os cambios.
7. Confirme que o motorista já está habilitado para o contexto onde o esperava usar.

Para o caso de referencia, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correcto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade actual.

Quando terminar esta secção, deverias ter motoristas que não só existem na plantilla, mas também são elegíveis do ponto de vista operativo e normativo. fileciteturn38file0L17-L34

## Confirmando que a plantilla já está pronta para a próxima camada de Rostering

O último passo é verificar que a base de motoristas já está pronta para entrar na próxima camada: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é só ter nomes carregados, mas uma plantilla coerente, trazível e utilizável pelo motor.

Antes de terminar, assegure-se de que:
1. Já carregou ou importou a plantilla.
2. Já revisou os perfis principais.
3. Já comprovou dados estruturais e dinâmicos.
4. Já validou habilitações essenciais.

Para confirmar que a plantilla já está preparada:
1. Volte à lista geral de motoristas.
2. Revise que o colectivo necessário para o seu caso está presente.
3. Comprove que os perfis críticos não têm lacunas de informação importantes.
4. Assegure-se de que as pessoas que esperas usar estão habilitadas para o contexto correcto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referencia, termina esta quick start solo quando puder afirmar:
1. A planilha de conductores de L1 já está carregada.
2. Os perfiles clave já foram revisados.
3. As habilitações esenciais já estão em vigor.
4. A base já está pronta para passar a adscripción operativa.

Quando terminares esta seção, deverias ter uma planilha de conductores suficientemente sólida como para continuar com a próxima camada de Rostering.

## Leituras adicionais

- [Gestão da adscrição operativa do motorista](P21_Gestão_da_adscrição_operativa_do_motorista.md)