import json

from src.generate_background import GenerateBackground
from src.generate_skill import GenerateSkill


class NeotodCV:
    def __init__(self, base_html_path, site_parts_path, print_result=False):
        self.print_result = print_result

        with open(base_html_path) as f:
            self.base_html = f.read()

        with open(site_parts_path) as f:
            self.site_parts = json.load(f)

    def run(self):
        # 1) intro
        intro_str = f"<h1>{self.site_parts['intro']['top']}</h1>"
        intro_str += f"<h1>{self.site_parts['intro']['bottom']}</h1>"

        # 2) job title
        job_title_str = ", ".join(self.site_parts["job_titles"])

        # 3) social media

        # 4) about me
        about_me_str = f"<p>"
        for about_me_line in self.site_parts["about_me"]:
            about_me_str += f"{about_me_line}<br>\n"

        about_me_str += "</p>\n"

        # 5) generate skills
        all_skills_html_str = ""
        for skill_data in self.site_parts["skills"][
            "Languages"
        ]:  # TODO make skills seperated section by section
            result = GenerateSkill(
                skill_data["name"],
                skill_data["level"],
                skill_data["svg_icon_html"],
            ).run()

            all_skills_html_str += result

        all_skills_html_str += "\n"

        # 6) generate background
        all_backgrounds_html_str = """<div id="backgrounds-container-right" class="col-sm-auto col-md-12 col-lg-6 my-auto mt-md-3">\n"""
        for background_data in self.site_parts["background"]:
            result = GenerateBackground(**background_data).run()

            all_backgrounds_html_str += result

        all_backgrounds_html_str += "\n</div>"

        return self.base_html.format(
            intro=intro_str,
            job_title=job_title_str,
            social_media_gitub_url=self.site_parts["social_media"]["github"],
            social_media_linkedin_url=self.site_parts["social_media"]["linkedin"],
            social_media_email_url=self.site_parts["social_media"]["email"],
            about_me=about_me_str,
            skills=all_skills_html_str,
            background=all_backgrounds_html_str,
        )
