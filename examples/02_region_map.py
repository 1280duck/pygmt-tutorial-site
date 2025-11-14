import pygmt

def main():
    """基礎 2：畫西太平洋區域地圖。"""
    fig = pygmt.Figure()

    region = "110/160/0/50"  # 110E~160E, 0N~50N

    fig.coast(
        region=region,
        projection="M15c",
        frame=["af", "+tWest Pacific"],
        land="lightgray",
        water="lightblue",
        shorelines="1p,black",
        borders="1/0.5p,black",
    )

    fig.show()
    # fig.savefig("west_pacific_map.png")

if __name__ == "__main__":
    main()
