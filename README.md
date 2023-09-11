# Flyfood

Projeto FlyFood

Estamos no ano de 2025 e nesse futuro não tão distante o trânsito está caótico. As empresas de delivery já não conseguem fazer entregas em um tempo aceitável e o custo com entregadores está muito alto, pois mão-de-obra humana está cada vez mais valorizada devido à grande oferta de empregos (ok… essa última parte é mais sonho do que realidade, mas vamos considerá-la). Então, um ex-aluno do BSI-UFRPE resolve criar uma empresa chamada FlyFood para fazer entregas utilizando drones.

Essas máquinas voadoras fantásticas podem receber uma rota de entregas e executá-las à risca. Ou seja, elas podem voar desde o local de origem do pedido (por exemplo, restaurante ou lanchonete) com vários pedidos no seu compartimento de carga e entregar em vários endereços espalhados na cidade. Essa capacidade de sair com vários pedidos otimiza bastante o tempo de entrega dos pedidos. No entanto, nem tudo são flores. A capacidade das baterias dos drones continuam sendo um problema. Sendo assim, é preciso otimizar ao máximo o trajeto do drone para conseguir concluir todas as entregas dentro do ciclo da bateria.

Com esse cenário em vista, já nos dias atuais (2021) o empreendedor da FlyFood vai começar a desenvolver um algoritmo de roteamento. Ou seja, um algoritmo que seja capaz de definir o menor trajeto para a realização de todas as entregas do drone.

Para abstrair as questões de encontrar endereços e obter coordenadas GPS, vamos trabalhar com uma matriz que representa os pontos da cidade. Veja um exemplo de matriz logo a seguir:

Seu trabalho será elaborar um algoritmo que vai ler uma matriz, a partir de um arquivo, com os pontos de entrega e o ponto de origem e retorno. Ele deverá retornar a ordem em que o drone deve percorrer os pontos de entrega. Essa ordem deve ser a de menor custo, ou seja, a que o drone vá percorrer a menor distância em dronômetros.

O formato do arquivo de entrada será o seguinte para a matriz de exemplo.

4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0


Sua resposta deverá ser a sequência de pontos (em forma de string) que produz o menor circuito possível a ser percorrido pelo drone entre os pontos de entrega, partindo e retornando ao ponto R (o ponto R não precisa ser incluído na sequência de resposta). Por exemplo: "A D C B". (errata: Se existir mais de um trajeto com a menor distância, basta retornar um deles.)

Divirta-se!
