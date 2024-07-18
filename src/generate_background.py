class GenerateBackground:
    def __init__(
        self, title, company_name, start_date, end_date, description, used_skills
    ):
        self.title = title
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.used_skills = used_skills

        self.used_skills_str = """
<div id="background-used-skill-container" class="px-1 py-1 mx-1 my-1 bg-light border text-dark">
	<h6 class="text-small">{skill_name}</h6>
</div>"""

    def run(self):
        self.get_skills_str()

        BASE_HTML = """
<div id="background-container" class="bg-white text-dark py-4 px-4 my-2">
                <div id="background-header" class="row pb-2 border-bottom mb-2">
                  <div
                    id="background-company-name"
                    class="col-5 my-auto mx-auto"
                  >
                    <h2 class="my-auto mx-auto fw-bold">{company_name}</h2>
                  </div>

                  <div id="background-header-right" class="col-7 my-auto mx-auto">
                    <div id="background-role-name" class="row">
                      <h4 class="text-sm-left" style="font-size: 1.5em;">{title}</h4>
                    </div>

                    <div id="background-dates" class="row my-auto mx-auto">
                      {start_date} to {end_date}
                    </div>
                  </div>

                </div>
                <div id="background-description" class="row" style="font-size: 0.9em;">
                  <p>
                    {description}
                  </p>
                </div>

                <div id="background-used-skills" class="d-flex flex-row mt-2 justify-content-start align-items-center flex-wrap">
                  <div id="background-used-skills-text" class="px-3">
                    <h6 class="text-small fw-bold">used skills</h6>
                  </div>

                  {used_skills}
                </div>

</div>"""

        beautified_description_str = ""
        for line in self.description:
            beautified_description_str += f"{line}<br>\n"

        return BASE_HTML.format(
            company_name=self.company_name,
            title=self.title,
            start_date=self.start_date,
            end_date=self.end_date,
            description=beautified_description_str,
            used_skills=self.get_skills_str(),
        )

    def get_skills_str(self):
        skills_str = ""

        for skill_name in self.used_skills:
            skills_str += self.used_skills_str.format(skill_name=skill_name)

        return skills_str
