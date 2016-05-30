#al043
# Daniela Duarte - 78542
# Pedro Guerreiro - 78264 
#Joao Esteves - 78304
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
from janela_sopa_letras import *
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                              |
#                                                                              |
#                              ----TAIS----                                    |
#                                                                              |
#                                                                              |
#||||||||||||||||||||||||||||||TIPO DIRECAO|||||||||||||||||||||||||||||||||||||

# RECONHECEDORES:

def e_direcao(arg):
    ''' 
    e_direcao: universal ---> logico
    e_direcao (arg) recebe qualquer argumento, e devolve um valor
    logico, que determina se o argumento e uma direcao ou nao.
    '''
    
    direcoes = ['N', 'S', 'E', 'W','NE', 'NW', 'SE', 'SW']
    return arg in direcoes


def e_norte(D):
    '''
    e_norte: direcao ---> logico
    e_norte(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao norte
    '''    
    return D == 'N'



def e_sul(D):
    '''
    e_sul: direcao ---> logico
    e_sul(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao sul
    '''    
    return D == 'S'

def e_leste(D):
    '''
    e_leste: direcao ---> logico
    e_leste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao leste
    '''    
    return D == 'E'

def e_oeste(D):
    '''
    e_oeste: direcao ---> logico
    e_oeste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao oeste
    '''    
    return D == 'W'

def e_nordeste(D):
    '''
    e_nordeste: direcao ---> logico
    e_nordeste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao nordeste
    '''    
    return D == 'NE'   

def e_noroeste(D):
    '''
    e_noroeste: direcao ---> logico
    e_noroeste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao noroeste
    '''    
    return D == 'NW' 

def e_sudeste(D):
    '''
    e_sudeste: direcao ---> logico
    e_sudeste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao sudeste
    '''    
    return D == 'SE'   

def e_sudoeste(D):
    '''
    e_sudoeste: direcao ---> logico
    e_sudoeste(D) recebe como argumento uma direcao e devolve um valor logico,
    comparando se a direcao fornecida e a direcao oeste
    '''    
    return D == 'SW'


# Testes:

def direcoes_iguais(D1,D2):
    '''
    direcoes_iguais: direcao x direcao ---> logico
    direcoes_iguais(D1,D2) recebe como argumentos duas direcoes e devolve um
    valor logico dependendo se sao iguais ou nao.
    '''
    return D1 == D2

    
#OUTRAS OPERACOES

def direcao_oposta(D):
    '''
    direcao_oposta: direcao ---> direcao
    direcao_oposta(D) recebe uma direcao e devolve a direcao contraria
    '''
    dir_op = {'N':'S','S':'N','E':'W','W':'E','NW':'SE',\
              'NE':'SW','SE':'NW','SW':'NE'}
    return dir_op[D]
    
#||||||||||||||||||||||||||||||TIPO COORDENADA||||||||||||||||||||||||||||||||||

# CONSTRUTORES

def coordenada(l, c, d):
    '''
    coordenada: int x int x direcao --> coordenada
    coordenada(l, c, d) recebe dois inteiros e uma direcao, e devolve
    a representacao da coordenada
    '''
    
    if isinstance(l, int) and isinstance(c, int) and e_direcao(d) and l >= 0 and c >= 0:
        return [l, c, d]
    raise ValueError ('coordenada: argumentos invalidos')
    
# SELETORES

def coord_linha(c):
    '''
    coordenada_linha: coordenada --> int
    coordenada_linha(c) recebe como argumento uma coordenada, 
    e devolve a linha dessa coordenada
    '''
    return c[0]
    
def coord_coluna(c):
    '''
    coordenada_coluna: coordenada --> int
    coordenada_coluna(c) recebe como argumento uma coordenada, 
    e devolve a coluna dessa coordenada
    '''
    return c[1]

def coord_direcao(c):
    '''
    coordenada_direcao: coordenada --> direcao
    coordenada_direcao(c) recebe como argumento uma coordenada 
    e devolve a direcao dessa coordenada
    '''    
    
    return c[2]

# RECONHECEDOR

