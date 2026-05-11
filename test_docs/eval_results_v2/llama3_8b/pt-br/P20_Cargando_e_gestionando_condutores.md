---
title: Cargando e gerenciando motoristas
shortTitle: '# Motoristas

## Informações de Motoristas

* **Nome**: [Nome do Motorista]
* **Número de Identificação**: [Número de Identificação do Motorista]
* **Telefone**: [Telefone do Motorista]
* **E-mail**: [E-mail do Motorista]

## Escalas

* **Escala Atual**: [Escala Atual do Motorista]
* **Próxima Escala**: [Próxima Escala do Motorista]
* **Rendição**: [Rendição do Motorista]

## Viagens

* **Viagens Agendadas**: [Viagens Agendadas do Motorista]
* **Viagens Realizadas**: [Viagens Realizadas do Motorista]
* **Quilômetros Ociados**: [Quilômetros Ociados do Motorista]
* **Viagens Ociosas**: [Viagens Ociosas do Motorista]

## Frota

* **Frota Disponível**: [Frota Disponível]
* **Frota em Uso**: [Frota em Uso]
* **Frota em Manutenção**: [Frota em Manutenção]

## Planning

* **Planning de Viagens**: [Planning de Viagens]
* **Itinerário**: [Itinerário]
* **Linha**: [Linha]
* **Depósito**: [Depósito]

## Fluxo de Trabalho

* **Fluxo de Trabalho**: [Fluxo de Trabalho]
* **Status do Trabalho**: [Status do Trabalho]
* **Histórico de Trabalho**: [Histórico de Trabalho]

## Equipe

* **Equipe de Suporte**: [Equipe de Suporte]
* **Contato de Suporte**: [Contato de Suporte]

## Rostering

* **Rostering**: [Rostering]
* **Scheduling**: [Scheduling]

## GoalBus

* **GoalBus**: [GoalBus]
* **GoalDriver**: [GoalDriver]

## Bidding

* **Bidding**: [Bidding]

## Dispatching

* **Dispatching**: [Dispatching]

## Planning

* **Planning**: [Planning]

## Relatórios

* **Relatórios de Viagens**: [Relatórios de Viagens]
* **Relatórios de Frota**: [Relatórios de Frota]
* **Relatórios de Trabalho**: [Relatórios de Trabalho]

## Ajustes

* **Ajustes de Escalas**: [Ajustes de Escalas]
* **Ajustes de Viagens**: [Ajustes de Viagens]
* **Ajustes de Frota**: [Ajustes de Frota]

## Ferramentas

* **Ferramentas de Planning**: [Ferramentas de Planning]
* **Ferramentas de Rostering**: [Ferramentas de Rostering]
* **Ferramentas de Dispatching**: [Ferramentas de Dispatching]

## Ajuda

* **Ajuda**: [Ajuda]
* **Documentação**: [Documentação]'
intro: Aprenda a criar, importar e manter a base de motoristas no GoalBus, revisar seu perfil operativo e deixar uma plantilla confiável antes de passar a adscrição, regras e cálculo de Escalas.
contentType: how-tos
versions:
  - '*'
---

## Criando ou Importando a Plantilla de Condutores

Antes de discutir regras de Escalas, ausências ou atribuição de turnos, você precisa ter uma base confiável de condutores. No GoalBus, a gestão de condutores atua como a fonte principal de verdade para a operatividade humana: permite combinar criação manual e carga em massa, e concentra identidade, afiliação ao Depósito e disponibilidade em um mesmo diretório. fileciteturn38file2L1-L24

Use essa quick start quando já tiver clara a transição desde Programação a Escalas e precisar preparar a equipe real de pessoas que participará na atribuição.

Antes de começar, certifique-se de que:
1. Já encerrou a transição desde Programação em P19.
2. Tem claro qual equipe de condutores participará no cálculo.
3. Sabe se vai dar alta alguns condutores manualmente ou se precisar de uma carga em massa.
4. Tem acesso ao ambiente com permissões para gerenciar pessoal.

Para essa quick start, use esse caso de referência:

> **Vou carregar e revisar a plantilla de condutores que poderá cobrir a solução de L1 antes de entrar em adscrição, regras e disponibilidade.**

Para criar ou importar a plantilla de condutores:
1. No GoalBus, vá ao módulo de **Configuração** > **Pessoal** > **Gestão de Condutores**.
ref: P20_Imagen1.png | compact
2. Revisie se os condutores do caso já existem na lista geral.
3. Se precisar criar poucos condutores, clique em **Novo Condutores**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos condutores, realize uma importação em massa mediante arquivo CSV desde **Carga Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolher importação em massa, prepare o arquivo com os dados mínimos que sua operação precisa para identificar corretamente cada pessoa. A janela de importação atuará como ajuda para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e comprove que os condutores aparecem corretamente.
8. Se detectar duplicados ou registros incompletos, corrija-os antes de seguir.

Para o caso de referência, termine essa seção apenas quando puder afirmar:
1. Os motoristas de L1 já estão cadastrados ou importados.
2. A lista geral reflete uma única plantilha de referência.
3. Já pode abrir o perfil de cada motorista para revisar seu contexto operativo.

