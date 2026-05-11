---
title: Carregar e Gerenciar Condutores
shortTitle: Condutores
intro: 'Aprenda a criar, importar e manter a base de condutores no GoalBus, revisar o seu perfil operativo e deixar uma planilha confiável antes de passar à adscrição, regras e cálculo de Rostering.'
contentType: tutoriais
versions:
  - '*'
---

## Criando a plantilla de condutores

Antes de falar de regras de Rostering, ausências ou atribuição de turnos, precisa ter uma base confiável de condutores. No GoalBus, a gestão de condutores atua como a fonte principal de verdade para a operação: permite combinar criação manual e carga masiva, e concentra identidade, afiliação ao depósito e disponibilidade num único diretório. 

fileciteturn38file2L1-L24


Usa esta quick start quando já tiver a transição clara de Scheduling para Rostering e necessite preparar o colectivo real de pessoas que participará na atribuição.

Antes de começar, certifique-se de que:
1. Já encerrou a transição de Scheduling em P19.
2. Tem claro qual o colectivo de condutores que participará no cálculo.
3. Sabe se vai dar de alta poucos condutores manualmente ou se precisa de uma carga masiva.
4. Tem acesso ao ambiente com permissões para gerenciar pessoal.

Para esta quick start, usa este caso de referência:

> **Vou carregar e revisar a plantilla de condutores que poderá cobrir a solução de L1 antes de entrar em adscripción, regras e disponibilidade.**

Para criar ou importar a plantilla de condutores:
1. No GoalBus, vá ao módulo de **Configuração** > **Personal** > **Gestión de Condutores**.
ref: P20_Imagen1.png | compact
2. Revise se os condutores do caso já existem na lista geral.
3. Se precisar criar poucos condutores, clique em **Novo Condutores**.
ref: P20_Imagen2.png | compact(2x)
4. Se precisar carregar muitos condutores, realize uma importação em massa através de arquivo CSV a partir de **Carga Personal**.
ref: P20_Imagen3.png | compact
5. Se optar por importação em massa, prepare o arquivo com os dados mínimos que a sua operação precisa para identificar corretamente cada pessoa. A janela de importação actuará de ajuda para preparar o CSV de carga.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e verifique se os condutores aparecem corretamente.
8. Se detectar duplicados ou registros incompletos, corrija-os antes de prosseguir.

Para o caso de referência, termina esta seção apenas puder afirmar:
1. Os motoristas da L1 já estão dados de alta ou importados.
2. A lista geral reflete uma única plantilla de referência.
3. Já pode abrir o perfil de cada motorista para verificar o seu contexto operativo.

Quando terminar esta seção, deverias ter uma plantilla de motoristas carregada e visível no sistema. fileciteturn38file0L1-L7
fileciteturn38file2L1-L24

## Revisando o perfil do motorista e seus dados estruturais

Uma vez criada a plantilla, precisa verificar o **perfil do motorista**. O perfil não é apenas uma ficha de contacto: é o expediente digital completo do funcionário dentro da operação. Ahí convivem dados estáticos, contexto operativo e atributos que o sistema usará mais tarde para analisar a sua elegibilidade. fileciteturn38file0L8-L20
fileciteturn38file2L25-L40

Antes de começar esta seção, certifique-se de que:
1. Já tem motoristas visíveis na lista geral.
2. Já sabe qual motorista ou qual grupo usará como amostra.
3. Quer validar que o registro não é apenas administrativo, mas operativo.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral de dados estáticos.
3. Verifique pelo menos estes grupos de informação:
   1. dados básicos, como nome e código,
   2. dados operativos, como convênio coletivo ou tipo de contrato,
   3. links operativos, como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se algum dado estrutural for ausente, complemente-o antes de continuar.
5. Salve qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar consistência na plantilla.

Para o caso de referência, revisa ao menos:
1. O código do motorista.
2. O seu depósito principal.
3. O seu grupo de trabalho.
4. As propriedades operacionais que condicionarão a sua atribuição posterior.

Quando termines esta seção, deberias ter claro que cada motorista tem um expediente operativo coerente e utilizável. fileciteturn38file0L8-L20