def e_coordenada(arg):
    '''
    e_coordenada: argumento --> logico
    e_coordenada(arg) recebe qualquer argumento, e diz se 
    e coordenada ou nao 
    '''
    
    if isinstance(arg, list) and len(arg) == 3 and isinstance(coord_linha(arg), int) \
       and isinstance(coord_coluna(arg), int) and e_direcao(coord_direcao(arg))\
       and coord_linha(arg) >= 0 and coord_coluna(arg) >= 0:
        return True 
    return False
    
 
# TESTES

def coordenadas_iguais(c1, c2):
    '''
    coordenadas_iguais: coordenada x coordenada --> logico
    coordenadas_iguais(c1, c2): recebe duas coordenadas e devolve 
    o valor verdadeiro se as coordenadas c1 e c2 forem iguais e 
    falso caso contrario
    '''
    return coord_linha(c1) == coord_linha(c2) and coord_coluna(c1) == coord_coluna(c2) and direcoes_iguais(coord_direcao(c1), coord_direcao(c2))
    
    
# OUTRAS OPERACOES

def coordenada_string(c):
    '''
    coordenada_string: coordenada --> string
    coordenada_string(c): recebe uma coordenada e devolve a representacao 
    externa de c, sob a forma de string
    '''
    return '(' + str(coord_linha(c)) + ', ' + str(coord_coluna(c))\
               + ')' + '-' + str(coord_direcao(c))

#|||||||||||||||||||||||||||||||Tipo Grelha|||||||||||||||||||||||||||||||||||||

#CONSTRUTOR 

def grelha(lst):
    '''
    grelha: lst ---> grelha
    grelha(g), recebe uma lista de strings que representa a 'sopa de letras' 
    e devolve o tipo grelha.
    '''    
    if isinstance(lst, list) and lst != []:
        for i in lst:
            if not isinstance(i, str) or len(lst[0]) != len(i):
                raise ValueError('grelha: argumentos invalidos')
        return lst
    raise ValueError ('grelha: argumentos invalidos')

#SELETORES

def grelha_nr_linhas(g):
    '''
    grelha_nr_linhas: grelha ---> int >= 0
    grelha_nr_linhas(g) recebe uma grelha e devolve o numero de linhas da 
    grelha
    '''    
    return len(g)

def grelha_nr_colunas(g):
    '''
    grelha_nr_colunas: grelha ---> int >= 0
    grelha_nr_colunas(g) recebe uma grelha e devolve o numero de coluna da 
    grelha
    '''    
    return len(g[0])

def grelha_elemento(g, l, c):
    '''
    grelha_elemento: grelha x int >= 0 x int >=0 ---> str
    grelha_elemento(g, l , c) devolve o elemento que se encontra na posicao l, c
    da grelha
    '''    
    if  0 <= l < grelha_nr_linhas(g) and 0 <= c < grelha_nr_colunas(g):
        return g[l][c]
    else:
        raise ValueError('grelha_elemento: argumentos invalidos')
    
