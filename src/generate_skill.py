class GenerateSkill:
    def __init__(self, skill_name, n_filled_stars, icon_svg_html, n_max_blank_stars=5):
        self.skill_name = skill_name
        self.n_filled_stars = n_filled_stars
        self.n_max_blank_stars = n_max_blank_stars
        self.icon_svg_html = icon_svg_html

        self.yellow_star_html = """<div class="col-1 mx-1 px-0">
    <svg
    id="star"
    xmlns="http://www.w3.org/2000/svg"
    width="15"
    height="15"
    viewBox="0 0 48 48"
    >
    <defs>
        <style>
        .filled_star {
            fill: #ffb500;
            stroke: #fff;
            stroke-linecap: round;
            stroke-width: 0;
            fill-rule: evenodd;
        }
        </style>
    </defs>
    <path
        class="filled_star"
        d="M34.865,39.83l-10.25-5.621-10.153,5.8,2.091-11.647L7.99,20.335l11.542-1.577L24.394,8l5.042,10.672L41,20.047l-8.426,8.173Z"
    />
    </svg>
</div>"""

        self.blank_star_html = """<div class="col-1 mx-1 px-0">
<svg
id="star"
xmlns="http://www.w3.org/2000/svg"
width="15"
height="15"
viewBox="0 0 48 48"
>
<defs>
    <style>
    .empty_star {
        fill: #000000;
        stroke: #fff;
        stroke-linecap: round;
        stroke-width: 0;
        fill-rule: evenodd;
    }
    </style>
</defs>
<path
    class="empty_star"
    d="M34.865,39.83l-10.25-5.621-10.153,5.8,2.091-11.647L7.99,20.335l11.542-1.577L24.394,8l5.042,10.672L41,20.047l-8.426,8.173Z"
/>
</svg>
</div>"""

    def run(self):
        BASE_HTML = """
<div id="skill" class="row col-lg-2 col-md-3 col-sm-5 px-1 py-2 mx-1 my-1 bg-white text-dark">
    <div id="skill-icon-container" class="col-4 mx-auto my-auto">
        {icon_svg_html}
    </div>

    <div id="skill-main-container" class="col-8 mx-auto my-auto">
        <div id="skill-name-container" class="row">
            <h6 class="text-small">{skill_name}</h6>
        </div>

        <div id="skill-stars-container" class="my-auto">
            <div class="row">
                {stars_html}
            </div>
        </div>
    </div>
</div>"""

        return BASE_HTML.format(
            skill_name=self.skill_name,
            icon_svg_html=self.icon_svg_html,
            stars_html=self.get_stars_html(),
        )

    def get_stars_html(self):
        stars_html = ""
        for i in range(self.n_filled_stars):
            stars_html += self.yellow_star_html
        for i in range(self.n_max_blank_stars - self.n_filled_stars):
            stars_html += self.blank_star_html

        return stars_html
