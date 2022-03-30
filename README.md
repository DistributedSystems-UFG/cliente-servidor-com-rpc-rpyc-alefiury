# String Client-Server RPC

Essa aplicação implementa um par cliente-servidor utilizando RPC que realiza operações entre duas strings.

Nessa aplicação, quando conectado com o servidor, o cliente consegue realizar chamadas de métodos, que são implementados no servidor, como se fossem métodos locais. Com isso, é possível alcançar-se transparencia de acesso, o que não era possível com uma troca de mensagens convencional em um sistema cliente-servidor com a utilização de sockets, dado que precissavamos utilizar operações de envio (send) e recebimento (receive), os quais não ocultam a comunicação entre as entidades.

## Vídeo Demonstrativo

[Link para o Vídeo]()