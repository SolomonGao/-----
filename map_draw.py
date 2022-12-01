from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


class MyMap(): 
    def to_map_city(self, province, city, variate, update_time):
        pieces = [
            {"max": 999999999999999, "min": 10001, "label": ">10000", "color": "#8A0808"},
            {"max": 9999, "min": 1000, "label": "1000-9999", "color": "#B40404"},
            {"max": 999, "min": 100, "label": "100-999", "color": "#DF0101"},
            {"max": 99, "min": 10, "label": "10-99", "color": "#F5A9A9"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0 ", "color": "#FFFFF"},
        ]

        c = (
            Map(init_opts=opts.InitOpts(width="1500px", height="880px"))
            .add(province+"现确诊人数",[list(z) for z in zip(city, variate)],province,)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=province+"疫情地图分布", subtitle='截止%s '%(update_time), 
                                            pos_left="center", pos_top="30px",),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces),
            )
            .render(f"pandemic_{province}.html")
        )

    def to_map_china(self, area, variate, update_time):
        pieces = [
            {"max": 999999999999999, "min": 10001, "label": ">10000", "color": "#8A0808"},
            {"max": 9999, "min": 1000, "label": "1000-9999", "color": "#B40404"},
            {"max": 999, "min": 100, "label": "100-999", "color": "#DF0101"},
            {"max": 99, "min": 10, "label": "10-99", "color": "#F5A9A9"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0 ", "color": "#FFFFF"},
        ]

        c = (
            Map(init_opts=opts.InitOpts(width="1500px", height="880px"))
            .add("累计确诊人数", [list(z) for z in zip(area, variate)], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布", subtitle='截止%s '%(update_time), 
                                            pos_left="center", pos_top="30px",),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces),
            )
            .render("pandemic_China.html")
        )

