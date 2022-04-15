# String Client-Server RPC

- [Introdução](#Introdução)
- [Dependencias](#Dependências)
- [Vídeo Demonstrativo](#Vídeo-Demonstrativo)

# Introdução

Essa aplicação implementa um par cliente-servidor utilizando RPC que realiza operações entre duas strings. Tais operações incluem: Concatenação, Distancia de Levenshtein e Checagem de igualdade.

Nessa aplicação, quando conectado com o servidor, o cliente consegue realizar chamadas de métodos, que são implementados no servidor, como se fossem métodos locais. Com isso, é possível alcançar-se transparencia de acesso, o que não era possível com uma troca de mensagens convencional em um sistema cliente-servidor com a utilização de sockets, dado que precissavamos utilizar operações de envio (send) e recebimento (receive), os quais não ocultam a comunicação entre as entidades.

# Dependências

- rpyc

# Vídeo Demonstrativo

[Link para o Vídeo](https://drive.google.com/file/d/1BlgyuFZ3uQ0mNN50yZBT6guH5AhLE_kr/view?usp=sharing)
