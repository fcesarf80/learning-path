def centralizar(jan, larg, alt):
    ltela = jan.winfo_screenwidth() // 2
    atela = jan.winfo_screenheight() // 2

    jlarg = larg // 2
    jalt = alt // 2

    posx = ltela - jlarg
    posy = atela - jalt

    return f"{larg}x{alt}+{posx}+{posy}"