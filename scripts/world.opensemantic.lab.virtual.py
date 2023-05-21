from pathlib import Path

from reusable import WorldCreat, WorldMeta

# Provide information on the page package to be created
package_meta_data = WorldMeta(
    # Package name
    name="OSW Virtual Lab",
    # Package repository name - usually the GitHub repository name
    repo="world.opensemantic.lab.virtual",
    # Package ID - usually the same as repo
    id="world.opensemantic.lab.virtual",
    # Package subdirectory - usually resembling parts of the package name
    subdir="base",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=("For modelling, simulation and optimization"),
    # Specify the package version - use semantic versioning
    version="0.2.0",
    # Author(s)
    author=["Simon Stier", "Andreas Räder"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        "Category:OSW8e511130cecf4d7fa4177c9c65904fc1",  # Model
        "Category:OSWecff4345b4b049218f8d6628dc2f2f21",  # MetaModel
        "Category:OSW553f78cc66194ae1873241207b906c4b",  # BattmoModel
    ],
)
# Provide the information needed (only) to create the page package
package_creation_config = WorldCreat(
    # Specify the path to the working directory - where the package is stored on disk
    working_dir=Path(__file__).parents[1]
    / "packages"
    / package_meta_data.repo,
)
# Create the page package
package_meta_data.create(
    creation_config=package_creation_config,
)