def grelha_linha(g, c):
    '''
    grelha_linha: grelha x coordenada ---> str
    grelha_linha(g, cord) devolve a cadeia de caracteres que corresponde a linha inteira
    definida segundo a direcao dada pela coordenada c, e que inclui a posicao
    dada pela mesma coordenada
    '''  
    if 0 <= coord_linha(c) < grelha_nr_linhas(g) and 0 <= coord_coluna(c) < grelha_nr_colunas(g):
        if e_sul(coord_direcao(c)):
            guarda_el = ''                
            for n in range(grelha_nr_linhas(g)):
                guarda_el = guarda_el + grelha_elemento(g,n,coord_coluna(c))
            return guarda_el
            
        elif e_norte(coord_direcao(c)):
            return inv_string(grelha_linha(g,coordenada(coord_linha(c),coord_coluna(c),'S')))
            
        elif e_leste(coord_direcao(c)):
            guarda_el = ''                
            for n in range(grelha_nr_colunas(g)):
                guarda_el = guarda_el + grelha_elemento(g,coord_linha(c),n)
            return guarda_el       
            
        elif e_oeste(coord_direcao(c)):
            return inv_string(grelha_linha(g,coordenada(coord_linha(c),coord_coluna(c),'E'))) 
            
        elif e_noroeste(coord_direcao(c)):
            n=1
            if coord_coluna (c) == grelha_nr_colunas(g) -1 or coord_linha (c) == grelha_nr_linhas(g) -1:
                guarda_el = grelha_elemento (g,coord_linha(c), coord_coluna(c))                               
                while coord_linha(c)-n >= 0 and coord_coluna(c)-n >=0:
                    guarda_el = guarda_el + grelha_elemento(g,coord_linha(c)- n, coord_coluna(c)-n)
                    n=n+1
                return guarda_el
            else:
                c_linha = coord_linha(c)
                c_coluna = coord_coluna(c)
                while c_linha != grelha_nr_linhas(g)-1 and c_coluna != grelha_nr_colunas(g)-1:
                    c_linha = c_linha + n
                    c_coluna = c_coluna + n
                return grelha_linha(g,[c_linha,c_coluna,coord_direcao(c)])
                
        elif e_nordeste(coord_direcao(c)):
            n=1
            if coord_coluna (c) == 0 or coord_linha(c) == grelha_nr_linhas(g)-1:
                guarda_el = grelha_elemento (g,coord_linha(c), coord_coluna(c))                               
                while coord_linha(c)-n >= 0 and coord_coluna(c)+ n < grelha_nr_colunas(g):
                    guarda_el = guarda_el + grelha_elemento(g,coord_linha(c)- n, coord_coluna(c)+n)
                    n=n+1
                return guarda_el
            else: 
                c_linha = coord_linha(c)
                c_coluna = coord_coluna(c)
                while c_linha != grelha_nr_linhas(g)-1 and c_coluna != 0:
                    c_linha = c_linha + n
                    c_coluna = c_coluna - n
                return grelha_linha(g,[c_linha,c_coluna,coord_direcao(c)])
                
        elif e_sudoeste(coord_direcao(c)):
            return inv_string(grelha_linha(g,coordenada(coord_linha(c),coord_coluna(c),'NE')))
        
        elif e_sudeste(coord_direcao(c)):
            return inv_string(grelha_linha(g,coordenada(coord_linha(c),coord_coluna(c),'NW')))
    raise ValueError ('grelha_linha: argumentos invalidos')

def inv_string(string):
    inverte = ''
    for c in range(len(string)-1,-1,-1):
        inverte = inverte + string[c]
    return inverte
        

#RECONHECEDOR

def e_grelha(arg):
    '''
    e_grelha: universal ---> logico
    e_grelha(arg) recebe qualquer argumento e devolve um valor logico que determina se este e uma grelha ou nao
    '''
    if isinstance(arg, list) and arg != []:
        for i in range (len(arg)):
            if not isinstance(arg[i], str) or len(arg[0]) != len(arg[i]):
                return False
        return True    
    return False

#TESTES

def grelhas_iguais(g1, g2):
    '''
    grelhas_iguais: grelha x grelha ---> logico
    grelhas_iguais(g1, g2) recebe como argumentos duas grelhas e devolve um valor logico que determina se as mesmas
    sao iguais ou nao
    '''
    if grelha_nr_linhas(g1)!= grelha_nr_linhas(g2) or grelha_nr_colunas(g1)!= grelha_nr_colunas(g2):
        return False
    else:
        for l in range (grelha_nr_linhas(g1)):
            for c in range (grelha_nr_colunas(g1)):
                if grelha_elemento(g1, l, c) != grelha_elemento(g2, l, c):
                    return False
            return True


#|||||||||||||||||||||||||||| O TIPO RESPOSTA|||||||||||||||||||||||||||||||||||

# CONSTRUTOR

def resposta (lst):
    '''
    resposta: lst ---> resposta
    resposta(lst) recebe uma lista e devolve a representacao 
    da resposta
    '''        
    if isinstance (lst,list):
        if lst != []:
            for i in lst :
                if not isinstance (i,tuple) or not isinstance(i[0],str) \
                   or not e_coordenada(i[1]):
                    raise ValueError ('resposta: argumentos invalidos')
            return res_ordena(lst)
        return lst
    raise ValueError ('resposta: argumentos invalidos')

# esta funcao somente verifica se o argumento e uma lista, se cada elemento
# da lista e um tuplo e se cada tuplo e' constituido por uma string e coord



