import pygmt

def main():
    """基礎 1：第一張世界地圖。"""
    fig = pygmt.Figure()

    fig.coast(
        region="g",
        projection="H0/15c",
        frame="afg",
        land="lightgray",
        water="white",
        shorelines="1p,black",
    )

    fig.show()
    # 若要輸出檔案：fig.savefig("first_world_map.png")

if __name__ == "__main__":
    main()
