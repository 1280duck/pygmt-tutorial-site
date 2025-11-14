import pygmt

def main():
    """進階 2：多投影子圖。"""
    fig = pygmt.Figure()

    fig.subplot(
        nrows=2,
        ncols=2,
        figsize=("18c", "12c"),
        frame="af",
        margins=["0.2c", "0.4c"],
        sharex="b",
        sharey="l",
        autolabel=True,
    )

    # Mercator
    fig.subplot_set(panel=0)
    fig.coast(
        region="g",
        projection="M8c",
        frame=["af", "+tMercator"],
        land="lightgray",
        water="white",
        shorelines="0.5p,black",
    )

    # Robinson
    fig.subplot_set(panel=1)
    fig.coast(
        region="g",
        projection="R8c",
        frame=["af", "+tRobinson"],
        land="lightgray",
        water="white",
        shorelines="0.5p,black",
    )

    # Hammer
    fig.subplot_set(panel=2)
    fig.coast(
        region="g",
        projection="H0/8c",
        frame=["af", "+tHammer"],
        land="lightgray",
        water="white",
        shorelines="0.5p,black",
    )

    # Mollweide
    fig.subplot_set(panel=3)
    fig.coast(
        region="g",
        projection="W0/8c",
        frame=["af", "+tMollweide"],
        land="lightgray",
        water="white",
        shorelines="0.5p,black",
    )

    fig.subplot_end()

    fig.show()
    # fig.savefig("projection_subplots.png")

if __name__ == "__main__":
    main()