Quando terminar essa seção, deveria ter uma plantilha de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando o perfil do motorista e seus dados estruturais

Uma vez criada a plantilha, precisa revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contato: é o expediente digital completo do empregado dentro da operação. Lá convivem dados estáticos, contexto operativo e atributos que o sistema usará mais adiante para raciocinar sobre sua elegibilidade. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de começar essa seção, assegure-se de que:
1. Já tem motoristas visíveis na lista geral.
2. Já sabe qual motorista ou qual grupo usar como exemplo.
3. Quer validar que o registro não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revisar a barra lateral de dados estáticos.
3. Compruebe pelo menos esses grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operativos, como convenio coletivo ou tipo de contrato,
   3. enlaces operativos, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural chave faltar, complete-o antes de seguir.
5. Guarde qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar consistência na plantilha.

Para o caso de referência, revise pelo menos:
1. O código do motorista.
2. Seu depósito principal.
3. Seu grupo de trabalho.
4. As propriedades operativas que condicionarão sua atribuição posterior.

Quando terminar essa seção, você deveria ter claro que cada motorista conta com um expediente operativo coerente e utilizable. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente a como o sistema raciocina sobre a pessoa. Na aba de administração, você pode revisar contadores e padrões de trabalho, que formam parte do contexto operativo usado mais adiante pela lógica de atribuição. fileciteturn38file0L12-L17

Antes de começar essa seção, certifique-se de que:
1. Já revisou os dados estáticos do perfil.
2. Já sabe se sua operação usa contadores ou padrões cíclicos.
3. Quer comprovar que o motorista não apenas existe, mas tem um contexto operativo interpretável.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abra a aba de **Detalhes de administração**.
2. Revisar os **contadores** ou KPI associados ao motorista se existirem.
3. Comprue o se o motorista está vinculado a algum **padrão de trabalho**.
4. Se sua operação usa padrões cíclicos, revise também o desfase ou posição atual do motorista dentro do padrão.
5. Confirme que esses dados têm sentido para o contexto real.
6. Se a informação dinâmica não for correta, ajuste-a antes de passar a regras ou cálculo.

Para o caso de referência, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Seus contadores ou KPI estão disponíveis se o processo os precisar?
3. O sistema poderia raciocinar corretamente sobre essa pessoa em um cálculo de atribuição?

Ao terminar essa seção, você deveria ter validada não apenas a identidade do motorista, mas também seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar o motorista em Escalas

Antes de considerar um motorista como elegível, você precisa revisar suas **habilitações**. Essas habilitações respondem à pergunta “Pode essa pessoa trabalhar legal ou tecnicamente nesse depósito, grupo ou unidade?”. Elas são gerenciadas em uma linha temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, caducado ou próximo a caducar para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto requerido, o motor gera um erro ao tentar atribuí-la. fileciteturn38file0L17-L34

Antes de começar essa seção, certifique-se de que:
1. Já revisou o perfil do motorista.
2. Já sabe qual depósito, grupo ou unidade precisará para seu caso.
3. Entende que uma habilitação não é o mesmo que uma cessão ou uma adscrição temporal.

Para revisar e validar as habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Cualificações**.
2. Revisar se existem registros vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócios.
3. Verifique o estado visual de cada habilitação:
   1. ativa,
   2. futura,
   3. próxima a caducar,
   4. caducada.
4. Se falta uma habilitação necessária, adicione-a com suas datas corretas.
5. Se uma habilitação já caducou e não deveria ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Guarde as alterações.
7. Confirme que o motorista já está habilitado para o contexto onde espera usá-lo.

Para o caso de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade atual.

Quando terminar esta seção, deverias ter motoristas que não só existem na plantilla, mas também são elegíveis desde o ponto de vista operativo e normativo. fileciteturn38file0L17-L34

## Confirmando que a plantilla já está lista para a próxima capa de Escalas

O último passo é verificar que a base de motoristas já está lista para entrar na próxima capa: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é só ter nomes carregados, mas uma plantilla coerente, trazável e utilável pelo planejador.

Antes de terminar, assegura-te de que:
1. Já carregaste ou importaste a plantilla.
2. Já revisaste os perfis principais.
3. Já comprovaste dados estruturais e dinâmicos.
4. Já validaste habilitações essenciais.

Para confirmar que a plantilla já está preparada:
1. Volta à lista geral de motoristas.
2. Revisa que a equipe necessária para o seu caso está presente.
3. Comprima que os perfis críticos não têm lacunas de informações importantes.
4. Assegura-te de que as pessoas que espera usar estão habilitadas para o contexto correto.
5. Pergunta-te se o sistema já poderia usar essa base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Escalas,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrige a base de motoristas antes de seguir.

Para o caso de referência, termine essa quick start apenas quando puder afirmar:
1. A plantilha de motoristas de L1 já está carregada.
2. Os perfis-chave já foram revisados.
3. As habilitações essenciais já estão vigentes.
4. A base já está pronta para passar à adscrição operativa.

Quando terminar essa seção, você deveria ter uma plantilha de motoristas suficientemente sólida para continuar com a próxima camada de Escalas.

## Leituras adicionais

- [Gestão da adscrição operativa do motorista](P21_Gestão_da_adscrição_operativa_do_motorista.md)