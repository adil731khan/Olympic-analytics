import matplotlib.pyplot as plt
PRIMARY = "#2563EB"

def line_chart(df, x, y, title):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x],df[y],color=PRIMARY,linewidth=3,marker="o")
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.grid(alpha=0.3)
    return fig

def bar_chart(df, x, y, title):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df[x],df[y],color=PRIMARY)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return fig

def horizontal_bar(df, x, y, title):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(df[y],df[x],color=PRIMARY)
    ax.set_title(title)
    ax.set_xlabel(x)
    return fig

def pie_chart(df, names, values, title):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(df[values],labels=df[names],autopct="%1.1f%%",startangle=90)
    ax.set_title(title)
    return fig