import pygmt
from pygmt.datasets import load_earth_relief

def main():
    """進階 1：台灣地形陰影圖。"""
    fig = pygmt.Figure()
    region = [118, 123.5, 20, 26]

    grid = load_earth_relief(
        resolution="15s",
        region=region,
        registration="gridline",
    )

    fig.grdimage(
        grid=grid,
        region=region,
        projection="M12c",
        frame=["af", "+tTaiwan relief"],
        cmap="geo",
        shading=True,
    )

    fig.coast(
        region=region,
        projection="M12c",
        shorelines="1p,black",
        borders="1/0.5p,black",
    )

    fig.colorbar(frame=["a1000", "+L高度/深度 (m)"])
    fig.show()
    # fig.savefig("taiwan_relief.png")

if __name__ == "__main__":
    main()