## Revisando o contexto operativo e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista inclui dados dinâmicos que afetam diretamente a forma como o sistema razona sobre a pessoa. Na aba de administração, podes revisar contadores e padrões de trabalho, que formam parte do contexto operativo usado mais tarde pela lógica de atribuição. fileciteturn38file0L12-L17

Antes de começar esta seção, asegúrate de que:
1. Já revisaste os dados estáticos do perfil.
2. Já sabes se a tua operação usa contadores ou padrões cíclicos.
3. Queres verificar que o motorista não só existe, mas que tem um contexto operativo interpretable.

Para revisar o contexto operativo dinâmico:
1. Dentro do perfil do motorista, abre a aba de **Detalhes de administração**.
2. Revisa os **contadores** ou KPI associados ao motorista se existem.
3. Verifica se o motorista está vinculado a algum **padrão de trabalho**.
4. Se a tua operação usa padrões cíclicos, revisa também o desfase ou posição atual do motorista dentro do padrão.
5. Confirma que estes dados têm sentido para o contexto real.
6. Se a informação dinâmica não for correta, ajusta-a antes de passar a regras ou cálculo.

## Validando Habilitações Antes de Usar o Conductor no Rostering

Antes de considerar um conductor como elegível, precisa verificar as suas **habilitaciones**. Estas habilitaciones respondem à pergunta "¿Esta pessoa pode trabalhar legal ou técnicamente neste depósito, grupo ou unidade?" Estas habilitaciones são geridas num intervalo temporal com data de início e fim, e o sistema mostra estados como ativo, futuro, caducado ou próximo a caducar para facilitar a leitura. Se uma pessoa não estiver habilitada para o contexto exigido, o motor gera um erro ao tentar atribuí-la. 

## Antes de Começar esta Seção, Certifique-se de que:

1. Já revisou o perfil do conductor.
2. Já sabe qual depósito, grupo ou unidade precisará para o seu caso.
3. Compreende que uma habilitação não é o mesmo que uma cesão ou uma adscrição temporal.

Para revisar e validar as habilitaciones:

1. Dentro do perfil do conductor, abra a aba **Habilitações / Cualificaciones**.
2. Verifique se existem registros vigentes para:
   1. Depósitos,
   2. Grupos de trabalho,
   3. Unidades de negócio.
3. Verifique o estado visual de cada habilitação:
   1. Ativa,
   2. Futura,
   3. Próxima a caducar,
   4. Caducada.
4. Se falta uma habilitação necessária, adicione-a com as datas corretas.
5. Se uma habilitação já caducou e não deve ser utilizada, deixe-a como histórico sem tentar reescrever o passado.
6. Salve os alterações.
7. Confirme que o conductor já está habilitado para o contexto onde pretende utilizá-lo.

Para o caso de referência, não continue até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho requerido está coberto.
3. Não há caducidades que rompam a elegibilidade atual.

Quando terminar esta seção, deverias ter motoristas que não só existem na planilha, mas também são elegíveis desde o ponto de vista operativo e normativo. 

## Confirmando que a planilha já está lista para a próxima capa de Rostering

O último passo é verificar que a base de motoristas já está lista para entrar na próxima capa: adscrição operativa, regras, ausências e cálculo. Aqui o objetivo não é apenas ter nomes carregados, mas uma planilha coerente, rastreável e utilizável pelo motor.

Antes de terminar, certifique-se de que:
1. Já carregou ou importou a planilha.
2. Já revisou os perfis principais.
3. Já verificou dados estruturais e dinâmicos.
4. Já validou habilitacões essenciais.

Para confirmar que a planilha já está preparada:
1. Volte à lista geral de motoristas.
2. Revise que o colectivo necessário para o seu caso está presente.
3. Verifique se os perfis críticos não têm furos de informação importantes.
4. Certifique-se de que as pessoas que esperas usar estão habilitadas para o contexto correto.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referência, termina esta quick start apenas quando puder afirmar:
1. A plantilla de motoristas da L1 já está carregada.
2. Os perfis chave já foram revisados.
3. As habilitações essenciais já estão vigentes.
4. A base já está lista para passar à adscrição operacional.

Quando terminar esta seção, deverás ter uma plantilla de motoristas suficientemente sólida como para continuar com a próxima etapa de Rostering.

## Leitura adicional

- [Gestão da adscrição operacional do motorista](P21_Gestão_da_adscrição_operacional_do_motorista.md)