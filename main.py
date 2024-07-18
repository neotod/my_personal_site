import click
import time
import json
from src.neotod_cv import NeotodCV

from src.generate_background import GenerateBackground
from src.generate_skill import GenerateSkill


@click.group()
def cli():
    pass


@cli.command()
@click.argument("skill_name")
@click.argument("n_filled_stars", type=int)
@click.argument("n_max_blank_stars", default=5, type=int)
@click.option("-p", "--print_result", is_flag=True, default=False)
def generate_skill(skill_name, n_filled_stars, n_max_blank_stars, print_result):
    if n_filled_stars > n_max_blank_stars:
        raise click.ClickException("Filled stars can't be bigger than Max blank stars.")

    icon_svg_html = input("Enter skill icon svg html and press enter: \n")

    result = GenerateSkill(
        skill_name, n_filled_stars, icon_svg_html, n_max_blank_stars
    ).run()

    if print_result:
        print("Here ya are :D\n")
        print(result)
    else:
        file_name = f"skill_{int(time.time())}.html"
        with open(f"./{file_name}", "w") as f:
            print(
                f"Skill '{skill_name}' html generated and saved into file {file_name}"
            )
            f.write(result)

    print(
        "Generate html is very ugly in case of formatting, you can apply formatting before using it anywhere."
    )


@cli.command()
@click.option("-c", "--site_parts", default="./site_parts.json")
@click.option("-p", "--print_result", is_flag=True, default=False)
def generate_background(site_parts, print_result):
    with open(site_parts) as f:
        site_parts = json.load(f)

    all_backgrounds_html_str = """<div id="backgrounds" class="col-md-6 col-lg-6">\n"""
    for background_data in site_parts["background"]:
        result = GenerateBackground(**background_data).run()

        all_backgrounds_html_str += result

    all_backgrounds_html_str += "\n</div>"

    if print_result:
        print("Here ya are :D\n")
        print(all_backgrounds_html_str)
    else:
        file_name = f"background_{int(time.time())}.html"

        with open(f"./{file_name}", "w") as f:
            print(f"Backgrounds html generated and saved into file {file_name}")
            f.write(all_backgrounds_html_str)

    print(
        "Generate html is very ugly in case of formatting, you can apply formatting before using it anywhere."
    )


@cli.command()
@click.option("-b", "--base_html_path", default="./base_index.html")
@click.option("-c", "--site_parts_path", default="./site_parts.json")
@click.option("-p", "--print_result", is_flag=True, default=False)
def main(base_html_path, site_parts_path, print_result):
    result = NeotodCV(base_html_path, site_parts_path, print_result).run()

    if print_result:
        print("Here ya are :D\n")
        print(result)
    else:
        file_name = f"index_{int(time.time())}.html"

        with open(f"./{file_name}", "w") as f:
            print(f"HTML generated and saved into file {file_name}")
            f.write(result)

    print(
        "Generated html is very ugly in case of formatting, you can apply formatting before using it anywhere."
    )


if __name__ == "__main__":
    cli()