# SELECTORES

def resposta_elemento (res,n): 
    '''
    resposta_elemento: resposta x int >= 0 ---> tuplo
    resposta_elemento(res,n) recebe um argumento do tipo resposta e
    um numero inteiro e devolve o enesimo elemento da resposta
    '''       
    if  n < 0 or n >= resposta_tamanho(res):
        raise ValueError ('resposta_elemento: argumentos invalidos')
    return res[n]

def resposta_tamanho(res):
    '''
    resposta_tamanho: resposta ---> int
    resposta_tamanho(res) recebe um argumento do tipo resposta e devolve
    o tamanho da mesma, ou seja, o numero de elementos que a constitui
    '''       
    return len(res)


# MODIFICADORES


def acrescenta_elemento(r,s,c):  # mal probably
    '''
    acrescenta_elemento: resposta x string x coordenada ---> resposta
    acrescenta_elemento(r,s,c) recebe um argumento do tipo resposta,
    uma string e uma coordenada, acrescentado, nessa mesma resposta, 
    o tuplo (s,c)
    '''       
    return res_ordena(r + [(s,c)])



# RECONHECEDOR
    
def e_resposta(arg):
    '''
    e_resposta: universal ---> logico
    e_resposta(arg) recebe um argumento e devolve um valor logico, determinando se e uma resposta ou nao
    '''       
    if isinstance (arg,list):
        for i in range(len(arg)) :
            if not isinstance (arg[i],tuple) or not isinstance (arg[i][0],str) \
               or not e_coordenada(arg[i][1]):
                return False  
        return True
    return False

# x=[('Berlim',[1,0,'N']),('Berlim',[1,0,'N'])] e' suposto dar false?
# r=[('C',[1,0,'N']),('Br',[1,0,'S'])]
# C e Br, apesar de terem direccoes diferentes, tem a mesma coordenada, ta mal
# visto que comecam com letras diferentes

# TESTES
                                               
def respostas_iguais (r1,r2):
    '''
    resposta: resposta x resposta ---> logico
    resposta(lst) recebe dois argumentos do tipo resposta, devolvendo um valor logico que determina se as respostas sao iguais ou nao
    '''        
    if resposta_tamanho(r1) != resposta_tamanho(r2):
        return False
    else:
        for i in range (resposta_tamanho(r1)):
            if (r1[i][0] != r2[i][0]) or not coordenadas_iguais(r1[i][1],r2[i][1]):
                return False
        return True
                        

def res_ordena(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j][0] < lst[i][0]:
                lst[i],lst[j] = lst[j], lst[i]
            
                
    return lst    
            
# r1 =[('Berlim',[1,2,'N']),('Brasilia',[5,2,'S']),('Cad',[0,2,'N'])]
# r2 =[('Brasilia',[5,2,'S']),('Berlim',[1,2,'N']),('Cad',[0,2,'N'])]

# OUTRAS OPERACOES
            
def resposta_string(res):
    '''
    resposta_string: resposta ---> string
    resposta_string(res) recebe um argumento do tipo resposta e 
    devolve a sua representacao externa
    '''       
    guarda = '['
    if e_resposta(res):
        res = res_ordena(res)
        for i in range(len(res)):
            if not i == len(res)-1 :
                guarda = guarda + '<' + (res[i][0]) + ':(' + str(res[i][1][0]) + ', ' + str(res[i][1][1]) + ')-' \
                    + res[i][1][2] + '>, ' 
            else:
                guarda= guarda + '<' + (res[i][0]) + ':(' + str(res[i][1][0]) + ', ' + str(res[i][1][1]) + ')-' \
                    + res[i][1][2] + '>]' 
        return guarda
    
def converte_string(string):
    '''
    converte_string: string ---> string
    converte_string(string) recebe uma string, e se os caracteres forem letras minusculas,
    converte-as em maiusculas, se ja forem maiusculas nada acontece
    '''
    def converte_chr(c):
        char = ord (c)
        if char >= ord('a'):
            return chr(char -32)
        else:
            return c    
    str = ''
    for i in string:
        str = str + converte_chr(i)
    return str
    

