I developed a two-layer distributed application using Python Socket Programming as part of a computer networks lab project. The application structure includes a total of 13 servers - one central, three language-specific, and nine genre-specific servers.

The first layer of the application was designed to manage language-specific requests, incorporating three servers catering to Telugu, Hindi, and English literature respectively.

The second layer consists of nine servers, each connected to a language server, hosting books of three various genres: horror, detective, and technical.

A central server mediates communication between the client and the first layer of servers, facilitating seamless operations and interaction.

The application employs multi-threading techniques to handle multiple clients simultaneously, enhancing system efficiency and responsiveness. Overall, this setup ensures organized, manageable, and efficient distribution of digital library resources.
