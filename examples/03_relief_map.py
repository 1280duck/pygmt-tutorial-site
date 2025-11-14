import pygmt
from pygmt.datasets import load_earth_relief

def main():
    """基礎 3：地形與海深色階圖。"""
    fig = pygmt.Figure()

    grid = load_earth_relief(resolution="30m", registration="gridline")

    fig.grdimage(
        grid=grid,
        projection="R15c",
        frame="af",
        cmap="geo",
        shading=True,
    )

    fig.colorbar(frame=["a2000", "+L高度/深度 (m)"])

    fig.show()
    # fig.savefig("earth_relief_map.png")

if __name__ == "__main__":
    main()
