---
title: Carregando e gerenciando motoristas
shortTitle: Motoristas
intro: Aprenda a criar, importar e manter a base de motoristas no GoalBus, revisar seu perfil operacional e deixar uma plantilla fiable antes de passar a adscrição, regras e cálculo de Rostering.
contentType: how-tos
versions:
  - '*'
---

## Criando e importando a plantilha de motoristas

Antes de falar sobre regras de Rostering, ausências ou atribuição de escalas, você precisa ter uma base confiável de motoristas. No GoalBus, a gestão de motoristas atua como a fonte principal de verdade para a operatividade humana: permite combinar criação manual e carga massiva, e concentra identidade, afiliação ao depósito e disponibilidade em um mesmo diretório. fileciteturn38file2L1-L24

Use esta quick start quando já tiver clara a transição de Scheduling para Rostering e precisar preparar o coletivo real de pessoas que participará na atribuição.

Antes de começar, assegure-se de que:
1. Você já fechou a transição de Scheduling em P19.
2. Você sabe qual coletivo de motoristas participará no cálculo.
3. Você sabe se vai dar de alta alguns motoristas manualmente ou se precisará de uma carga massiva.
4. Você tem acesso ao ambiente com permissões para gerenciar pessoal.

Para esta quick start, use este caso de referência:

> **Vou carregar e revisar a plantilha de motoristas que poderá cobrir a solução de L1 antes de entrar em adscrição, regras e disponibilidade.**

Para criar ou importar a plantilha de motoristas:
1. No GoalBus, vá ao módulo de **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P20_Imagen1.png | compact
2. Revise se os motoristas do caso já existem na lista geral.
3. Se precisar criar poucos motoristas, clique em **Novo Motorista**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos motoristas, realize uma importação massiva através de arquivo CSV a partir de **Carga Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolher importação massiva, prepare o arquivo com os dados mínimos que sua operação precisa para identificar corretamente cada pessoa. A janela de importação atuará de auxílio para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e verifique que os motoristas aparecem corretamente.
8. Se detectar duplicados ou registros incompletos, corrija-os antes de seguir.

Para o caso de referência, termina esta seção só quando puder afirmar:
1. Os motoristas de L1 já estão cadastrados ou importados.
2. A lista geral reflete uma única planilha de referência.
3. Você já pode abrir o perfil de cada motorista para revisar seu contexto operacional.

Quando terminar esta seção, você deveria ter uma planilha de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Revisando o perfil do motorista e seus dados estruturais

Uma vez criada a planilha, você precisa revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contato: é o expediente digital completo do funcionário dentro da operação. Ali convivem dados estáticos, contexto operacional e atributos que o sistema usará mais tarde para raciocinar sobre sua elegibilidade. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de começar esta seção, assegure-se de que:
1. Você já tem motoristas visíveis na lista geral.
2. Você já sabe qual motorista ou qual grupo você usará como amostra.
3. Você quer validar que o registro não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral de dados estáticos.
3. Comunique-se com pelo menos estes grupos de informações:
   1. dados básicos, como nome e código,
   2. dados operativos, como convenção coletiva ou tipo de contrato,
   3. enlaces operativos, como depósito principal, equipe, área ou tipos de veículos autorizados.
4. Se algum dado estrutural chave estiver faltando, complete-o antes de seguir.
5. Salve qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar coerência na planilha.

Para o caso de referência, revise ao menos:
1. O código do motorista.
2. Seu depósito principal.
3. Seu grupo de trabalho.
4. As propriedades operacionais que condicionarão sua atribuição posterior.

Quando terminar esta seção, você deve ter clareza de que cada motorista possui um expediente operacional coerente e utilizável. fileciteturn38file0L8-L20

## Revisando o contexto operacional e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente como o sistema raciocina sobre a pessoa. Na aba de administração, você pode revisar contadores e padrões de trabalho, que formam parte do contexto operacional usado mais tarde pela lógica de atribuição. fileciteturn38file0L12-L17

