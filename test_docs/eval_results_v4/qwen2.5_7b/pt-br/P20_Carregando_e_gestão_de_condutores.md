---
title: 'Carregando e gerenciando motoristas'
shortTitle: 'Condutores'
intro: 'Aprenda a criar, importar e manter a base de condutores no GoalBus, revisar seu perfil operacional e deixar uma planta fiável antes de passar para adscrição, regras e cálculo de Rostering.'
contentType: 'how-tos'
versions:
  - '*'
---

## Criando e Importando a Plantilha de Motoristas

Antes de falar sobre regras de Escalas, ausências ou atribuição de escalas, você precisa ter uma base confiável de motoristas. No GoalBus, o gerenciamento de motoristas atua como a fonte principal da verdade para operações humanas: permite combinar criação manual e carga em massa, concentrando identidade, afiliação ao depósito e disponibilidade no mesmo diretório. fileciteturn38file2L1-L24

Use esta quick start quando já tiver clara a transição de Programação para Escalas e precisar preparar o coletivo real de pessoas que participará na atribuição.

Antes de começar, assegure-se de que:
1. Você já encerrou a transição da Scheduling em P19.
2. Você sabe qual coletivo de motoristas participará no cálculo.
3. Você sabe se vai dar alta alguns poucos motoristas manualmente ou precisará realizar uma carga em massa.
4. Você tem acesso ao ambiente com permissões para gerenciar pessoal.

Para esta quick start, use este caso de referência:

> **Vou carregar e revisar a plantilha de motoristas que poderá cobrir a solução L1 antes da adscrição, regras e disponibilidade.**

Para criar ou importar a plantilha de motoristas:
1. No GoalBus, vá ao módulo de **Configuração** > **Pessoal** > **Gerenciamento de Motoristas**.
ref: P20_Imagen1.png | compact
2. Verifique se os motoristas do caso já existem na lista geral.
3. Se precisar criar poucos motoristas, clique em **Novo Motorista**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos motoristas, realize uma importação em massa através de arquivo CSV a partir de **Carga Pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolher importação em massa, prepare o arquivo com os dados mínimos necessários para identificar corretamente cada pessoa. A janela de importação atuará como auxílio para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e verifique que os motoristas aparecem corretamente.
8. Se detectar duplicados ou registros incompletos, corrige-os antes de seguir.

Para o caso de referência, termine esta seção apenas quando puder afirmar:
1. Os motoristas da L1 já estão cadastrados ou importados.
2. A lista geral reflete uma única planilha de referência.
3. Você pode abrir o perfil de cada motorista para revisar seu contexto operacional.

Quando terminar essa seção, você deveria ter um modelo de motoristas carregado e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-24

## Revisando o perfil do motorista e seus dados estruturais

Depois de criar a planilha, você precisa revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contato: é o expediente digital completo do funcionário dentro da operação. Nele convivem dados estáticos, contexto operacional e atributos que o sistema usará mais tarde para raciocinar sobre sua elegibilidade. fileciteturn38file0L7-19 fileciteturn38file2L24-L36

Antes de iniciar esta seção, assegure-se de que:
1. Você já tem motoristas visíveis na lista geral.
2. Você sabe qual motorista ou grupo você usará como amostra.
3. Você quer validar que o registro não é apenas administrativo, mas operacional.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral com os dados estáticos.
3. Verifique pelo menos esses grupos de informações:
   1. dados básicos, como nome e código,
   2. dados operacionais, como convenção coletiva ou tipo de contrato,
   3. enlaces operacionais, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural crucial estiver faltando, complete-o antes de continuar.
5. Salve qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar coerência na planilha.

Para o caso de referência, revise ao menos:
1. O código do motorista.
2. Seu depósito principal.
3. Sua equipe de trabalho.
4. As propriedades operacionais que condicionarão sua atribuição posterior.

Quando terminar esta seção, você deve ter clareza de que cada motorista possui um expediente operacional coerente e utilzável. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente como o sistema raciocina sobre a pessoa. Na aba de administração você pode revisar contadores e padrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica da atribuição. fileciteturn38file0L12-L17

