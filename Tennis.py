

jugador1={"puntaje":0}
jugador2={"puntaje":0}


def asignarPuntaje(jugador,puntaje):

    if puntaje==1:
        puntaje=15
    if puntaje==2:
        puntaje=30
    if puntaje==3:
        puntaje=40
    if puntaje==4:
        puntaje=41
    if puntaje==5:
        puntaje=42
        
    if puntaje==0:
        puntaje=0
        
    jugador['puntaje']=puntaje


def recuperarPuntaje(jugador):
    return jugador['puntaje']


def recuperarMarcador():
    
    if (jugador1['puntaje'] == jugador2['puntaje']) and jugador1['puntaje']==40:
        return 'deuce'
    
    if (jugador1['puntaje'] == 41 ) and (jugador2['puntaje'] == 40):
        return 'Advantage PlayerOne'
    
    if (jugador1['puntaje'] == 40 ) and (jugador2['puntaje'] == 41):
        return 'Advantage PlayerTwo'
    
    if (jugador2['puntaje'] == 42):
        return 'PlayerTwo wins'
    
    if (jugador1['puntaje'] == 42):
        return 'PlayerOne wins'
    
    
    return f'{recuperarPuntaje(jugador1)} - {recuperarPuntaje(jugador2)}'


    


# In[26]:


asignarPuntaje(jugador1,53)
asignarPuntaje(jugador2,1)


# In[27]:


recuperarMarcador()


# In[ ]:





# In[ ]:




