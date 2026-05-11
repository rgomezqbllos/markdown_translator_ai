---
title: Carregando e gerenciando motoristas
shortTitle: Motoristas
intro: Aprenda a criar, importar e manter a base de condutores em GoalBus, revisar o seu perfil operacional e deixar uma planilha confiável antes de passar à adscrição, regras e cálculo de Rostering.
contentType: how-tos
versions:
  - '*'
---

## Criando a planilha de condutores

Antes de falar de regras de Rostering, ausencias ou atribuição de turnos, precisa ter uma base confiável de condutores. No GoalBus, a gestão de condutores atua como a fonte principal de verdade para a operação humana: permite combinar criação manual e carga massiva, e concentra identidade, afiliação ao depósito e disponibilidade em um mesmo diretório. fileciteturn38file2L1-L24


Use esta quick start quando já tiver a transição clara de Scheduling para Rostering e necessite preparar o colectivo real de pessoas que participará na atribuição.

Antes de começar, certifique-se de que:
1. Já encerrou a transição de Scheduling em P19.
2. Tem claro qual o colectivo de condutores que participará no cálculo.
3. Sabe se vai dar de alta poucos condutores manualmente ou se precisa de uma carga massiva.
4. Tem acesso ao ambiente com permissões para gerenciar pessoal.

Para esta quick start, use este caso de referência:

> **Vou carregar e revisar a planilha de condutores que poderá cobrir a solução de L1 antes de entrar em adscrição, regras e disponibilidade.**

Para criar ou importar a planilha de condutores:
1. No GoalBus, vá para o módulo de **Configuração** > **Personal** > **Gestão de Condutores**.
ref: P20_Imagen1.png | compact
2. Verifique se os condutores do caso já existem na lista geral.
3. Se precisar criar poucos condutores, clique em **Novo Condutores**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos condutores, realize uma importação massiva através de arquivo CSV a partir de **Carga Personal**.
ref: P20_Imagen3.png | compact
5. Se optar por importação massiva, prepare o arquivo com os dados mínimos que a sua operação precisa para identificar corretamente cada pessoa. A janela de importação actuará de ajuda para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e verifique se os condutores aparecem corretamente.
8. Se detectar duplicatas ou registros incompletos, corrija-os antes de prosseguir.

Para o caso de referência, termina esta seção apenas puder afirmar:
1. Os motoristas da L1 já estão dados de alta ou importados.
2. A lista geral reflete uma única plantilla de referência.
3. Já pode abrir o perfil de cada motorista para verificar o seu contexto operativo.

Quando terminar esta seção, deverias ter uma plantilla de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 Tully fileciteturn38file2L1-L24 Tully

## Revisando o perfil do motorista e seus dados estruturais

Uma vez criada a plantilla, necessitas revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contacto: é o expediente digital completo do empregado dentro da operação. Ahí convivem dados estáticos, contexto operativo e atributos que o sistema usará mais tarde para razonar sobre a sua elegibilidade. fileciteturn38file0L8-L20 Tully fileciteturn38file2L25-L40 Tully

Antes de começar esta seção, certifique-se de que:
1. Já tem motoristas visíveis na lista geral.
2. Já sabe qual motorista ou grupo vai usar como exemplo.
3. Quer validar que o registro não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral de dados estáticos.
3. Verifique pelo menos estes grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operativos, como convênio coletivo ou tipo de contrato,
   3. links operativos, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural for crucial, complemente-o antes de continuar.
5. Guarde qualquer mudança necessária.
6. Repita a revisão em vários motoristas para confirmar consistência na plantilla.

Para o caso de referência, revisa al menos:
1. O código do motorista.
2. O seu depósito principal.
3. O seu grupo de trabalho.
4. As propriedades operacionais que condicionarán a sua atribuição posterior.

Quando terminar esta seção, deberias ter claro que cada motorista tem um expediente operativo coerente e utilizável. fileciteturn38file0L8-L20


## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente a forma como o sistema raciocina sobre a pessoa. Na aba de administração, pode revisar contadores e padrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica de atribuição. fileciteturn38file0L12-L17


Antes de começar esta seção, certifique-se de que:
1. Já revisou os dados estáticos do perfil.
2. Já sabe se a sua operação usa contadores ou padrões cíclicos.
3. Quer verificar se o motorista não só existe, mas tem um contexto operativo interpretado.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abra a aba de **Detalhes de administração**.
2. Revise os **contadores** ou KPI associados ao motorista se existem.
3. Verifique se o motorista está vinculado a algum **padrão de trabalho**.
4. Se a sua operação usa padrões cíclicos, revise também o desfase ou posição atual do motorista dentro do padrão.
5. Confirme que estes dados têm sentido para o contexto real.
6. Se a informação dinâmica não for correta, ajuste-a antes de passar para regras ou cálculo.

Para o caso de referência, pregúntate:
1. Este motorista tem o padrão que deveria ter?
2. Os seus contadores ou KPI estão disponíveis se o processo os precisa?
3. O sistema poderia razonar correctamente sobre esta pessoa num cálculo de atribuição?

Quando termines esta seção, deberías ter validada não só a identidade do motorista, mas também o seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitacões antes de usar o motorista no Rostering

Antes de considerar um motorista como elegível, precisa revisar as suas **habilitacões**. Estas habilitacões respondem à pergunta "¿pode esta pessoa trabalhar legal ou técnicamente neste depósito, grupo ou unidade?". São geridas num intervalo temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, caducado ou próximo a caducar para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto requerido, o motor gera um erro ao tentar atribuí-la. fileciteturn38file0L17-L34

Antes de começar esta seção, certifique-se de que:
1. Já revisou o perfil do motorista.
2. Já sabe que depósito, grupo ou unidade precisará para o seu caso.
3. Entiende que uma habilitacão não é o mesmo que uma cesão ou uma adscripción temporal.

Para revisar e validar as habilitacões:
1. Dentro do perfil do motorista, abra a aba **Habilitacões / Qualificacões**.
2. Revise se existem registros vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócio.
3. Verifique o estado visual de cada habilitacão:
   1. ativa,
   2. futura,
   3. próxima a caducar,
   4. caducada.
4. Se falta uma habilitacão necessária, adicione-a com as datas corretas.
5. Se uma habilitacão já caducou e não deve ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Salve os cambios.
7. Confirme que o motorista já está habilitado para o contexto onde espera usá-lo.

Para o caso de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade atual.

Quando terminar esta seção, deverias ter motoristas que não só existem na planilha, mas também são elegíveis desde o ponto de vista operativo e normativo. fileciteturn38file0L17-L34

## Confirmando que a planilha já está lista para a próxima camada de Rostering

O último passo é verificar que a base de motoristas já está lista para entrar na próxima camada: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é apenas ter nomes carregados, mas uma planilha coerente, rastreável e utilizável pelo motor.

Antes de terminar, certifique-se de que:
1. Já carregou ou importou a planilha.
2. Já revisou os perfis principais.
3. Já verificou dados estruturais e dinâmicos.
4. Já validou habilitações essenciais.

Para confirmar que a planilha já está preparada:
1. Volte à lista geral de motoristas.
2. Verifique que o coletivo necessário para o seu caso está presente.
3. Verifique se os perfis críticos não têm furos de informação importantes.
4. Certifique-se de que as pessoas que esperam usar estão habilitadas para o contexto correto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referência, termina esta quick start só quando podes afirmar:
1. A plantilla de motoristas da L1 já está carregada.
2. Os perfis chave já foram revisados.
3. As habilitações essenciais já estão vigentes.
4. A base já está lista para passar à adscrição operacional.

Quando terminares esta seção, deberias ter uma plantilla de motoristas suficientemente sólida como para continuar com a seguinte etapa de Rostering.

## Leitura adicional

- [Gestão da adscrição operacional do motorista](P21_Gestão_da_adscrição_operacional_do_motorista.md)