# AntiScrapping-Toolkit

Esse repositório tem como objetivo apresentar informações e códigos sobre bloqueios durante webscrapping, como acontecem e o que podemos fazer para lidar com cada um deles. Será separado por tópicos, seguindo uma ordem natural de aprendizado.
Vamos começar então.

## O que um servidor vê?

Não tem como falar sobre isso sem antes dar uma introdução sobre o protocolo HTTP. Esse protocolo é a principal forma de conexão entre cliente/servidor, e durante esse processo, algumas informações do cliente são compartilhadas com o servidor. Vamos citar as principais:

1. **Headers**:
   Durante uma requisição, um cabeçalho é enviado obrigatoriamente para o servidor com algumas informações. Vamos dar destaque a um especificamente: *User-Agent*. Esse dado contém algumas informações importantes que podem contribuir para bloqueios, como por exemplo: navegador e versão do mesmo; sistema operacional e arquitetura; dispositivo; motor de renderização; compatibilidade. Aqui podemos ver um exemplo típico de useragent:

   ```plaintext
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
   ```

   Essa informação é importante, mas sozinha, não é de grande ajuda. Qualquer pessoa que estiver usando o mesmo sistema operacional e uma versão mais atual de um mesmo navegador pode ter o mesmo useragent. Porém, durante a comunicação HTTP, mais uma informação é informada: o endereço IP. Isso é feito no momento da conexão com o servidor. Com essas duas informações em mãos, um sistema básico de bloqueio já pode ser implementado. Afinal, se um mesmo useragent em um mesmo endereço IP começa a fazer várias requisições, já dá pra detectar que se trata de um mesmo usuário (apesar de não ser 100% das vezes, já que IP's podem ser compartilhados por diversos usuários, como em redes públicas). Com isso em mente, desenvolvi uma API bem básica apenas para demonstrar. Ela bloqueia o usuário após 5 requisições feitas, mas ao trocar o useragent, já não conseguimos identificar que é o mesmo usuário e o bloqueio é desfeito:
