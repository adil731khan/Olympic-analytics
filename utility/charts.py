def apply_layout(fig):
    fig.update_layout(template="plotly_white",paper_bgcolor="white",plot_bgcolor="white",
        font=dict(family="Inter",size=14),
        margin=dict(l=20,r=20,t=50,b=20))
    return fig

def line(df,x,y,title):
    fig=plt.line(df,x=x,y=y,markers=True,title=title)
    return apply_layout(fig)

def bar(df,x,y,title):
    fig=plt.bar(df,x=x,y=y,title=title,text=y)
    return apply_layout(fig)

def hbar(df,x,y,title):
    fig=plt.bar(df,x=x,y=y,orientation="h",title=title,text=x)
    return apply_layout(fig)

def pie(df,names,values,title):
    fig=plt.pie(df,names=names,values=values,hole=.5,title=title)
    return apply_layout(fig)