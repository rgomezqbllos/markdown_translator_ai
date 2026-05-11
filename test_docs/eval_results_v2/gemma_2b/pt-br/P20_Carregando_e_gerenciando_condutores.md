---
title: Carregando e gerenciando motoristas
shortTitle: Motoristas
intro: Aprende a criar, importar e manter a base de motoristas no GoalBus, revisar seu perfil operacional e deixar uma planilha confiável antes de passar à adscrição, regras e cálculo de Escalas.
contentType: how-tos
versions:
  - '*'
---

## Criando a plantilla de condutores

Antes de falar de regras de Escalas, ausencias ou alocação de turnos, você precisa ter uma base confiável de condutores. No GoalBus, a gestão de condutores atua como a fonte principal de verdade para a operação: permite combinar criação manual e carga masiva, e concentra identidade, afiliação ao depósito e disponibilidade em um mesmo diretório. 

fileciteturn38file2L1-L24


Use esta quick start quando já tiver claro a transição de Programação para Escalas e necessite preparar o conjunto real de pessoas que participará da alocação.

Antes de começar, certifique-se de que:
1. Já encerrou a transição de Programação em P19.
2. Tem claro qual o conjunto de condutores que participará no cálculo.
3. Sabe se vai dar alta poucos condutores manualmente ou se precisa de uma carga masiva.
4. Tem acesso ao ambiente com permissões para gerenciar pessoal.

Para esta quick start, use este caso de referência:

> **Vou carregar e revisar a plantilla de condutores que poderá cobrir a solução de L1 antes de entrar em adscripción, regras e disponibilidade.**

Para criar ou importar a plantilla de condutores:
1. No GoalBus, vá para o módulo de **Configuração** > **Personal** > **Gerenciamento de Condutores**.
ref: P20_Imagen1.png | compact
2. Verifique se os condutores do caso já existem na lista geral.
3. Se precisar criar poucos condutores, clique em **Novo Condutores**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos condutores, realize uma importação em massa através de arquivo CSV a partir de **Carga Personal**.
ref: P20_Imagen3.png | compact
5. Se optar por importação em massa, prepare o arquivo com os dados mínimos que sua operação precisa para identificar corretamente cada pessoa. A janela de importação irá auxiliar na preparação do CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e verifique se os condutores aparecem corretamente.
8. Se detectar duplicatas ou registros incompletos, corrija-os antes de prosseguir.

Para o caso de referência, termine esta seção apenas possa afirmar:
1. Os motoristas da L1 já estão dados de alta ou importados.
2. A lista geral reflete uma única plantilla de referência.
3. Já é possível abrir o perfil de cada motorista para revisar seu contexto operacional.

Quando terminar esta seção, você deve ter uma plantilla de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7 Tully fileciteturn38file2L1-L24 Tully

## Revisando o perfil do motorista e seus dados estruturais

Uma vez criada a plantilla, você precisa revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contato: é o expediente digital completo do funcionário dentro da operação. Ahí convivem dados estáticos, contexto operacional e atributos que o sistema usará mais tarde para analisar sua elegibilidade. fileciteturn38file0L8-L20 Tully fileciteturn38file2L25-L40 Tully

Antes de começar esta seção, certifique-se de que:
1. Já tem motoristas visíveis na lista geral.
2. Já sabe qual motorista ou qual grupo usará como amostra.
3. Quer validar que o registro não é apenas administrativo, mas operacional.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral de dados estáticos.
3. Verifique pelo menos estes grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operacionais, como convênio coletivo ou tipo de contrato,
   3. links operacionais, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural for crucial, complete-o antes de prosseguir.
5. Salve qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar consistência na plantilla.

Para o caso de referência, revise ao menos:
1. O código do motorista.
2. Seu depósito principal.
3. Seu grupo de trabalho.
4. As propriedades operacionais que condicionarão sua atribuição posterior.

Quando terminar esta seção, você deve ter claro que cada motorista possui um expediente operacional coerente e utilizável. 

## Revisando o contexto operacional e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente a forma como o sistema raciocina sobre a pessoa. Na aba de administração, você pode revisar contadores e padrões de trabalho, que fazem parte do contexto operacional usado posteriormente pela lógica de atribuição. 