Antes de iniciar esta seção, assegure-se de:
1. Ter já revisado os dados estáticos do perfil.
2. Saber se sua operação usa contadores ou padrões cíclicos.
3. Verificar que o motorista não apenas existe, mas possui um contexto operativo interpretável.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abra a aba de **Detalhes da administração**.
2. Revise os **contadores** ou KPI associados ao motorista se existirem.
3. Verifique se o motorista está vinculado a algum **padrão de trabalho**.
4. Se sua operação usa padrões cíclicos, revise também o deslocamento ou posição atual do motorista dentro do padrão.
5. Confirme que esses dados fazem sentido para o contexto real.
6. Se as informações dinâmicas não forem corretas, ajuste-as antes de passar às regras ou cálculo.

Para o caso de referência, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Seus contadores ou KPI estão disponíveis se o processo os precisar?
3. O sistema poderia raciocinar corretamente sobre esta pessoa em um cálculo de escalas?

Quando terminar essa seção, você deve validar não apenas a identidade do motorista, mas também seu contexto operativo dinâmico. fileciteturn38file0L12-L17

## Validando habilitações antes de usar o motorista na Escalas

Antes de considerar um motorista como elegível, você precisa revisar suas **habilitações**. Essas habilitações respondem à pergunta “essa pessoa pode trabalhar legal ou tecnicamente neste depósito, grupo ou unidade?”. Elas são gerenciadas em uma linha temporal com data inicial e final, e o sistema mostra estados como ativo, futuro, vencido ou próximo a vencer para facilitar a leitura. Se uma pessoa não estiver habilitada no contexto necessário, o motor gera um erro ao tentar escalá-la. fileciteturn38file0L17-L34

Antes de começar esta seção, assegure-se de que:
1. Você já revisou o perfil do motorista.
2. Você já sabe qual depósito, grupo ou unidade será necessário para seu caso.
3. Entende que uma habilitação não é a mesma coisa que um relevo ou adscrição temporária.

Para revisar e validar as habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Qualificações**.
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
5. Se uma habilitação já venceu e não deve ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Salve as alterações.
7. Confirme que o motorista está habilitado para o contexto onde você espera utilizá-lo.

Para o caso de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho necessário está coberto.
3. Não há vencimentos que rompam a elegibilidade atual.

Quando terminar esta seção, você deve ter motoristas que não apenas existem na plantilha, mas também são elegíveis do ponto de vista operacional e normativo. fileciteturn38file0L17-L34

## Confirmando que a planilha já está pronta para a próxima camada de Escalas

O último passo é verificar se a base de motoristas já está pronta para entrar na próxima camada: adscrição operacional, regras, faltas e cálculo. Aqui o objetivo não é apenas ter nomes carregados, mas uma planilha coerente, trazível e utilizável pelo sistema.

Antes de terminar, garanta que:
1. Você já carregou ou importou a plantilha.
2. Você já revisou os perfis principais.
3. Você já verificou dados estruturais e dinâmicos.
4. Você já validou habilitações essenciais.

Para confirmar que a planilha já está preparada:
1. Volte à lista geral de motoristas.
2. Verifique se o coletivo necessário para seu caso está presente.
3. Comunique-se sobre os perfis críticos não terem lacunas importantes de informação.
4. Garanta que as pessoas que você espera usar estão habilitadas no contexto correto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operacional,
   2. regras de Escalas,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referência, termine esta quick start apenas quando você puder afirmar:
1. A planilha de motoristas L1 já está carregada.
2. Os perfis-chave já foram revisados.
3. As habilitações essenciais já estão válidas.
4. A base já está pronta para passar à adscrição operativa.

Quando terminar esta seção, você deveria ter uma planilha de motoristas suficientemente sólida como para continuar com a próxima camada de Escalas.

## Leituras adicionais

- [Gerenciamento da adscripción operativa do motorista](P21_Gerenciamento_da_adscrição_operativa_do_motorista.md)