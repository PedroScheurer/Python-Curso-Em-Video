import try3

arqProducao = 'teste.txt'

if not try3.arquivoExiste(arqProducao):
    try3.criarArquivo(arqProducao)

try3.menu(arqProducao)