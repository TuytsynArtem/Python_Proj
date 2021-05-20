for i,pryatki in enumerate(pryatki):
        if t_1.get(pryatki) is not None:
            t_1[pryatki]+=1
        else:
            t_1[pryatki]=1
    klv = list(t_1.keys())
    for i,klvshka in enumerate(klv):
        if  klvshka!=0:
            klv[i]=ability_data["Ability"][klvshka]
        else:
            klv[i]="No t_1 Ability"
    znch = list(t_1.values())
    
    plt.pie(znch,labels=klv,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different t_1 Ability of Pokemons")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()