#|||||||||||||||||||||||| FUNCOES IMPLEMENTADAS ||||||||||||||||||||||||||||||||


def forma_palavras(lst):
    '''
    forma_palavras: lista ---> lista
    forma_palavras(lst), recebe uma lista e devolve uma lista com as
    palavras a procurar 
    '''    
    indesejado1 = ','
    indesejado2 = ' '
    constroi1 = ''
    constroi2 = []    
    for i in range(10,len(lst[1])):
        a = lst[1][i] # caracter   
        if i == len(lst[1])-1:
            return constroi2 + [constroi1]
        elif a == indesejado1:
            constroi2 = constroi2 + [constroi1]
        elif a == indesejado2:
            constroi1 = ''
        else:  
            constroi1 = constroi1 + converte_string(a)
                    
            
def forma_grelha(lst):
    '''
    forma_grelha: lista ---> lista
    forma_grelha(lst), recebe uma lista e devolve uma lista com a grelha, 
    em que cada elemento da lista e uma string que corresponde a uma linha
    '''    
    elemento = ''
    lista = []
    for i in lst[2:]:
        if i != '' and i != '\n':
            for e in i:
                if ord(e) != 32 and ord(e) != 10: # espaco e \n
                    elemento = elemento + e
            lista = lista + [elemento]
            elemento = ''
    return grelha(lista)
            

#grelha = ['aedy','baxc','cdfd','daac','ebde','ffhi']
#palavras= ['dea','xab','ihf']

def junta_todas(grelha, palavras):
    '''
    junta_todas: grelha x lista ---> resposta
    junta_todas(grelha, palavras) recebe uma grelha e uma lista e devolve 
    uma resposta, onde foi feita uma procura das palavras em todas as direcoes
    '''
    direcoes = ['N', 'S', 'E', 'W','NE', 'NW', 'SE', 'SW']     
    resposta_f = resposta([])    
    for direcao in direcoes:
        resposta_f = resposta_f + procura_palavras_numa_direcao(grelha,palavras,direcao)
    return resposta_f

def procura_palavras_numa_direcao(grelha,palavras,direcao):
    '''
    procura_palavras_numa_direcao: grelha x lista x direcao ---> resposta 
    procura_palavras_numa_direcao(grelha,palavras,direcao) recebe uma grelha, uma lista
    e uma direcao, devolvendo  uma resposta, onde foi feita uma procura das palavras
    nessa direcao
    '''
    if e_direcao(direcao) and e_grelha(grelha) and isinstance(palavras, list):
        res_final = resposta([])
        for palavra in palavras:
            if e_coordenada(encontra_coord_numa_direcao(grelha,palavra,direcao)): #se ha coordenada
                res_final = acrescenta_elemento(res_final,palavra,encontra_coord_numa_direcao(grelha,palavra,direcao)) 
        return res_final

def encontra_coord_numa_direcao(grelha, palavra, direcao): # palavra -> coordenada
    '''
    encontra_coord_numa_direcao: grelha x string x direcao ---> coordenada
    encontra_coord_numa_direcao(grelha, palavra, direcao) recebe uma grelha uma 
    string e uma direcao, e devolve a coordenada correspondente a primeira letra
    da string
    '''
    coord = []
    if e_sul(direcao) or e_norte(direcao):
        for c in range(grelha_nr_colunas(grelha)): # somar colunas para encontrar a tal (c)
            string = grelha_linha(grelha,coordenada(0,c,direcao))                        
            if palavra in string: # pertence a' string? entao vou encontrar o l
                for l in range(grelha_nr_linhas(grelha)): #somar linhas para encontar a tal (l)
                    if palavra == string[l:len(palavra)+l] and e_sul(direcao):
                        return coordenada(l,c,direcao)
                    elif palavra == string[l:len(palavra)+l] and e_norte(direcao):
                        return coordenada(grelha_nr_linhas(grelha)-1-l,c,direcao)
                    
    elif e_leste(direcao) or e_oeste(direcao):
        for l in range(grelha_nr_linhas(grelha)): # somar linhas para encontrar a tal (l)
            string = grelha_linha(grelha,coordenada(l,0,direcao))               
            if palavra in string:
                for c in range(grelha_nr_colunas(grelha)): #somar colunas para encontar a tal (c)
                    if palavra == string[c:len(palavra)+c] and e_leste(direcao):
                        return coordenada(l,c,direcao)
                    elif palavra == string[c:len(palavra)+c] and e_oeste(direcao):
                        return coordenada(l,grelha_nr_colunas(grelha)-1-c,direcao)
                    
    elif e_sudeste(direcao):
        for c in range(grelha_nr_colunas(grelha)): # vou aumentar colunas e ver se esta, nao esta? vou aumentar linhas
            string = grelha_linha(grelha,coordenada(0,c,direcao))
            if palavra in string:
                for l in range(len(string)):# ja tenho coluna, vou saber qual a linha
                    if palavra == string[l:len(palavra)+l]:
                        return coordenada(l,c+l,direcao)
        for l in range(1, grelha_nr_linhas(grelha)):
            string = grelha_linha( grelha, coordenada(l,0,direcao))
            if palavra in string:
                for c in range(grelha_nr_colunas(grelha)):
                    if palavra == string[c,len(palavra)+c]:
                        return coordenada(l+c,c,direcao)
                    
    elif e_noroeste(direcao):
        for l in range(grelha_nr_linhas(grelha)): # vou definir cada linha(somar) fixada na ultima coluna
            string = grelha_linha(grelha, coordenada(l,grelha_nr_colunas(grelha)-1,direcao))
            if palavra in string:
                for c in range(len(string)): 
                    if palavra == string[c:len(palavra)+c]:
                        return coordenada(l-c,grelha_nr_colunas(grelha)-1-c,direcao)
        for c in range(grelha_nr_colunas(grelha)-1): # vai so ate a penultima linha
            string = grelha_linha(grelha, coordenada(grelha_nr_linhas(grelha)-1,c,direcao))
            if palavra in string:
                for l in range(len(string)):
                    if palavra == string[l:len(palavra)+l]:
                        return coordenada(grelha_nr_linhas(grelha)-1-l,c-l,direcao)
                    
    elif e_sudoeste(direcao):
        for c in range(grelha_nr_colunas(grelha)):
            string = grelha_linha(grelha, coordenada(0,c,direcao))
            if palavra in string:
                for l in range(c):
                    if palavra == string[l:len(palavra)+l]:
                        return coordenada(l, c-l, direcao)
        for l in range(1, grelha_nr_linhas(grelha)):
            string = grelha_linha(grelha, coordenada(l,grelha_nr_colunas(grelha)-1, direcao))
            if palavra in string:
                for c in range(len(string)):
                    if palavra == string [c:len(palavra)+c]:
                        return coordenada(l+c, grelha_nr_colunas(grelha)-1-c, direcao)
                    
    elif e_nordeste(direcao):
        for l in range(grelha_nr_linhas(grelha)):
            string = grelha_linha(grelha, coordenada(l,0,direcao))
            if palavra in string:
                for n in range(len(string)-len(palavra)+1):
                    if palavra == string[n:len(palavra)+n]:
                        return coordenada(l-n,n,direcao)
        for c in range(grelha_nr_colunas(grelha)):
            string = grelha_linha(grelha, coordenada(grelha_nr_linhas(grelha)-1, c, direcao))
            n=0
            if palavra in string:
                for n in range(len(string)-len(palavra)+1):
                    if palavra == string[n:len(palavra)+n]:
                        return coordenada(grelha_nr_linhas(grelha)-1-n,c+n,direcao)
            
                           
    
def sopa_letras(ficheiro):
    '''
    sopa_letras: string --> resposta
    sopa_letras(ficheiro) recebe o nome do ficheiro numa string, forma uma grelha,
    e uma lista das palavras a procurar, e procura na grelha as palavras da lista 
    em todas as direcoes devolvendo uma resposta 
    '''
    
    fich = open(ficheiro,'r')
    lst_linhas = fich.readlines()
    
    grelha = forma_grelha(lst_linhas)
    palavras = forma_palavras(lst_linhas)
    res = junta_todas(grelha,palavras)
    janela = janela_sopa_letras(ficheiro)
    janela.mostra_palavras(res)
    janela.termina_jogo()  
    return res