Antes de começar esta seção, certifique-se de que:
1. Já revisou os dados estáticos do perfil.
2. Já sabe se sua operação usa contadores ou padrões cíclicos.
3. Quer verificar se o motorista não só existe, mas tem um contexto operacional interpretado.

Para revisar o contexto operacional dinâmico:
1. Dentro do perfil do motorista, abra a aba de **Detalhes de administração**.
2. Revise os **contadores** ou KPIs associados ao motorista se existirem.
3. Verifique se o motorista está vinculado a algum **padrão de trabalho**.
4. Se sua operação usa padrões cíclicos, revise também o desfase ou posição atual do motorista dentro do padrão.
5. Confirme que esses dados têm sentido para o contexto real.
6. Se a informação dinâmica não estiver correta, ajuste-a antes de passar para regras ou cálculo.

## Validando Habilitaciones antes de usar o Conductor em Escalas

Antes de considerar um motorista como elegível, você precisa revisar suas **habilitaciones**. Essas habilitaciones respondem à pergunta "Esta pessoa pode trabalhar legal ou técnicamente neste depósito, grupo ou unidade?". Elas são gerenciadas em uma linha temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, caducado ou próximo a caducar para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto exigido, o motor gera um erro ao tentar atribuí-la. 

## Antes de começar esta seção, certifique-se de que:
1. Já revisou o perfil do motorista.
2. Já sabe qual depósito, grupo ou unidade será necessário para seu caso.
3. Entende que uma habilitação não é o mesmo que uma cesão ou uma adscrição temporal.

Para revisar e validar as habilitaciones:
1. Dentro do perfil do motorista, abra a aba **Habilitaciones / Qualificações**.
2. Verifique se existem registros vigentes para:
   1. Depósitos,
   2. Grupos de trabalho,
   3. Unidades de negócio.
3. Verifique o estado visual de cada habilitação:
   1. Ativa,
   2. Futura,
   3. Próxima a caducar,
   4. Caducada.
4. Se falta uma habilitação necessária, adicione-a com suas datas corretas.
5. Se uma habilitação já caducou e não deve ser usada, deixe-a como histórico sem tentar reescrever o passado.
6. Salve os cambios.
7. Confirme que o motorista já está habilitado para o contexto onde espera usá-lo.

Para fins de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade atual.

Quando terminar esta seção, você deve ter motoristas que não só existem na planilha, mas também são elegíveis desde o ponto de vista operacional e normativo. 

## Confirmando que a planilha já está pronta para a próxima camada de Escalas

O último passo é verificar se a base de motoristas já está pronta para entrar na próxima camada: adscrição operacional, regras, ausências e cálculo. Aqui, o objetivo não é apenas ter nomes carregados, mas uma planilha coerente, rastreável e utilizável pelo motorista.

Antes de terminar, certifique-se de que:
1. Já carregou ou importou a planilha.
2. Já revisou os perfis principais.
3. Já verificou dados estruturais e dinâmicos.
4. Já validou habilitacões essenciais.

Para confirmar que a planilha já está pronta:
1. Volte à lista geral de motoristas.
2. Verifique se o coletivo necessário para o seu caso está presente.
3. Verifique se os perfis críticos não possuem lacunas de informações importantes.
4. Certifique-se de que as pessoas que você espera usar estão habilitadas para o contexto correto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operacional,
   2. regras de Escalas,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo passo rápido.
7. Se a resposta for não, corrija a base de motoristas antes de continuar.

Para o caso de referência, finalize esta quick start somente quando você conseguir afirmar:
1. A plantilla de motoristas da linha L1 já está carregada.
2. Os perfis chave já foram revisados.
3. As habilitações essenciais já estão vigentes.
4. A base já está pronta para passar à adscrição operacional.

Quando terminar essa seção, você deve ter uma plantilla de motoristas suficientemente sólida para continuar com a próxima etapa de Escalas.

## Leitura adicional

- [Gestão da adscrição operacional do motorista](P21_Gestão_da_adscrição_operacional_do_motorista.md)