Antes de começar esta seção, assegure-se de que:
1. Você já revisou os dados estáticos do perfil.
2. Você sabe se sua operação usa contadores ou padrões cíclicos.
3. Você quer verificar que o motorista não apenas existe, mas também possui um contexto operacional interpretável.

Para revisar o contexto operacional dinâmico:
1. Dentro do perfil do motorista, abra a aba de **Detalhes de administração**.
2. Revise os **contadores** ou KPI associados ao motorista, se existirem.
3. Verifique se o motorista está vinculado a algum **padrão de trabalho**.
4. Se sua operação usa padrões cíclicos, revise também o deslocamento ou posição atual do motorista dentro do padrão.
5. Confirme que esses dados fazem sentido para o contexto real.
6. Se a informação dinâmica não for correta, ajuste-a antes de passar para regras ou cálculo.

Para o caso de referência, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Seus contadores ou KPI estão disponíveis se o processo os precisar?
3. O sistema poderia raciocinar corretamente sobre esta pessoa em um cálculo de escalas?

Quando terminar esta seção, você deve ter validado não apenas a identidade do motorista, mas também seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar o motorista em Escalas

Antes de considerar um motorista como elegível, você precisa revisar suas **habilitações**. Essas habilitações respondem à pergunta “Esta pessoa pode trabalhar legal ou tecnicamente neste depósito, grupo ou unidade?”. Elas são gerenciadas em uma linha temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, vencido ou próximo a vencer para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto requerido, o motor gera um erro ao tentar escalá-la. fileciteturn38file0L17-L34

Antes de começar esta seção, assegure-se de que:
1. Você já revisou o perfil do motorista.
2. Você já sabe qual depósito, grupo ou unidade será necessário para seu caso.
3. Entende que uma habilitação não é a mesma que uma cessão ou uma adscrição temporária.

Para revisar e validar as habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Cualificações**.
2. Verifique se existem registros vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócio.
3. Comunique-se o estado visual de cada habilitação:
   1. ativa,
   2. futura,
   3. próxima a vencer,
   4. vencida.
4. Se falta uma habilitação necessária, adicione-a com suas datas corretas.
5. Se uma habilitação já venceu e não deveria ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Salve as alterações.
7. Confirme que o motorista já está habilitado para o contexto onde você espera usá-lo.

Para o caso de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho necessário está coberto.
3. Não há vencimentos que quebram a elegibilidade atual.

Quando terminar esta seção, você deveria ter motoristas que não só existem na plantilla, mas também são elegíveis do ponto de vista operacional e normativo. fileciteturn38file0L17-L34

## Confirmando que a plantilla já está pronta para a próxima camada de Rostering

O último passo é verificar que a base de motoristas já está pronta para entrar na próxima camada: adscrição operacional, regras, faltas e disponibilidade. Aqui o objetivo não é apenas ter nomes carregados, mas uma plantilla coerente, trazível e utilizável pelo motor.

Antes de terminar, assegure-se de que:
1. Você já carregou ou importou a plantilla.
2. Você já revisou os perfis principais.
3. Você já verificou dados estruturais e dinâmicos.
4. Você já validou habilitações essenciais.

Para confirmar que a plantilla já está preparada:
1. Volte à lista geral de motoristas.
2. Revise que o coletivo necessário para seu caso está presente.
3. Comprove que os perfis críticos não têm lacunas de informação importantes.
4. Assegure-se de que as pessoas que você espera usar estão habilitadas para o contexto correto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operacional,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referência, termine esta quick start apenas quando você puder afirmar:
1. A plantilha de motoristas de L1 já está carregada.
2. Os perfis-chave já foram revisados.
3. As habilitações essenciais já estão válidas.
4. A base já está pronta para passar à adscrição operativa.

Quando terminar esta seção, você deveria ter uma plantilha de motoristas suficientemente sólida para continuar com a próxima camada de Rostering.

## Leituras adicionais

- [Gestão da adscrição operativa do motorista](P21_Gestão_da_adscrição_operativa_do_motorista.md)