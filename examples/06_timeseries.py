import numpy as np
import pygmt

def main():
    """進階 3：時間序列折線圖。"""
    fig = pygmt.Figure()

    months = np.arange(1, 13)
    values = np.array([0.2, 0.4, 0.8, 1.1, 1.3, 1.0, 0.6, 0.1, -0.2, -0.4, -0.3, 0.0])

    fig.basemap(
        region=[0.5, 12.5, -1.5, 1.5],
        projection="X12c/6c",
        frame=["WSne", "xafg+tMonth", "yafg+tIndex"],
    )

    fig.plot(x=months, y=values, pen="1.5p,blue")
    fig.plot(x=months, y=values, style="c0.2c", fill="blue")

    fig.show()
    # fig.savefig("timeseries_example.png")

if __name__ == "__main__":
    main()
