TRABALHO AVALIATIVO

Orientações
A atividade é individual e deverá ser desenvolvida em Python.
Crie uma pasta para a avaliação contendo exatamente os seguintes arquivos:
avaliacao/
├-- questao1.py
├-- questao2.py
├-- questao3.py
└── questao4.py
• Os nomes das classes, funções, métodos e parâmetros especificados nas questões deverão ser mantidos, pois os
programas serão submetidos também a testes automáticos durante a correção.
• Os exemplos apresentados servem apenas para demonstrar algumas situações. Durante a correção poderão ser
utilizados outros valores, inclusive valores de fronteira e situações inválidas não mostradas nos exemplos.
• Não utilize input() nas soluções. Os valores serão fornecidos diretamente às classes e funções durante os testes.
• A atividade deverá ser resolvida utilizando os conteúdos estudados em aula. Não é permitido o uso de ferramentas
de Inteligência Artificial para produzir as respostas(DEUS ESTÁ VENDO)
1. Drone de inspeção — 30 pontos
Um laboratório utiliza drones para realizar inspeções em áreas de difícil acesso.
Cada drone possui um código e uma quantidade de bateria disponível, representada por um valor percentual.
Implemente no arquivo questao1.py a classe:
Drone
-------------------------
codigo
bateria
-------------------------
voar(minutos)
O método voar(minutos) deverá considerar que cada minuto de voo consome 4% da bateria.
As seguintes regras devem ser respeitadas:
• o tempo de voo deverá ser maior que zero;
• se o tempo informado for menor ou igual a zero, a operação não poderá continuar e deverá ser lançada uma
ValueError com a mensagem "Tempo de voo inválido";
• se a bateria disponível não for suficiente para realizar todo o voo solicitado, a operação não poderá
continuar e deverá ser lançada uma ValueError com a mensagem "Bateria insuficiente";
• quando o voo puder ser realizado, a bateria deverá ser reduzida de acordo com o tempo informado;
• uma operação recusada não poderá alterar a bateria do drone;
• ao concluir um voo válido, o método deverá retornar a quantidade de bateria restante.
Exemplo de situação
Um drone com 80% de bateria consegue realizar um voo de 5 minutos e termina com 60%.
Entretanto, sua implementação deverá funcionar corretamente para diferentes valores de bateria e duração de
voo.

2. Definição segura de altitude — 25 pontos
Um drone de inspeção somente pode operar entre 10 e 120 metros de altitude, inclusive.
No arquivo questao2.py, implemente duas funções:
validar_altitude(altitude)
solicitar_altitude(altitude)
A função validar_altitude(altitude) deverá:
• aceitar valores entre 10 e 120;
• retornar a própria altitude quando ela for válida;
• lançar uma ValueError com a mensagem "Altitude não permitida" quando o valor estiver fora da faixa
permitida.
A função solicitar_altitude(altitude) representa a parte do sistema responsável por tentar configurar a altitude.
Ela deverá:
• tentar utilizar validar_altitude;
• caso nenhuma exceção aconteça, retornar:
Altitude definida: X m
• caso ocorra a ValueError lançada pela validação, a exceção deverá ser capturada e tratada, retornando:
Falha: MENSAGEM_DA_EXCEÇÃO
A mensagem utilizada no tratamento deverá ser obtida da própria exceção capturada.
Exemplos de resultados
Para uma altitude válida de 50 metros:
Altitude definida: 50 m
Para uma altitude inválida:
Falha: Altitude não permitida
Outras altitudes serão utilizadas durante a correção.
3. Verificação de uma missão — 25 pontos
Antes de iniciar uma missão, o sistema verifica sua duração planejada.
Uma missão somente poderá possuir duração entre 1 e 60 minutos, inclusive.
No arquivo questao3.py, implemente a função:
executar_verificacao(duracao)
A função deverá criar inicialmente uma lista vazia chamada historico.
Em seguida, deverá realizar a verificação da duração utilizando obrigatoriamente a estrutura completa:
try
except
else
finally
O comportamento deverá ser:
• dentro do try, verificar a duração;
• se ela for menor que 1 ou maior que 60, lançar ValueError com a mensagem "Duração inválida";
• o except deverá capturar essa exceção e acrescentar ao histórico:
ERRO: Duração inválida
• o else deverá acrescentar ao histórico:
Missão liberada
• o finally deverá acrescentar ao histórico:
Verificação encerrada
Ao final, a função deverá retornar a lista historico.

Exemplo de uma missão válida
Para uma duração válida, o resultado deverá possuir:
["Missão liberada", "Verificação encerrada"]
Exemplo de uma missão inválida
Para uma duração inválida:
["ERRO: Duração inválida", "Verificação encerrada"]
Observe que "Verificação encerrada" deverá aparecer independentemente de a operação ter sucesso ou erro.
4. Propagação e tratamento da exceção — 20 pontos
O sistema possui três etapas para configurar a velocidade de voo de um drone.
Implemente no arquivo questao4.py as seguintes funções:
validar_velocidade(velocidade)
configurar_voo(velocidade)
iniciar_missao(velocidade)
Um drone somente poderá operar com velocidade maior que 0 e menor ou igual a 80 km/h.
validar_velocidade(velocidade)
Deverá:
• retornar a velocidade quando ela for válida;
• lançar ValueError com a mensagem "Velocidade inválida" quando a regra não for atendida.
configurar_voo(velocidade)
Deverá utilizar validar_velocidade(velocidade).
Essa função não deverá capturar a exceção.
Se a velocidade for válida, deverá retornar:
Velocidade configurada: X km/h
Se uma exceção ocorrer em validar_velocidade, ela deverá continuar seu caminho normalmente até quem chamou
configurar_voo.
iniciar_missao(velocidade)
Esta será a responsável por reagir ao possível problema.
Ela deverá:
• tentar executar configurar_voo;
• se não ocorrer exceção, retornar o resultado da configuração;
• se ocorrer ValueError, capturá-la e retornar:
Missão cancelada: MENSAGEM_DA_EXCEÇÃO
Exemplo
Uma velocidade permitida deverá produzir algo como:
Velocidade configurada: 60 km/h
Uma velocidade não permitida deverá produzir:
Missão cancelada: Velocidade inválida
Durante a correção serão utilizadas outras velocidades para verificar tanto o funcionamento normal quanto a
propagação e o tratamento da exceção.
